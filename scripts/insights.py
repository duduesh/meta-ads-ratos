#!/usr/bin/env python3
"""
Meta Ads Ratos - Insights & Reporting
Subcommands: account, campaign, adset, ad, async
"""

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (
    init_api,
    resolve_account,
    print_json,
    handle_fb_error,
    print_error,
    parse_fields,
    parse_json_arg,
    add_account_arg,
    add_fields_arg,
)

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad

# ---------------------------------------------------------------------------
# Default fields
# ---------------------------------------------------------------------------

DEFAULT_INSIGHTS_FIELDS = [
    "impressions",
    "clicks",
    "spend",
    "cpc",
    "cpm",
    "ctr",
    "actions",
    "cost_per_action_type",
    "reach",
    "frequency",
]

DATE_PRESET_CHOICES = [
    "today",
    "yesterday",
    "this_month",
    "last_month",
    "this_quarter",
    "last_3d",
    "last_7d",
    "last_14d",
    "last_28d",
    "last_30d",
    "last_90d",
    "maximum",
]

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _add_insights_args(parser):
    """Add all common insight arguments to a subparser."""
    add_fields_arg(parser)
    parser.add_argument(
        "--date-preset",
        default="last_30d",
        choices=DATE_PRESET_CHOICES,
        help="Date preset (default: last_30d)",
    )
    parser.add_argument(
        "--time-range",
        help='JSON time range: \'{"since":"2024-01-01","until":"2024-01-31"}\'',
    )
    parser.add_argument(
        "--time-increment",
        default="all_days",
        help="Time increment: 1, 7, 14, 28, monthly, all_days (default: all_days)",
    )
    parser.add_argument(
        "--breakdowns",
        help="Comma-separated breakdowns: age,gender,country,region,publisher_platform,platform_position,device_platform,impression_device",
    )
    parser.add_argument(
        "--level",
        choices=["account", "campaign", "adset", "ad"],
        help="Aggregation level",
    )
    parser.add_argument(
        "--action-breakdowns",
        help="Comma-separated action breakdowns",
    )
    parser.add_argument(
        "--filtering",
        help="JSON filtering spec",
    )
    parser.add_argument(
        "--sort",
        help="Sort field (prefix with - for descending)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Result limit (default: 25)",
    )
    parser.add_argument("--after", help="Pagination cursor (next page)")
    parser.add_argument("--before", help="Pagination cursor (previous page)")


def _build_insights_params(args):
    """Build the params dict from parsed arguments."""
    params = {}

    if args.date_preset and not args.time_range:
        params["date_preset"] = args.date_preset
    if args.time_range:
        params["time_range"] = parse_json_arg(args.time_range, "time-range")
    if args.time_increment:
        params["time_increment"] = args.time_increment
    if args.breakdowns:
        params["breakdowns"] = args.breakdowns.split(",")
    if args.level:
        params["level"] = args.level
    if args.action_breakdowns:
        params["action_breakdowns"] = args.action_breakdowns.split(",")
    if args.filtering:
        params["filtering"] = parse_json_arg(args.filtering, "filtering")
    if args.sort:
        params["sort"] = [args.sort]
    if args.limit:
        params["limit"] = args.limit
    if getattr(args, "after", None):
        params["after"] = args.after
    if getattr(args, "before", None):
        params["before"] = args.before

    return params


def _resolve_fields(args):
    """Resolve fields from args or return defaults."""
    if args.fields:
        return parse_fields(args.fields)
    return list(DEFAULT_INSIGHTS_FIELDS)


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------


@handle_fb_error
def cmd_account(args):
    """Account-level insights."""
    init_api()
    account_id = resolve_account(getattr(args, "id", None) or getattr(args, "account", None))
    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    account = AdAccount(account_id)
    cursor = account.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(results)


@handle_fb_error
def cmd_campaign(args):
    """Campaign-level insights."""
    init_api()
    if not args.id:
        print_error("--id e obrigatorio para insights de campanha.")
        sys.exit(1)

    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    campaign = Campaign(args.id)
    cursor = campaign.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(results)


@handle_fb_error
def cmd_adset(args):
    """Ad set-level insights."""
    init_api()
    if not args.id:
        print_error("--id e obrigatorio para insights de ad set.")
        sys.exit(1)

    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    adset = AdSet(args.id)
    cursor = adset.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(results)


@handle_fb_error
def cmd_ad(args):
    """Ad-level insights."""
    init_api()
    if not args.id:
        print_error("--id e obrigatorio para insights de ad.")
        sys.exit(1)

    fields = _resolve_fields(args)
    params = _build_insights_params(args)

    ad = Ad(args.id)
    cursor = ad.get_insights(fields=fields, params=params)
    results = [item for item in cursor]
    print_json(results)


@handle_fb_error
def cmd_async(args):
    """Async report for heavy queries."""
    init_api()
    account_id = resolve_account(getattr(args, "id", None) or getattr(args, "account", None))
    fields = _resolve_fields(args)
    params = _build_insights_params(args)
    poll_interval = args.poll_interval

    account = AdAccount(account_id)
    report = account.get_insights_async(fields=fields, params=params)

    print(f"Async report criado: {report['id']}", file=sys.stderr)
    print(f"Aguardando conclusao (poll a cada {poll_interval}s)...", file=sys.stderr)

    while True:
        report = report.api_get()
        status = report.get("async_status", "Unknown")
        pct = report.get("async_percent_completion", 0)

        print(f"  Status: {status} ({pct}%)", file=sys.stderr)

        if status == "Job Completed":
            break
        if status in ("Job Failed", "Job Skipped"):
            print_error(f"Report falhou com status: {status}")
            sys.exit(1)

        time.sleep(poll_interval)

    print("Buscando resultados...", file=sys.stderr)
    cursor = report.get_result()
    results = [item for item in cursor]
    print_json(results)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads Insights & Reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcomando")

    # account
    p_account = subparsers.add_parser("account", help="Account-level insights")
    p_account.add_argument("--id", help="Account ID (default: META_AD_ACCOUNT_ID)")
    add_account_arg(p_account)
    _add_insights_args(p_account)
    p_account.set_defaults(func=cmd_account)

    # campaign
    p_campaign = subparsers.add_parser("campaign", help="Campaign insights")
    p_campaign.add_argument("--id", required=True, help="Campaign ID")
    _add_insights_args(p_campaign)
    p_campaign.set_defaults(func=cmd_campaign)

    # adset
    p_adset = subparsers.add_parser("adset", help="Ad set insights")
    p_adset.add_argument("--id", required=True, help="Ad set ID")
    _add_insights_args(p_adset)
    p_adset.set_defaults(func=cmd_adset)

    # ad
    p_ad = subparsers.add_parser("ad", help="Ad insights")
    p_ad.add_argument("--id", required=True, help="Ad ID")
    _add_insights_args(p_ad)
    p_ad.set_defaults(func=cmd_ad)

    # async
    p_async = subparsers.add_parser("async", help="Async report (heavy queries)")
    p_async.add_argument("--id", help="Account ID (default: META_AD_ACCOUNT_ID)")
    add_account_arg(p_async)
    _add_insights_args(p_async)
    p_async.add_argument(
        "--poll-interval",
        type=int,
        default=5,
        help="Poll interval in seconds (default: 5)",
    )
    p_async.set_defaults(func=cmd_async)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
