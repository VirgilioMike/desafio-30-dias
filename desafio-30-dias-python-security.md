# 🐍 Desafio 30 Dias — Python para Segurança

---

## 📐 Como usar este plano

Cada dia segue a mesma estrutura:

```
🎯 Objetivo      → o que você vai aprender neste dia
🧠 Conceito-chave → o conceito de Python ou lógica que entra em cena
📋 Enunciado     → o que o script deve fazer
💡 Por onde começar → seu primeiro passo concreto
🔐 Contexto real → onde isso aparece no seu trabalho
```

---

## 🗓️ Dia 0 — Configuração do Ambiente *(faça antes de começar)*

**🎯 Objetivo:** Ter o ambiente pronto para nunca travar por problema de setup.

**Checklist:**
- [ ] Instalar Python 3.11+ → https://python.org
- [ ] Instalar VS Code → https://code.visualstudio.com
- [ ] Instalar extensão "Python" no VS Code (by Microsoft)
- [ ] Abrir terminal e rodar: `python --version`
- [ ] Criar pasta `desafio-30-dias/` e dentro dela `dia01/`
- [ ] Criar arquivo `dia01/hello.py` com o conteúdo: `print("Iniciando a jornada!")`
- [ ] Rodar o arquivo e ver a saída no terminal
- [ ] Criar repositório no GitHub e fazer o primeiro commit

**💡 Dica:** No VS Code, use `Ctrl + `` ` para abrir o terminal integrado.

---

# SEMANA 1 — Lógica de Programação e Validação

> **O que você aprende essa semana:**  
> Sintaxe Python do zero: variáveis, strings, condicionais (`if/elif/else`), loops (`for`, `while`), listas e funções simples. Tudo aplicado a problemas reais de segurança.

---

## Dia 01 — Validador de Senhas Fortes

**🎯 Objetivo:** Aprender variáveis, strings, condicionais e o conceito de função.

**🧠 Conceito-chave:** `if / elif / else` + métodos de string (`isupper()`, `islower()`, `isdigit()`)

**📋 Enunciado:**  
Crie um script que receba uma senha e verifique se ela atende à política da empresa:
- Mínimo de 8 caracteres
- Pelo menos 1 letra maiúscula
- Pelo menos 1 letra minúscula
- Pelo menos 1 número
- Pelo menos 1 caractere especial (`!@#$%^&*`)

O script deve imprimir quais critérios passaram e quais falharam, e no final dizer se a senha é **FORTE** ou **FRACA**.

**💡 Por onde começar:**
```python
senha = input("Digite uma senha: ")

# Comece verificando o tamanho:
if len(senha) >= 8:
    print("✅ Tamanho OK")
else:
    print("❌ Senha muito curta")

# Agora tente verificar se tem maiúscula:
# Dica: use any(c.isupper() for c in senha)
```

**🔐 Contexto real:** Toda equipe de AppSec define políticas de senha. Você vai automatizar essa validação em vez de checar manualmente.

---

## Dia 02 — Classificador de Criticidade CVSS

**🎯 Objetivo:** Entender entrada de dados, conversão de tipos e estrutura de decisão encadeada.

**🧠 Conceito-chave:** `float()`, `if / elif / else` em cascata, f-strings

**📋 Enunciado:**  
Crie um script que receba uma pontuação CVSS (número de 0.0 a 10.0) e retorne a classificação correta segundo o padrão CVSS v3:

| Pontuação | Classificação |
|-----------|---------------|
| 0.0       | Nenhuma       |
| 0.1 – 3.9 | Baixa         |
| 4.0 – 6.9 | Média         |
| 7.0 – 8.9 | Alta          |
| 9.0 – 10.0 | Crítica      |

O script deve rejeitar valores fora do intervalo 0–10 com uma mensagem de erro clara.

**💡 Por onde começar:**
```python
pontuacao = float(input("Digite a pontuação CVSS: "))

if pontuacao < 0 or pontuacao > 10:
    print("❌ Pontuação inválida. Deve ser entre 0.0 e 10.0")
elif pontuacao == 0:
    # complete aqui...
```

**🔐 Contexto real:** Você usa isso toda vez que recebe um relatório de scan e precisa priorizar qual vulnerabilidade atacar primeiro.

---

## Dia 03 — Detector de Segredos Hardcoded

**🎯 Objetivo:** Aprender loops `for`, estrutura de listas e busca dentro de strings.

**🧠 Conceito-chave:** `for` loop, `.lower()`, `in` (busca em string), listas

**📋 Enunciado:**  
Crie um script que simule uma linha de um arquivo de código (string) e procure por palavras-chave sensíveis. Se encontrar, deve alertar qual palavra foi encontrada e em qual "linha" ela aparece.

Palavras-chave a buscar:
```
AWS_SECRET, PASSWORD, TOKEN, API_KEY, SECRET_KEY, PRIVATE_KEY, DB_PASSWORD
```

Simule um "arquivo" como uma lista de strings (cada string = uma linha do código).

**💡 Por onde começar:**
```python
palavras_sensiveis = ["password", "token", "api_key", "secret"]

codigo = [
    'username = "admin"',
    'password = "Senha@123"',
    'url = "https://api.empresa.com"',
    'api_key = "sk-abc123xyz"',
]

for numero_linha, linha in enumerate(codigo, start=1):
    # Dica: use linha.lower() para não diferenciar maiúsculas
    # Depois verifique se alguma palavra_sensivel está na linha
    pass
```

**🔐 Contexto real:** É exatamente o que ferramentas SAST como Semgrep e TruffleHog fazem — varrem código buscando por padrões de segredos.

---

## Dia 04 — Filtro de IPs: Internos vs Externos

**🎯 Objetivo:** Trabalhar com listas, loops e condicionais para classificar dados.

**🧠 Conceito-chave:** `.startswith()`, listas, `.append()`, formatação de saída

**📋 Enunciado:**  
Dada uma lista de endereços IP, separe os que pertencem à rede interna dos externos. IPs internos seguem os padrões RFC 1918:
- `10.x.x.x`
- `172.16.x.x` a `172.31.x.x`
- `192.168.x.x`

O script deve exibir duas listas separadas e a contagem de cada uma.

**💡 Por onde começar:**
```python
ips = [
    "10.0.0.5", "200.150.30.1", "192.168.1.10",
    "8.8.8.8", "172.16.5.20", "45.33.32.156"
]

internos = []
externos = []

for ip in ips:
    if ip.startswith("10.") or ip.startswith("192.168."):
        internos.append(ip)
    else:
        externos.append(ip)
        # Dica: a faixa 172.16-31 é mais complexa, tente depois!
```

**🔐 Contexto real:** Em análise de logs e resposta a incidentes, essa separação é o primeiro passo — você só investiga fundo os IPs externos suspeitos.

---

## Dia 05 — Calculadora de Risco Residual

**🎯 Objetivo:** Criar sua primeira função, entender parâmetros e retorno de valores.

**🧠 Conceito-chave:** `def função():`, `return`, operações matemáticas, `round()`

