---
name: meta-ads-ratos
description: Gerencia campanhas Meta Ads (Facebook/Instagram) via SDK oficial. Le campanhas, conjuntos, anuncios, criativos e insights. Cria, edita, pausa, duplica e deleta objetos. Busca interesses, comportamentos e geolocalizacoes para targeting. Troca url_tags em criativos existentes. Use quando o usuario mencionar meta ads, facebook ads, instagram ads, campanha, conjunto de anuncios, ad set, criativo, targeting, publico, insights, metricas de anuncio, duplicar campanha, url_tags, utm, criar campanha, pausar campanha, orcamento de campanha, audiencia, lookalike, pixel. Tambem dispara com /meta-ads-ratos setup.
---

# Meta Ads Ratos

Skill completa para gestao de Meta Ads via SDK oficial (`facebook-business`). Substitui o MCP fb-ads-mcp-server com mais poder: duplicacao de campanhas/ads, swap de url_tags, e acesso total a API.

## Setup

Na primeira vez, rode o install wizard:

```bash
python3 ~/.claude/skills/meta-ads-ratos/scripts/setup.py
```

Se faltar algo:
1. Instalar SDK: `pip3 install facebook-business`
2. Configurar token: `export META_ADS_TOKEN="seu-token"` no `~/.zshrc`
3. Configurar conta padrao (opcional): `export META_AD_ACCOUNT_ID="act_123"` no `~/.zshrc`

## Como usar

Todos os scripts estao em `~/.claude/skills/meta-ads-ratos/scripts/`. O padrao e:

```
python3 <script>.py <subcomando> [argumentos]
```

O Claude deve interpretar o pedido do usuario e executar o script correto via Bash.

---

## Referencia rapida de operacoes

### Leitura (read.py)

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `accounts` | Lista contas de anuncio | `read.py accounts` |
| `account-details` | Detalhes de uma conta | `read.py account-details --id act_123` |
| `campaigns` | Lista campanhas | `read.py campaigns --account act_123 --status ACTIVE` |
| `campaign` | Detalhes de uma campanha | `read.py campaign --id 123` |
| `adsets` | Lista ad sets de uma conta | `read.py adsets --account act_123` |
| `adsets-by-campaign` | Ad sets de uma campanha | `read.py adsets-by-campaign --campaign 123` |
| `adset` | Detalhes de um ad set | `read.py adset --id 123` |
| `adsets-by-ids` | Varios ad sets por IDs | `read.py adsets-by-ids --ids 123,456` |
| `ads` | Lista ads de uma conta | `read.py ads --account act_123 --status ACTIVE` |
| `ads-by-campaign` | Ads de uma campanha | `read.py ads-by-campaign --campaign 123` |
| `ads-by-adset` | Ads de um ad set | `read.py ads-by-adset --adset 123` |
| `ad` | Detalhes de um ad | `read.py ad --id 123` |
| `creative` | Detalhes de um criativo | `read.py creative --id 123` |
| `creatives-by-ad` | Criativos de um ad | `read.py creatives-by-ad --ad 123` |
| `preview` | Preview HTML de criativo | `read.py preview --creative 123` |
| `images` | Lista imagens da conta | `read.py images --account act_123` |
| `videos` | Lista videos da conta | `read.py videos --account act_123` |
| `activities` | Log de atividades da conta | `read.py activities --account act_123` |
| `activities-by-adset` | Atividades de um ad set | `read.py activities-by-adset --adset 123` |
| `custom-audiences` | Lista audiencias custom | `read.py custom-audiences --account act_123` |
| `lookalike-audiences` | Lista audiencias lookalike | `read.py lookalike-audiences --account act_123` |
| `paginate` | Busca URL de paginacao | `read.py paginate --url "https://..."` |

### Insights (insights.py)

