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

## Disclaimer: use com responsabilidade

Essa skill foi **vibe-codada com Claude Code** a partir da documentacao oficial do [facebook-business SDK](https://github.com/facebook/facebook-python-business-sdk) e da [Meta Marketing API](https://developers.facebook.com/docs/marketing-api/). Ela e um projeto experimental que estamos comecando a testar agora.

**Pontos importantes antes de usar:**

- **Use por sua conta e risco.** Nos nao garantimos que o uso dessa skill nao vai resultar em restricoes, bloqueios ou qualquer problema na sua conta de anuncios. A Meta tem politicas proprias sobre automacao e pode mudar as regras a qualquer momento.
- **Leia as politicas da Meta.** Antes de usar qualquer automacao, entenda os [Termos de Servico da Meta](https://www.facebook.com/policies/ads/) e as [regras de rate limiting da Marketing API](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/). A skill inclui delays entre operacoes de escrita, mas isso nao e garantia de nada.
- **Revise o codigo.** Essa skill tem acesso de leitura e escrita na sua conta de anuncios. Antes de usar, avalie o codigo dos scripts pra entender o que cada operacao faz. E open source justamente pra isso.
- **Campanhas sempre nascem pausadas.** Por seguranca, toda criacao via skill e feita com status PAUSED. Mas operacoes de edicao e exclusao agem diretamente nos objetos. Tenha cuidado.
- **Sem garantia de funcionamento.** O SDK e a API da Meta mudam com frequencia. Algo que funciona hoje pode quebrar amanha. Se algo parar de funcionar, provavelmente e uma mudanca na API -- nao no seu setup.

Em resumo: e uma ferramenta poderosa, mas voce e o responsavel pelo que acontece na sua conta. Use com consciencia, teste em contas de teste primeiro se possivel, e nao faca nada que voce nao faria manualmente no Ads Manager.

## Criado por

[Ratos de IA](https://ratosdeia.com.br) - Curso Claude Code OS