**📋 Enunciado:**  
Crie uma função `calcular_risco()` que receba:
- **Valor do Ativo** (1–100)
- **Probabilidade de Ameaça** (0–100%)
- **Eficácia do Controle** (0–100%)

E calcule o **Risco Residual** com a fórmula:
```
Risco Residual = Valor_Ativo × (Probabilidade / 100) × (1 - Eficácia / 100)
```

Classifique o resultado como: Baixo (< 10), Médio (10–29), Alto (30–59), Crítico (≥ 60).

**💡 Por onde começar:**
```python
def calcular_risco(valor_ativo, probabilidade, eficacia_controle):
    risco = valor_ativo * (probabilidade / 100) * (1 - eficacia_controle / 100)
    return round(risco, 2)

# Teste a função:
resultado = calcular_risco(80, 70, 50)
print(f"Risco Residual: {resultado}")
# Agora adicione a classificação!
```

**🔐 Contexto real:** Gestão de riscos usa exatamente esse tipo de cálculo. Você vai poder criar uma mini-calculadora de risco que hoje faz no Excel.

---

## Dia 06 — Normalizador de URLs

**🎯 Objetivo:** Manipulação avançada de strings, múltiplas condições e boas práticas de função.

**🧠 Conceito-chave:** `.startswith()`, `.endswith()`, `.rstrip()`, f-strings, funções

**📋 Enunciado:**  
Crie uma função `normalizar_url()` que padronize qualquer URL seguindo as regras da empresa:
1. Sempre usar `https://` (nunca `http://`)
2. Nunca terminar com `/`
3. Sempre minúscula
4. Remover espaços extras

Teste com estas entradas:
```python
urls = [
    "http://empresa.com/",
    "HTTPS://SITE.COM",
    "  empresa.com  ",
    "https://api.empresa.com/v1/",
]
```

**💡 Por onde começar:**
```python
def normalizar_url(url):
    url = url.strip()       # Remove espaços
    url = url.lower()       # Tudo minúsculo
    
    if url.startswith("http://"):
        url = url.replace("http://", "https://", 1)
    elif not url.startswith("https://"):
        url = "https://" + url
    
    # Agora remova a barra do final se existir...
    return url
```

**🔐 Contexto real:** Pipelines de CI/CD e scanners DAST precisam de URLs bem formatadas. Uma URL errada pode fazer o scanner pular um endpoint inteiro.

---

## Dia 07 — Gerador de Variações de Payload XSS

**🎯 Objetivo:** Consolidar loops, listas e strings com propósito ofensivo/educativo.

**🧠 Conceito-chave:** `for` com múltiplas listas, f-strings, listas de strings

**📋 Enunciado:**  
Crie um script que gere variações de payloads XSS trocando a tag HTML, o evento e o valor do atributo. O script deve:
1. Gerar todas as combinações possíveis
2. Salvar a lista em um arquivo `payloads.txt`
3. Exibir quantos payloads foram gerados

Use estas listas base:
```python
tags = ["script", "img", "svg", "body", "input"]
eventos = ["onload", "onerror", "onclick", "onmouseover"]
valores = ["alert(1)", "alert('XSS')", "console.log(document.cookie)"]
```

**💡 Por onde começar:**
```python
tags = ["script", "img", "svg"]
eventos = ["onload", "onerror"]
valores = ["alert(1)", "alert('XSS')"]

payloads = []

for tag in tags:
    for evento in eventos:
        for valor in valores:
            payload = f"<{tag} {evento}={valor}>"
            payloads.append(payload)

print(f"Total gerado: {len(payloads)} payloads")
# Agora salve em arquivo!
# Dica: open("payloads.txt", "w") as arquivo:
```

**🔐 Contexto real:** Em testes de Pentest/AppSec, você gera wordlists de payloads para testar WAFs e filtros. Automatizar isso poupa horas.

---

# SEMANA 2 — Arquivos, Parsing e Relatórios

> **O que você aprende essa semana:**  
> Leitura e escrita de arquivos, parsing de CSV e JSON, manipulação de dados estruturados. Você vai criar scripts que leem outputs de ferramentas reais como Nessus e Checkmarx.

---

## Dia 08 — Leitor de Lista de Ativos com Detecção de Duplicatas

**🎯 Objetivo:** Aprender a ler arquivos externos e usar conjuntos (`set`) para lógica de unicidade.

**🧠 Conceito-chave:** `open()`, `readlines()`, `set()`, detecção de duplicatas

**📋 Enunciado:**  
Crie um arquivo `servidores.txt` com uma lista de nomes de servidores (um por linha, com alguns repetidos). O script deve:
1. Ler o arquivo
2. Identificar e listar os servidores duplicados
3. Exibir a lista final sem duplicatas
4. Mostrar estatísticas: total lido, únicos, duplicados

**💡 Por onde começar:**
```python
# Primeiro crie o arquivo servidores.txt manualmente com:
# web01, web02, db01, web01, api01, db01 (um por linha)

with open("servidores.txt", "r") as arquivo:
    linhas = arquivo.readlines()

servidores = [linha.strip() for linha in linhas]  # Remove \n
# Use set() para encontrar únicos
# Compare len(servidores) com len(set(servidores))
```

**🔐 Contexto real:** Inventários de ativos com duplicatas causam gaps de segurança — um servidor "duplicado" pode ser esquecido fora do scope de um scan.

---

## Dia 09 — Parser de CSV de Vulnerabilidades

**🎯 Objetivo:** Ler e filtrar dados de um CSV real, como exports de Nessus ou Checkmarx.

**🧠 Conceito-chave:** módulo `csv`, `DictReader`, filtros por coluna, ordenação

**📋 Enunciado:**  
Crie um arquivo `vulnerabilidades.csv` simulando um export de scanner com as colunas:
`ID, Nome, Severidade, CVSS, Host, Status`

O script deve:
1. Ler o CSV completo
2. Filtrar apenas as vulnerabilidades com Severidade = "Crítica"
3. Ordenar por CVSS (maior primeiro)
4. Exibir em formato de tabela no terminal

**💡 Por onde começar:**
```python
import csv

with open("vulnerabilidades.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    criticas = []
    for linha in leitor:
        if linha["Severidade"] == "Crítica":
            criticas.append(linha)

# Ordene por CVSS:
criticas.sort(key=lambda x: float(x["CVSS"]), reverse=True)

for vuln in criticas:
    print(f"{vuln['ID']} | {vuln['Nome']} | CVSS: {vuln['CVSS']}")
```

**🔐 Contexto real:** Todo analista de vulnerabilidades recebe CSVs de ferramentas. Filtrar manualmente em Excel é lento — esse script faz em segundos.

---

## Dia 10 — Limpador de Falsos Positivos em Logs

**🎯 Objetivo:** Ler, filtrar e reescrever arquivos — o ciclo completo de processamento de logs.

**🧠 Conceito-chave:** leitura + escrita de arquivo, `not in`, lista de exclusões

**📋 Enunciado:**  
Crie um script que leia um arquivo de log (`access.log`) e remova todas as linhas que contenham IPs da lista de "IPs conhecidos" da empresa (IPs internos e sistemas de monitoramento). Salve o resultado em `access_filtrado.log`.