| Subcomando | Exemplo |
|---|---|
| `account` | `insights.py account --id act_123 --date-preset last_7d` |
| `campaign` | `insights.py campaign --id 123 --date-preset last_30d --breakdowns age,gender` |
| `adset` | `insights.py adset --id 123 --time-range '{"since":"2026-03-01","until":"2026-03-31"}'` |
| `ad` | `insights.py ad --id 123 --date-preset yesterday` |
| `async` | `insights.py async --id act_123 --date-preset maximum --level campaign` |

Parametros comuns de insights: `--date-preset`, `--time-range` (JSON), `--time-increment`, `--breakdowns`, `--level`, `--action-breakdowns`, `--filtering` (JSON), `--sort`, `--limit`

### Targeting (targeting.py)

| Subcomando | Exemplo |
|---|---|
| `interests` | `targeting.py interests --q "design grafico"` |
| `interest-suggestions` | `targeting.py interest-suggestions --ids 123,456` |
| `behaviors` | `targeting.py behaviors --locale pt_BR` |
| `demographics` | `targeting.py demographics` |
| `geolocations` | `targeting.py geolocations --q "Porto Alegre" --types city` |
| `validate` | `targeting.py validate --account act_123 --spec '{...}'` |
| `reach` | `targeting.py reach --account act_123 --spec '{...}'` |
| `delivery` | `targeting.py delivery --account act_123 --spec '{...}' --daily-budget 5000` |
| `describe` | `targeting.py describe --account act_123 --spec '{...}'` |

### Criacao (create.py)

| Subcomando | Exemplo |
|---|---|
| `campaign` | `create.py campaign --account act_123 --name "LEADS-Teste" --objective OUTCOME_LEADS` |
| `adset` | `create.py adset --account act_123 --name "Publico-Frio" --campaign 123 --optimization-goal LINK_CLICKS --targeting '{...}' --daily-budget 5000` |
| `ad` | `create.py ad --account act_123 --name "Carrossel-V1" --adset 123 --creative '{"creative_id":"456"}'` |
| `creative` | `create.py creative --account act_123 --name "Criativo-V1" --object-story-spec '{...}' --url-tags "utm_source=facebook&utm_medium=cpc"` |
| `image` | `create.py image --account act_123 --url "https://exemplo.com/imagem.jpg"` |
| `video` | `create.py video --account act_123 --url "https://exemplo.com/video.mp4"` |
| `custom-audience` | `create.py custom-audience --account act_123 --name "Compradores-2026"` |
| `lookalike` | `create.py lookalike --account act_123 --name "LAL-Compradores" --source 123 --spec '{"country":"BR","ratio":0.01}'` |

**IMPORTANTE:** Todas as criacoes sao feitas com status PAUSED. Revisar antes de ativar.

### Edicao (update.py)

| Subcomando | Exemplo |
|---|---|
| `campaign` | `update.py campaign --id 123 --status ACTIVE --daily-budget 10000` |
| `adset` | `update.py adset --id 123 --targeting '{...}' --daily-budget 5000` |
| `ad` | `update.py ad --id 123 --status PAUSED` |
| `audience-users` | `update.py audience-users --id 123 --schema EMAIL --data '[["hash1"]]' --action add` |

### Exclusao (delete.py)

| Subcomando | Exemplo |
|---|---|
| `object` | `delete.py object --id 123` |
| `audience` | `delete.py audience --id 123` |

### Avancado (advanced.py) -- NOVIDADES

| Subcomando | O que faz | Exemplo |
|---|---|---|
| `swap-url-tags` | Troca url_tags de um ad existente | `advanced.py swap-url-tags --ad 123 --url-tags "utm_source=facebook&utm_medium=cpc&utm_campaign=leads"` |
| `duplicate-ad` | Duplica ad com novos url_tags | `advanced.py duplicate-ad --id 123 --adset 456 --url-tags "utm_source=facebook"` |
| `duplicate-adset` | Duplica ad set | `advanced.py duplicate-adset --id 123 --campaign 456` |
| `duplicate-campaign` | Duplica campanha inteira | `advanced.py duplicate-campaign --id 123 --deep` |

