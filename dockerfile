FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Copia os arquivos de configuração do projeto
COPY pyproject.toml uv.lock requirements.txt ./

# Instala as dependências usando o uv de forma ultra rápida
RUN uv pip install --system -r requirements.txt

# Copia o resto do código
COPY . .

# Comando padrão para rodar o mutmut
CMD ["mutmut", "run"]