**💡 Por onde começar:**
```python
ips_conhecidos = ["10.0.0.5", "192.168.1.100", "172.16.0.1", "monitoring-bot"]

with open("access.log", "r") as f:
    linhas = f.readlines()

linhas_suspeitas = []
for linha in linhas:
    # Verifique se NENHUM IP conhecido está na linha
    if not any(ip in linha for ip in ips_conhecidos):
        linhas_suspeitas.append(linha)

with open("access_filtrado.log", "w") as f:
    f.writelines(linhas_suspeitas)

print(f"Removidas: {len(linhas) - len(linhas_suspeitas)} linhas")
print(f"Restantes para análise: {len(linhas_suspeitas)} linhas")
```

**🔐 Contexto real:** Em SOC e resposta a incidentes, filtrar ruído de logs é o primeiro passo para encontrar o sinal real de um ataque.

---

## Dia 11 — Conversor de Dicionário para JSON Formatado

**🎯 Objetivo:** Trabalhar com dicionários Python e serialização JSON.

**🧠 Conceito-chave:** `dict`, módulo `json`, `json.dumps()`, `json.dump()`, indentação

**📋 Enunciado:**  
Crie um dicionário Python representando uma vulnerabilidade com os campos:
`id, nome, severidade, cvss, descricao, hosts_afetados, remediacao, status`

O script deve:
1. Converter para JSON formatado (indentado)
2. Salvar em arquivo `vulnerabilidade.json`
3. Ler o arquivo de volta e exibir no terminal

**💡 Por onde começar:**
```python
import json

vulnerabilidade = {
    "id": "CVE-2024-1234",
    "nome": "SQL Injection no módulo de login",
    "severidade": "Crítica",
    "cvss": 9.8,
    "hosts_afetados": ["web01.empresa.com", "web02.empresa.com"],
    "status": "Aberta"
}

# Converta para JSON formatado:
json_formatado = json.dumps(vulnerabilidade, indent=4, ensure_ascii=False)
print(json_formatado)

# Salve em arquivo:
with open("vulnerabilidade.json", "w", encoding="utf-8") as f:
    json.dump(vulnerabilidade, f, indent=4, ensure_ascii=False)
```

**🔐 Contexto real:** APIs de ferramentas como Jira, Defect Dojo e plataformas de GRC trocam dados em JSON. Saber criar e ler JSON é essencial para integrações.

---

## Dia 12 — Monitor de Configuração (.env)

**🎯 Objetivo:** Ler e validar arquivos de configuração, padrão crítico em DevSecOps.

**🧠 Conceito-chave:** parsing manual de arquivo, `split()`, validação de valores

**📋 Enunciado:**  
Crie um arquivo `.env` simulado com variáveis de ambiente. O script deve:
1. Ler o arquivo `.env`
2. Detectar variáveis com valor vazio (ex: `DB_PASSWORD=`)
3. Detectar variáveis com valores claramente inseguros (ex: `password`, `123456`, `admin`)
4. Gerar um relatório de achados

**💡 Por onde começar:**
```python
valores_inseguros = ["password", "123456", "admin", "test", "changeme", "default"]

with open(".env", "r") as f:
    linhas = f.readlines()

for linha in linhas:
    linha = linha.strip()
    if "=" not in linha or linha.startswith("#"):
        continue
    
    chave, _, valor = linha.partition("=")
    
    if not valor:
        print(f"⚠️  VAZIO: {chave}")
    elif valor.lower() in valores_inseguros:
        print(f"🔴 INSEGURO: {chave}={valor}")
```

**🔐 Contexto real:** Variáveis de ambiente vazias ou com valores padrão são um vetor comum de incidentes. Esse check entra em pipelines CI/CD antes do deploy.

---

## Dia 13 — Verificador de Integridade com SHA-256

**🎯 Objetivo:** Usar módulo de criptografia nativo do Python para verificação de integridade.

**🧠 Conceito-chave:** módulo `hashlib`, leitura binária de arquivo, comparação de hashes

**📋 Enunciado:**  
Crie um script que:
1. Calcule o hash SHA-256 de qualquer arquivo
2. Compare com um hash "esperado" (baseline)
3. Alerte se o arquivo foi modificado
4. Bonus: leia uma lista de arquivos + hashes esperados de um JSON e verifique todos

**💡 Por onde começar:**
```python
import hashlib

def calcular_sha256(caminho_arquivo):
    sha256 = hashlib.sha256()
    
    with open(caminho_arquivo, "rb") as f:  # "rb" = leitura binária
        while bloco := f.read(4096):        # Lê em blocos (arquivos grandes)
            sha256.update(bloco)
    
    return sha256.hexdigest()

hash_atual = calcular_sha256("arquivo_teste.txt")
hash_esperado = "abc123..."  # Cole aqui um hash gerado antes

if hash_atual == hash_esperado:
    print("✅ Integridade OK — arquivo não foi modificado")
else:
    print("🚨 ALERTA — arquivo foi modificado!")
```

**🔐 Contexto real:** Verificação de integridade é usada em cadeia de custódia forense, validação de artefatos de build e detecção de tampering em configurações críticas.

---

## Dia 14 — Gerador Automático de Relatório em Markdown

**🎯 Objetivo:** Consolidar toda a Semana 2 — ler dados, processar e gerar output formatado.

**🧠 Conceito-chave:** f-strings multi-linha, escrita de arquivo, função com múltiplos parâmetros, `datetime`

**📋 Enunciado:**  
Crie um script interativo que peça informações ao usuário e gere um relatório de pentest em Markdown (.md):
- Nome do projeto / cliente
- Escopo testado
- Lista de vulnerabilidades encontradas (ID, nome, severidade)
- Conclusão

O relatório deve ter data/hora automática, sumário executivo e tabela de vulnerabilidades.

**💡 Por onde começar:**
```python
from datetime import datetime

def gerar_relatorio(projeto, escopo, vulnerabilidades):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    relatorio = f"""# Relatório de Pentest — {projeto}
**Data:** {data}  
**Escopo:** {escopo}

## Sumário Executivo
...

## Vulnerabilidades Encontradas

| ID | Nome | Severidade |
|----|------|------------|
"""
    for vuln in vulnerabilidades:
        relatorio += f"| {vuln['id']} | {vuln['nome']} | {vuln['severidade']} |\n"
    
    return relatorio

# Salve com open("relatorio.md", "w")
```

**🔐 Contexto real:** Relatórios de pentest consomem horas do analista. Um gerador de templates poupa tempo e padroniza a entrega para o cliente.

---

# SEMANA 3 — Requisições HTTP e Integrações com APIs

> **O que você aprende essa semana:**  
> Fazer requisições HTTP, consumir APIs REST, trabalhar com JSON de respostas e integrar com ferramentas externas via Webhook. Esta semana você para de rodar scripts locais e começa a falar com o mundo externo.

**Antes de começar:** instale a biblioteca requests:
```bash
pip install requests
```

---

## Dia 15 — Verificador de Security Headers HTTP

