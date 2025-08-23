# Imagen base oficial de Python
FROM mcr.microsoft.com/devcontainers/python:3.11

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crea directorio de trabajo
WORKDIR /workspace

# Copia los requirements si existen
COPY requirements.txt* /workspace/

# Instala dependencias de Python
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Usuario que usará VSCode
USER vscode