O `swap-url-tags` resolve o problema de nao poder editar url_tags em criativos existentes: cria um criativo novo identico com os url_tags corretos e troca no ad.

O `--deep` no `duplicate-campaign` duplica tambem todos os ad sets e ads da campanha.

---

## Regras de seguranca

O Claude DEVE seguir estas regras ao executar operacoes:

1. **Criar sempre PAUSED** -- nunca criar objetos com status ACTIVE diretamente
2. **Confirmar antes de deletar** -- perguntar ao usuario antes de executar delete
3. **Confirmar antes de ativar** -- perguntar antes de mudar status para ACTIVE
4. **Respeitar rate limits** -- o SDK ja inclui delays entre operacoes de escrita (1s). Se receber erro de rate limit (codigos 17, 32, 80004), aguardar 60 segundos antes de tentar novamente
5. **Orcamento com cuidado** -- ao alterar daily_budget ou lifetime_budget, confirmar o valor com o usuario. Valores sao em centavos (5000 = R$50,00)
6. **Nunca hardcodar tokens** -- sempre usar a env var META_ADS_TOKEN

## Fluxos comuns

### Criar campanha completa
1. `create.py campaign` -- cria campanha PAUSED
2. `create.py adset` -- cria ad set PAUSED com targeting
3. `create.py image` ou `create.py video` -- sobe midia
4. `create.py creative` -- cria criativo com url_tags
5. `create.py ad` -- cria ad PAUSED linkando criativo ao ad set
6. Revisar tudo com o usuario
7. `update.py campaign --status ACTIVE` -- ativar

### Corrigir url_tags de ads existentes

**IMPORTANTE:** Criativos na Meta sao imutaveis. Nao da pra editar url_tags, URL de destino, imagem ou texto de um criativo existente via API. Isso vale especialmente pra criativos baseados em posts organicos (effective_object_story_id) -- a URL vem do post original e nao pode ser alterada.

**O fluxo correto e duplicar o ad com criativo novo:**
1. `read.py ads-by-campaign --campaign XXX` -- listar ads
2. `read.py creatives-by-ad --ad XXX` -- ver criativo atual e url_tags
3. Criar novo criativo usando o `object_story_id` do original + url_tags corretos
4. Criar novo ad PAUSED no mesmo ad set com o criativo novo
5. Ativar o novo ad
6. Pausar o ad antigo

Pra criativos de post organico, usar a API direta:
```bash
# Criar criativo com url_tags corretos reusando o post original
POST act_XXX/adcreatives
  name: "nome [url_tags_fix]"
  object_story_id: "PAGE_ID_POST_ID"  (do effective_object_story_id do criativo antigo)
  url_tags: "utm_source=facebook&utm_medium=cpc&utm_campaign=NOME_CAMPANHA"

# Criar novo ad PAUSED
POST act_XXX/ads
  name: "nome [url_tags_fix]"
  adset_id: MESMO_ADSET
  creative: {"creative_id": "NOVO_ID"}
  status: PAUSED
  tracking_specs: (copiar do ad original)

# Ativar novo, pausar antigo
POST novo_ad_id  status=ACTIVE
POST antigo_ad_id  status=PAUSED
```

### Duplicar campanha para teste A/B
1. `advanced.py duplicate-campaign --id XXX --deep` -- copia tudo
2. `update.py adset --id NOVO_ADSET --targeting '{...}'` -- alterar targeting
3. `update.py campaign --id NOVA_CAMPANHA --name "Teste B"` -- renomear
4. Ativar quando pronto

### Puxar relatorio de performance
1. `insights.py campaign --id XXX --date-preset last_30d --breakdowns age,gender`
2. Ou para relatorio pesado: `insights.py async --id act_XXX --date-preset maximum --level ad`