**🎯 Objetivo:** Fazer sua primeira requisição HTTP e analisar headers de resposta.

**🧠 Conceito-chave:** `requests.get()`, `response.headers`, dicionários, checklist de segurança

**📋 Enunciado:**  
Crie um script que receba uma URL e verifique a presença dos principais security headers:

| Header | Por que importa |
|--------|-----------------|
| `Strict-Transport-Security` | Força HTTPS |
| `X-Frame-Options` | Previne Clickjacking |
| `X-Content-Type-Options` | Previne MIME sniffing |
| `Content-Security-Policy` | Controla recursos carregados |
| `Referrer-Policy` | Controla vazamento de URL |

Exiba o resultado com ✅ (presente) ou ❌ (ausente) para cada header.

**💡 Por onde começar:**
```python
import requests

url = input("Digite a URL para verificar: ")

headers_esperados = [
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "Referrer-Policy",
]

try:
    resposta = requests.get(url, timeout=10, verify=True)
    print(f"\nStatus: {resposta.status_code}")
    print(f"Servidor: {resposta.headers.get('Server', 'não informado')}\n")
    
    for header in headers_esperados:
        if header in resposta.headers:
            print(f"✅ {header}: {resposta.headers[header][:60]}")
        else:
            print(f"❌ {header}: AUSENTE")
except Exception as e:
    print(f"Erro: {e}")
```

**🔐 Contexto real:** Checagem de security headers é parte de qualquer assessment de AppSec e aparece em OWASP Top 10. Ferramentas como securityheaders.com fazem exatamente isso.

---

## Dia 16 — Consulta de CVEs via API do NIST

**🎯 Objetivo:** Consumir uma API pública REST e extrair dados de uma resposta JSON.

**🧠 Conceito-chave:** API REST, `response.json()`, navegação em JSON aninhado, parâmetros de query

**📋 Enunciado:**  
Crie um script que consulte a API pública do NIST NVD (National Vulnerability Database) passando um CVE ID e exiba:
- Descrição da vulnerabilidade
- CVSS Score e vetor
- Data de publicação
- Status

API base: `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-XXXX-XXXXX`

**💡 Por onde começar:**
```python
import requests

cve_id = input("Digite o CVE ID (ex: CVE-2021-44228): ")
url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"

resposta = requests.get(url, timeout=15)

if resposta.status_code == 200:
    dados = resposta.json()
    
    # Navegue no JSON: dados → vulnerabilities → [0] → cve
    cve = dados["vulnerabilities"][0]["cve"]
    
    descricao = cve["descriptions"][0]["value"]
    print(f"\n📋 {cve_id}")
    print(f"Descrição: {descricao[:200]}...")
    
    # Tente extrair o CVSS score do caminho:
    # cve → metrics → cvssMetricV31 → [0] → cvssData → baseScore
```

**🔐 Contexto real:** Em gestão de vulnerabilidades, você cruza CVEs de scanners com a NVD para obter descrições e scores atualizados. Isso normalmente é feito manualmente.

---

## Dia 17 — Scanner de Subdomínios Básico

**🎯 Objetivo:** Fazer múltiplas requisições HTTP em sequência e tratar erros por requisição.

**🧠 Conceito-chave:** loop com `requests`, `try/except` por iteração, timeout, status codes

**📋 Enunciado:**  
Crie um script que receba um domínio base e tente uma lista de subdomínios comuns, verificando quais respondem com HTTP 200. Salve os ativos encontrados em `subdominios_ativos.txt`.

```python
subdomains = ["www", "mail", "api", "dev", "staging", "admin", 
              "portal", "vpn", "remote", "ftp", "blog", "app"]
```

**💡 Por onde começar:**
```python
import requests

dominio = input("Domínio base (ex: empresa.com): ")
subdomains = ["www", "mail", "api", "dev", "staging", "admin"]

ativos = []

for sub in subdomains:
    url = f"https://{sub}.{dominio}"
    try:
        resposta = requests.get(url, timeout=5, verify=False)
        if resposta.status_code == 200:
            print(f"✅ ATIVO: {url}")
            ativos.append(url)
        else:
            print(f"🟡 {url} → {resposta.status_code}")
    except:
        print(f"❌ {url} → sem resposta")
```

**⚠️ Atenção ética:** Use apenas em domínios que você tem autorização para testar.

**🔐 Contexto real:** Reconhecimento de superfície de ataque começa por enumeração de subdomínios. Este é um script educativo equivalente ao `subfinder` ou `amass` em escala pequena.

---

## Dia 18 — Alerta Automático via Webhook (Slack/Teams)

**🎯 Objetivo:** Enviar dados via POST para uma URL de Webhook externa.

**🧠 Conceito-chave:** `requests.post()`, JSON body, Webhook, headers de requisição

**📋 Enunciado:**  
Crie um script que simule a detecção de um evento crítico de segurança e envie um alerta para um canal do Slack via Webhook. O alerta deve conter:
- Tipo de evento
- Severidade
- Host afetado
- Timestamp
- Recomendação de ação

**💡 Por onde começar:**
```python
import requests
import json
from datetime import datetime

# Para testar sem Slack: use https://webhook.site para gerar um endpoint gratuito
WEBHOOK_URL = "https://hooks.slack.com/services/SEU_WEBHOOK_AQUI"

def enviar_alerta(evento, severidade, host):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    mensagem = {
        "text": f"🚨 *ALERTA DE SEGURANÇA*",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Evento:* {evento}\n*Severidade:* {severidade}\n*Host:* {host}\n*Hora:* {timestamp}"
                }
            }
        ]
    }
    
    resposta = requests.post(WEBHOOK_URL, json=mensagem)
    return resposta.status_code

# Dica: use https://webhook.site para testes sem precisar do Slack
```

**🔐 Contexto real:** Alertas automáticos de segurança via Slack/Teams são padrão em pipelines DevSecOps. Você vai parar de mandar e-mail manual para o time.

---

## Dia 19 — Verificador de Expiração de Certificado SSL

**🎯 Objetivo:** Usar socket e ssl para inspecionar certificados TLS/SSL programaticamente.

**🧠 Conceito-chave:** módulos `ssl` e `socket`, `datetime`, cálculo de diferença de datas

**📋 Enunciado:**  
Crie um script que se conecte a uma URL e exiba:
- Data de expiração do certificado
- Quantos dias faltam para expirar
- Alerta se faltar menos de 30 dias
- Alerta crítico se faltar menos de 7 dias

**💡 Por onde começar:**
```python
import ssl
import socket
from datetime import datetime

def verificar_ssl(hostname):
    ctx = ssl.create_default_context()
    
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        s.connect((hostname, 443))
        cert = s.getpeercert()
    
    data_expiracao_str = cert["notAfter"]
    data_expiracao = datetime.strptime(data_expiracao_str, "%b %d %H:%M:%S %Y %Z")
    dias_restantes = (data_expiracao - datetime.utcnow()).days
    
    print(f"🔒 Host: {hostname}")
    print(f"📅 Expira em: {data_expiracao.strftime('%d/%m/%Y')}")
    print(f"⏳ Dias restantes: {dias_restantes}")
    
    if dias_restantes < 7:
        print("🔴 CRÍTICO — certificado expira em menos de 7 dias!")
    elif dias_restantes < 30:
        print("🟡 ATENÇÃO — certificado expira em menos de 30 dias")

verificar_ssl("google.com")
```

