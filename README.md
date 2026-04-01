# Meta Ads Ratos

Skill de Meta Ads para Claude Code. Gerencia campanhas no Facebook e Instagram via SDK oficial da Meta (`facebook-business`).

**54 operacoes** organizadas em 7 scripts:
- **read.py** - 22 operacoes de leitura (campanhas, ad sets, ads, criativos, audiencias)
- **insights.py** - 5 operacoes de metricas e relatorios
- **targeting.py** - 9 operacoes de busca de interesses, comportamentos e geolocalizacao
- **create.py** - 8 operacoes de criacao (campanhas, ad sets, ads, criativos, imagens, videos, audiencias)
- **update.py** - 4 operacoes de edicao
- **delete.py** - 2 operacoes de exclusao
- **advanced.py** - 4 operacoes avancadas (duplicacao, swap de url_tags)

## Instalacao rapida

```bash
# 1. Copiar a skill para a pasta do Claude Code
cp -r . ~/.claude/skills/meta-ads-ratos/

# 2. Instalar o SDK da Meta
pip3 install facebook-business

# 3. Configurar as variaveis de ambiente (adicionar ao ~/.zshrc ou ~/.bashrc)
export META_ADS_TOKEN="seu-token-aqui"
export META_AD_ACCOUNT_ID="act_123456789"

# 4. Verificar a instalacao
python3 ~/.claude/skills/meta-ads-ratos/scripts/setup.py
```

## Como obter o token

1. Acesse [Meta for Developers](https://developers.facebook.com/)
2. Crie um App do tipo "Business"
3. Adicione o produto "Marketing API"
4. No Business Manager, crie um System User e gere um token com permissoes `ads_management` e `ads_read`

Tutorial completo: [ratosdeia.com.br/assets/tutorial-meta-ads-ratos](https://ratosdeia.com.br/assets/tutorial-meta-ads-ratos)

## Uso

Depois de instalada, a skill e ativada automaticamente quando voce fala com o Claude Code sobre Meta Ads. Exemplos:

- "lista as campanhas ativas da minha conta"
- "cria uma campanha de leads com orcamento de R$50/dia"
- "pega as metricas dos ultimos 7 dias da campanha X"
- "duplica essa campanha e troca os url_tags"

## Criado por

[Ratos de IA](https://ratosdeia.com.br) - Curso Claude Code OS