**🔐 Contexto real:** Certificados SSL expirados causam indisponibilidade e alertas de segurança no browser. Monitorar isso proativamente é parte do trabalho de AppSec.

---

## Dia 20 — Download e Verificação de Artefato de Segurança

**🎯 Objetivo:** Baixar um arquivo via HTTP e verificar sua integridade com hash (combina Dias 13 e 16).

**🧠 Conceito-chave:** `requests` com stream download, `hashlib`, escrita binária de arquivo

**📋 Enunciado:**  
Crie um script que:
1. Baixe um arquivo de uma URL (simule um relatório/artefato de ferramenta)
2. Salve localmente
3. Calcule o SHA-256 do arquivo baixado
4. Compare com o hash publicado (simule como se fosse um `checksums.txt`)
5. Confirme se o download foi íntegro

**💡 Por onde começar:**
```python
import requests
import hashlib

def baixar_arquivo(url, destino):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(destino, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"✅ Download concluído: {destino}")

def verificar_integridade(caminho, hash_esperado):
    sha256 = hashlib.sha256()
    with open(caminho, "rb") as f:
        while bloco := f.read(4096):
            sha256.update(bloco)
    
    hash_real = sha256.hexdigest()
    return hash_real == hash_esperado

# Teste com qualquer URL de arquivo público
```

**🔐 Contexto real:** Em pipelines de CI/CD, artefatos (imagens Docker, binários) devem ter integridade verificada antes do deploy. Isso previne supply chain attacks.

---

## Dia 21 — Identificador de Tecnologias via Headers HTTP

**🎯 Objetivo:** Extrair e analisar informações de fingerprinting a partir de headers HTTP.

**🧠 Conceito-chave:** dicionário de mapeamentos, `response.headers`, lógica de detecção por padrão

**📋 Enunciado:**  
Crie um script que analise os headers de resposta de uma URL e tente identificar:
- Servidor web (nginx, apache, IIS, etc.)
- Linguagem/framework de backend
- CDN ou WAF em uso
- Versões expostas (e alerte sobre isso)

**💡 Por onde começar:**
```python
import requests

tecnologias = {
    "nginx": ["nginx"],
    "apache": ["apache"],
    "microsoft IIS": ["iis", "microsoft-iis"],
    "cloudflare": ["cloudflare"],
    "AWS": ["awselb", "amazon"],
}

url = input("URL para fingerprint: ")
resposta = requests.get(url, timeout=10)

servidor = resposta.headers.get("Server", "").lower()
x_powered = resposta.headers.get("X-Powered-By", "").lower()

print(f"Server header: {servidor}")
print(f"X-Powered-By: {x_powered}")

for tech, palavras in tecnologias.items():
    for palavra in palavras:
        if palavra in servidor or palavra in x_powered:
            print(f"🔍 Detectado: {tech}")
```

**🔐 Contexto real:** Fingerprinting é a etapa de reconhecimento em qualquer teste. Identificar versões expostas em headers é um achado comum — `Server: Apache/2.2.15` já diz muito para um atacante.

---

## Dia 21.A — Bônus: Anatomia de uma API REST (curl → Python)

**🎯 Objetivo:** Entender métodos HTTP, paths, bodies e headers na prática — traduzindo curl para Python.

**🧠 Conceito-chave:** verbos HTTP (GET, POST, PUT, PATCH, DELETE), path params, query params, request body, status codes semânticos

**📋 Enunciado:**

Antes de consumir APIs em Python, você precisa entender o que está mandando. Neste dia, você vai:

1. Estudar os 5 métodos HTTP principais com exemplos de segurança
2. Traduzir cada curl para Python com `requests`
3. Analisar o que cada resposta significa

**🧠 Guia rápido — Métodos HTTP:**

| Método | Semântica | Exemplo de uso em AppSec |
|--------|-----------|--------------------------|
| `GET` | Buscar/ler recurso | Consultar CVE, listar vulnerabilidades |
| `POST` | Criar novo recurso | Abrir ticket de vuln, criar alerta |
| `PUT` | Substituir recurso inteiro | Atualizar status completo de um ativo |
| `PATCH` | Atualizar parcialmente | Mudar só o status de uma vuln para "Resolvida" |
| `DELETE` | Remover recurso | Excluir um falso positivo do sistema |

**📋 Exercício — Traduza cada curl para Python:**

```bash
# curl 1: GET com query param
curl "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228"

# curl 2: POST com body JSON e header de autenticação
curl -X POST https://api.defectdojo.example.com/api/v2/findings/ \
  -H "Authorization: Token abc123" \
  -H "Content-Type: application/json" \
  -d '{"title": "SQL Injection", "severity": "Critical", "active": true}'

# curl 3: PATCH para atualizar apenas o status
curl -X PATCH https://api.example.com/vulnerabilities/42 \
  -H "Authorization: Bearer token_aqui" \
  -d '{"status": "resolved"}'

# curl 4: DELETE
curl -X DELETE https://api.example.com/false-positives/99 \
  -H "Authorization: Bearer token_aqui"
```

**💡 Traduções em Python:**

```python
import requests

BASE = "https://api.example.com"
HEADERS = {
    "Authorization": "Bearer SEU_TOKEN",
    "Content-Type": "application/json"
}

# GET com query param
resposta = requests.get(
    f"{BASE}/vulnerabilities",
    params={"severity": "critical", "status": "open"},
    headers=HEADERS
)

# POST criando um finding
nova_vuln = {
    "title": "SQL Injection no endpoint /login",
    "severity": "Critical",
    "active": True,
    "description": "Parâmetro 'user' vulnerável a injeção"
}
resposta = requests.post(f"{BASE}/findings/", json=nova_vuln, headers=HEADERS)
print(f"Criado com status: {resposta.status_code}")  # 201 = Created

# PATCH atualizando só o status
resposta = requests.patch(
    f"{BASE}/vulnerabilities/42",
    json={"status": "resolved"},
    headers=HEADERS
)

# DELETE
resposta = requests.delete(f"{BASE}/false-positives/99", headers=HEADERS)
print(f"Deletado: {resposta.status_code}")  # 204 = No Content
```

**🧠 Status codes que você precisa conhecer:**

| Código | Significado | Quando aparece |
|--------|-------------|----------------|
| 200 | OK | GET bem-sucedido |
| 201 | Created | POST criou recurso |
| 204 | No Content | DELETE ou PATCH sem body de retorno |
| 400 | Bad Request | Body malformado, campo faltando |
| 401 | Unauthorized | Token ausente ou inválido |
| 403 | Forbidden | Token válido mas sem permissão |
| 404 | Not Found | ID ou path errado |
| 429 | Too Many Requests | Rate limit atingido |
| 500 | Internal Server Error | Bug na API — reportar ao time |

**🔐 Contexto real:** Em AppSec você vai interagir com APIs de Defect Dojo, Jira, SonarQube, Checkmarx, Tenable e muitas outras. Saber a diferença entre um 401 e um 403 já te poupa 30 minutos de debug.

---

## Dia 21.B — Bônus: Testador de Endpoints de API com Autenticação

**🎯 Objetivo:** Construir um script que teste múltiplos endpoints de uma API, validando autenticação, métodos permitidos e respostas esperadas.

**🧠 Conceito-chave:** dicionário de rotas, autenticação via header, validação de status code, detecção de endpoints sem auth

**📋 Enunciado:**

Crie um script `api_tester.py` que:
1. Receba uma `BASE_URL` e um `TOKEN` de autenticação
2. Teste uma lista de endpoints com seus métodos e payloads
3. Verifique se cada endpoint exige autenticação (tente sem token também)
4. Detecte endpoints que retornam dados sensíveis sem autenticação (BOLA/BFLA)
5. Gere um relatório resumido com os achados

**💡 Por onde começar:**

```python
import requests

BASE_URL = "https://sua-api.com"
TOKEN = "SEU_TOKEN_AQUI"

# Defina os endpoints a testar: método, path, payload, status esperado
endpoints = [
    {"metodo": "GET",    "path": "/api/v1/users",          "payload": None, "status_ok": 200},
    {"metodo": "GET",    "path": "/api/v1/users/1",         "payload": None, "status_ok": 200},
    {"metodo": "POST",   "path": "/api/v1/findings",        "payload": {"title": "test", "severity": "Low"}, "status_ok": 201},
    {"metodo": "DELETE", "path": "/api/v1/findings/999",    "payload": None, "status_ok": 204},
    {"metodo": "GET",    "path": "/api/v1/admin/settings",  "payload": None, "status_ok": 403},
]

headers_auth    = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
headers_sem_auth = {"Content-Type": "application/json"}

achados = []

for ep in endpoints:
    url = BASE_URL + ep["path"]
    metodo = ep["metodo"].lower()
    
    # Testa COM autenticação
    try:
        resp_auth = getattr(requests, metodo)(url, json=ep["payload"], headers=headers_auth, timeout=8)
    except Exception as e:
        print(f"❌ Erro em {ep['metodo']} {ep['path']}: {e}")
        continue

    # Testa SEM autenticação
    resp_sem_auth = getattr(requests, metodo)(url, json=ep["payload"], headers=headers_sem_auth, timeout=8)

    status_com    = resp_auth.status_code
    status_sem    = resp_sem_auth.status_code
    status_ok     = ep["status_ok"]

    # Detecta endpoint sem proteção de auth
    if status_sem in [200, 201] and ep["metodo"] != "GET":
        achado = f"🔴 BFLA: {ep['metodo']} {ep['path']} retornou {status_sem} SEM token!"
        achados.append(achado)
        print(achado)
    elif status_sem == 200 and ep["path"].find("admin") != -1:
        achado = f"🔴 Endpoint admin acessível sem auth: {ep['path']}"
        achados.append(achado)
        print(achado)
    else:
        ok = "✅" if status_com == status_ok else "⚠️ "
        print(f"{ok} {ep['metodo']:6} {ep['path']:35} com auth: {status_com} | sem auth: {status_sem}")

print(f"\n{'='*50}")
print(f"Total de achados: {len(achados)}")
```

**🔐 Contexto real:** BOLA (Broken Object Level Authorization) e BFLA (Broken Function Level Authorization) são os dois primeiros itens do OWASP API Security Top 10. Esse script automatiza o teste básico dessas categorias — algo que você hoje faz manualmente no Postman ou Burp.

---

# SEMANA 4 — Orientação a Objetos e Scripts Avançados

> **O que você aprende essa semana:**  
> Orientação a Objetos (POO) do zero, argumentos de linha de comando, automação complexa e estruturação de ferramentas reutilizáveis. Você vai deixar de escrever scripts soltos e começar a escrever ferramentas.

> **Por que POO agora?**  
> Depois de 3 semanas escrevendo funções, você naturalmente percebeu que alguns dados "pertencem juntos". POO é o jeito formal de organizar isso. Uma `Vulnerabilidade` tem ID, nome, severidade — faz sentido que eles fiquem no mesmo objeto.

---

## Dia 22 — Classe Vulnerability

**🎯 Objetivo:** Entender classes, atributos e métodos — o coração da POO.

**🧠 Conceito-chave:** `class`, `__init__()`, `self`, métodos, `__str__()`

**📋 Enunciado:**  
Crie uma classe `Vulnerability` que organize dados de uma vulnerabilidade com os atributos:
`id, nome, severidade, cvss, host, status, data_descoberta`

E os métodos:
- `is_critical()` → retorna True se CVSS ≥ 9.0
- `to_dict()` → retorna os dados como dicionário
- `to_json()` → retorna os dados como string JSON
- `__str__()` → representação legível para `print()`

**💡 Por onde começar:**
```python
import json
from datetime import date

class Vulnerability:
    def __init__(self, id, nome, severidade, cvss, host, status="Aberta"):
        self.id = id
        self.nome = nome
        self.severidade = severidade
        self.cvss = cvss
        self.host = host
        self.status = status
        self.data_descoberta = date.today().isoformat()
    
    def is_critical(self):
        return self.cvss >= 9.0
    
    def __str__(self):
        return f"[{self.severidade}] {self.id} — {self.nome} (CVSS: {self.cvss})"

# Teste:
v = Vulnerability("CVE-2021-44228", "Log4Shell", "Crítica", 10.0, "web01")
print(v)
print(v.is_critical())
```

**🔐 Contexto real:** Plataformas como Defect Dojo e Faraday organizam vulnerabilidades exatamente assim — como objetos com propriedades e métodos.

---

## Dia 23 — Gerenciador de Ativos com POO

**🎯 Objetivo:** Criar relacionamento entre classes e uma classe "gerenciadora".

**🧠 Conceito-chave:** múltiplas classes, lista de objetos, métodos CRUD (create, read, update, delete)

**📋 Enunciado:**  
Crie duas classes:
- `Ativo` — representa um servidor (hostname, ip, tipo, criticidade, owner)
- `Inventario` — gerencia uma coleção de ativos com métodos: `adicionar()`, `remover()`, `buscar_por_ip()`, `listar_criticos()`, `exportar_json()`

**💡 Por onde começar:**
```python
class Ativo:
    def __init__(self, hostname, ip, tipo, criticidade, owner):
        self.hostname = hostname
        self.ip = ip
        self.tipo = tipo           # "web", "banco", "api", etc.
        self.criticidade = criticidade  # "Alta", "Média", "Baixa"
        self.owner = owner

class Inventario:
    def __init__(self):
        self.ativos = []
    
    def adicionar(self, ativo):
        self.ativos.append(ativo)
        print(f"✅ Ativo adicionado: {ativo.hostname}")
    
    def listar_criticos(self):
        return [a for a in self.ativos if a.criticidade == "Alta"]
    
    # Implemente: remover(), buscar_por_ip(), exportar_json()
```

**🔐 Contexto real:** Gerenciamento de ativos (CMDB) é fundamento de qualquer programa de segurança. Um inventário desatualizado é ponto cego para ataques.

---

## Dia 24 — Analisador de Dockerfile para Má Práticas

**🎯 Objetivo:** Parser de arquivo texto com lógica de detecção de padrões — aplicado a DevSecOps.

**🧠 Conceito-chave:** leitura de arquivo linha a linha, `.startswith()`, detecção de padrões, relatório

**📋 Enunciado:**  
Crie um script que leia um Dockerfile e aponte problemas de segurança:
- Imagem base `latest` (sem versão pinada)
- Uso de `USER root` explícito
- `ADD` em vez de `COPY` (pode fazer download de URLs)
- `--no-check-certificate` ou `--insecure` em comandos
- Secrets hardcoded (`ENV PASSWORD=`, `ENV TOKEN=`)
- `RUN apt-get install` sem `--no-install-recommends`

**💡 Por onde começar:**
```python
regras = [
    ("latest", "⚠️  Imagem sem versão pinada (use tag específica)"),
    ("USER root", "🔴 Uso explícito de root"),
    ("ADD http", "🟡 ADD com URL — prefira COPY + download separado"),
    ("ENV PASSWORD", "🔴 Possível secret hardcoded"),
    ("ENV TOKEN", "🔴 Possível token hardcoded"),
    ("--no-check-certificate", "🔴 Verificação de certificado desabilitada"),
]

with open("Dockerfile", "r") as f:
    linhas = f.readlines()

achados = []
for num, linha in enumerate(linhas, 1):
    for padrao, mensagem in regras:
        if padrao in linha:
            achados.append(f"Linha {num}: {mensagem}")

for achado in achados:
    print(achado)
```

**🔐 Contexto real:** Análise estática de Dockerfiles é parte do pipeline DevSecOps. Ferramentas como Hadolint fazem isso — você está construindo uma versão educativa.

---

## Dia 25 — Script de Força Bruta Educativo (Hash MD5)

**🎯 Objetivo:** Entender como ataques de dicionário funcionam na prática — para defendê-los melhor.

**🧠 Conceito-chave:** `hashlib.md5()`, leitura de wordlist, loop de tentativas, timing

**📋 Enunciado:**  
Crie um script que tente "recuperar" uma senha a partir do seu hash MD5 usando uma wordlist. O script deve:
1. Receber um hash MD5 como input
2. Carregar uma wordlist (arquivo de palavras)
3. Testar cada palavra
4. Exibir a senha se encontrada + quantas tentativas levou
5. Exibir o tempo total de execução

**💡 Por onde começar:**
```python
import hashlib
import time

def md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

hash_alvo = input("Hash MD5 a quebrar: ")
wordlist = "wordlist.txt"  # Crie um arquivo com senhas comuns

inicio = time.time()

with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
    for tentativa, linha in enumerate(f, 1):
        senha = linha.strip()
        if md5(senha) == hash_alvo:
            print(f"✅ Senha encontrada: {senha}")
            print(f"Tentativas: {tentativa} | Tempo: {time.time()-inicio:.2f}s")
            break
```

**⚠️ Aviso ético:** Use apenas para fins educativos e em ambientes controlados. Crie uma wordlist de teste com 20-30 palavras comuns.

**🔐 Contexto real:** Entender como brute force funciona é essencial para definir políticas de senha, lockout e armazenamento seguro com salt + bcrypt.

---

## Dia 26 — Extrator de Links Inseguros de HTML

**🎯 Objetivo:** Parsing de HTML para encontrar vulnerabilidades de mixed content.

**🧠 Conceito-chave:** módulo `re` (regex básico) ou `html.parser`, busca de padrões em texto

**📋 Enunciado:**  
Crie um script que receba o conteúdo HTML de uma página e extraia todos os links (`href`, `src`). Classifique cada link como:
- 🟢 HTTPS — seguro
- 🔴 HTTP — inseguro (mixed content)
- 🟡 Relativo — sem protocolo definido

**💡 Por onde começar:**
```python
import re
import requests

url = input("URL da página para analisar: ")
html = requests.get(url, timeout=10).text

# Padrão para encontrar href= e src=
padrao = r'(?:href|src)=["\']([^"\']+)["\']'
links = re.findall(padrao, html)

http_links = []
https_links = []
relativos = []

for link in links:
    if link.startswith("https://"):
        https_links.append(link)
    elif link.startswith("http://"):
        http_links.append(link)
    else:
        relativos.append(link)

print(f"🟢 HTTPS: {len(https_links)}")
print(f"🔴 HTTP (inseguros): {len(http_links)}")
for link in http_links:
    print(f"   → {link}")
```

**🔐 Contexto real:** Mixed content (HTTPS página + HTTP recurso) é um achado de AppSec — o recurso HTTP pode ser interceptado mesmo numa página HTTPS.

---

## Dia 27 — Verificador de Permissões de Arquivos (Linux)

**🎯 Objetivo:** Usar módulo `os` para interagir com o sistema de arquivos e detectar configurações inseguras.

**🧠 Conceito-chave:** `os.walk()`, `os.stat()`, `oct()`, permissões Unix

**📋 Enunciado:**  
Crie um script que percorra um diretório e identifique arquivos com permissões inseguras:
- World-writable (qualquer um pode escrever): permissão `xxx2`, `xxx3`, `xxx6`, `xxx7`
- SUID/SGID bit ativado
- Arquivos `.env`, `.key`, `.pem` com permissões abertas demais

**💡 Por onde começar:**
```python
import os
import stat

diretorio = input("Diretório para verificar: ")

for raiz, dirs, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        caminho = os.path.join(raiz, arquivo)
        try:
            permissoes = os.stat(caminho).st_mode
            octal = oct(permissoes)[-3:]  # Últimos 3 dígitos
            
            # World-writable: último dígito ≥ 2
            if int(octal[-1]) in [2, 3, 6, 7]:
                print(f"⚠️  World-writable: {caminho} ({octal})")
        except PermissionError:
            pass
```

**🔐 Contexto real:** Arquivos world-writable em servidores Linux são vetores de privilege escalation e persistência de atacante. Isso é checado em hardening e CIS Benchmarks.

---

## Dia 28 — Analisador de Git Diff para Segurança

**🎯 Objetivo:** Usar `subprocess` para rodar comandos do sistema e analisar o output.

**🧠 Conceito-chave:** módulo `subprocess`, parsing de texto, detecção de padrões em diff

**📋 Enunciado:**  
Crie um script que rode `git diff` entre dois commits e analise o output buscando por:
- Novos segredos hardcoded (`password=`, `token=`, `secret=`)
- Novas funções de conexão com banco (`connect(`, `mysql_connect`, `psycopg2.connect`)
- Remoção de linhas de log/audit (possível tentativa de evasão)

**💡 Por onde começar:**
```python
import subprocess

def rodar_git_diff(commit_antigo="HEAD~1", commit_novo="HEAD"):
    resultado = subprocess.run(
        ["git", "diff", commit_antigo, commit_novo],
        capture_output=True,
        text=True,
        cwd="."  # Diretório do repositório
    )
    return resultado.stdout

padroes_perigosos = ["password=", "token=", "secret=", ".connect(", "mysql_connect"]

diff = rodar_git_diff()

for num, linha in enumerate(diff.split("\n"), 1):
    if linha.startswith("+"):  # Linha adicionada no diff
        for padrao in padroes_perigosos:
            if padrao.lower() in linha.lower():
                print(f"🚨 Linha {num}: {linha.strip()}")
                print(f"   Padrão detectado: {padrao}")
```

**🔐 Contexto real:** Análise de diff em pull requests é onde SAST e secret scanners como GitLeaks e Semgrep entram em ação nos pipelines CI/CD.

---

## Dia 29 — Simulador de Firewall Log + Detecção de Padrão de Ataque

**🎯 Objetivo:** Gerar dados sintéticos, analisar padrões e detectar anomalias — como um SIEM básico.

**🧠 Conceito-chave:** módulo `random`, `collections.Counter`, análise de frequência, thresholds

**📋 Enunciado:**  
Parte 1 — Gerador: Crie um script que gere 1000 linhas de log de firewall aleatórias com: timestamp, IP origem, IP destino, porta, protocolo, ação (ALLOW/DENY).

Parte 2 — Detector: Analise os logs gerados e detecte:
- IPs com mais de 50 tentativas no mesmo destino (possível port scan)
- IPs com mais de 20 DENYs (possível ataque)
- Concentração de acessos numa porta específica (ex: SSH 22, RDP 3389)

**💡 Por onde começar:**
```python
import random
from datetime import datetime, timedelta
from collections import Counter

def gerar_logs(quantidade=1000):
    ips_atacantes = ["185.234.56.78", "103.21.244.0", "45.33.32.156"]
    ips_normais = [f"10.0.0.{i}" for i in range(1, 50)]
    portas = [22, 80, 443, 3389, 8080, 3306, 5432]
    
    logs = []
    for i in range(quantidade):
        # 20% de chance de ser um atacante
        ip_origem = random.choice(ips_atacantes if random.random() < 0.2 else ips_normais)
        log = {
            "ip_origem": ip_origem,
            "porta": random.choice(portas),
            "acao": random.choice(["ALLOW", "ALLOW", "DENY"])
        }
        logs.append(log)
    return logs

logs = gerar_logs()

# Analise: quem tem mais DENYs?
ip_denys = Counter(l["ip_origem"] for l in logs if l["acao"] == "DENY")
for ip, count in ip_denys.most_common(5):
    if count > 20:
        print(f"🚨 Suspeito: {ip} com {count} DENYs")
```

**🔐 Contexto real:** Detecção de anomalias em logs é o coração de um SIEM. Splunk, ELK e Sentinel fazem isso em escala — você está construindo a lógica base.

---

# 🏆 Dia 30 — PROJETO FINAL: Orquestrador DevSecOps

**🎯 Objetivo:** Integrar tudo que você aprendeu em 29 dias num único script profissional.

**🧠 Conceito-chave:** Arquitetura de script, módulos, POO, APIs, relatório JSON, Webhook

**📋 Enunciado:**  
Crie um script `devsecops_scanner.py` que execute as seguintes etapas em sequência:

### Etapa 1 — Configuração
Leia um arquivo `config.json` com:
```json
{
  "alvo": "https://example.com",
  "slack_webhook": "https://...",
  "headers_esperados": ["Strict-Transport-Security", "X-Frame-Options"],
  "cvss_minimo_critico": 9.0
}
```

### Etapa 2 — Verificação de Security Headers
Execute a lógica do Dia 15 usando os headers do `config.json`.

### Etapa 3 — Verificação de SSL
Execute a lógica do Dia 19 no alvo configurado.

### Etapa 4 — Geração de Relatório JSON
Consolide todos os achados num objeto `RelatorioSeguranca` com:
- Data/hora da execução
- Alvo verificado
- Headers presentes e ausentes
- Status do SSL + dias para expirar
- Score de risco geral (0–100)
- Lista de recomendações

### Etapa 5 — Salvar Relatório
Salve o relatório em `relatorio_YYYYMMDD_HHMMSS.json`.

### Etapa 6 — Enviar Alerta
Envie um resumo via Webhook (Slack/Teams) com o score de risco e os achados críticos.

**💡 Estrutura sugerida:**
```python
class RelatorioSeguranca:
    def __init__(self, alvo):
        self.alvo = alvo
        self.data = datetime.now().isoformat()
        self.achados = []
        self.score_risco = 100  # Começa em 100, desconta por achado
    
    def adicionar_achado(self, tipo, descricao, severidade):
        self.achados.append({...})
        if severidade == "Alta":
            self.score_risco -= 20
        elif severidade == "Média":
            self.score_risco -= 10

def executar_pipeline():
    config = carregar_config("config.json")
    relatorio = RelatorioSeguranca(config["alvo"])
    
    verificar_headers(config["alvo"], relatorio)
    verificar_ssl(config["alvo"], relatorio)
    
    salvar_relatorio(relatorio)
    enviar_alerta(config["slack_webhook"], relatorio)

if __name__ == "__main__":
    executar_pipeline()
```

**🔐 Contexto real:** Este é um pipeline DevSecOps funcional. Com pequenas adaptações, ele pode rodar num GitHub Actions ou Jenkins a cada deploy.

---

## 📊 Mapa de Progressão

| Semana | Foco | Conceitos Python | Relevância |
|--------|------|-----------------|------------|
| 1 | Lógica e Validação | variáveis, if/else, loops, funções | AppSec, GRC |
| 2 | Arquivos e Parsing | CSV, JSON, open(), hashlib | Análise de Vuln |
| 3 | HTTP e APIs | requests, REST, Webhooks, SSL | DevSecOps |
| 4 | POO e Avançado | classes, subprocess, os, regex | Tooling próprio |

## 🧰 Bibliotecas que você vai dominar

- `hashlib` — hashing e integridade
- `csv`, `json` — parsing de dados
- `requests` — requisições HTTP
- `ssl`, `socket` — inspeção de certificados
- `os`, `subprocess` — interação com sistema
- `datetime` — timestamps e datas
- `re` — expressões regulares básicas
- `collections` — estruturas avançadas

## 🎓 Checkpoint de Aprendizado

Ao final dos 30 dias, você será capaz de:
- ✅ Escrever scripts Python do zero sem depender de tutoriais
- ✅ Automatizar verificações de segurança que hoje faz manualmente
- ✅ Consumir APIs de ferramentas de segurança (NVD, scanners, SIEMs)
- ✅ Gerar relatórios automatizados em JSON e Markdown
- ✅ Estruturar ferramentas reutilizáveis com POO
- ✅ Entender como ataques funcionam para defendê-los melhor

---

*Boa jornada! Um commit por dia. 30 dias. Sem pular.*  
*"A automação não substitui o analista — ela libera o analista para pensar."*
