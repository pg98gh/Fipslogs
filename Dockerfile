# Basisimage verwenden, z.B. Python für die Ausführung von main.py
FROM python:3.9-slim

# Installiere curl und bash, um kubectl herunterzuladen und auszuführen
RUN apt-get update && apt-get install -y \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Installiere kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/

# Stelle sicher, dass kubectl und bash verfügbar sind
RUN kubectl version --client && bash --version

# Kopiere das Python-Skript in den Container
COPY main.py /app/main.py

# Kopiere das Bash-Skript in den Container (falls du eines hast)
COPY k8s_script.sh /app/k8s_script.sh

# Kopiere die Verzeichnisse templates und static in den Container
COPY templates /app/templates
COPY static /app/static

# Gib das Arbeitsverzeichnis an
WORKDIR /app

# Mache das Bash-Skript ausführbar (optional, falls es verwendet wird)
RUN chmod +x /app/k8s_script.sh

# Installiere alle Python-Abhängigkeiten, falls erforderlich
# (Ersetze requirements.txt mit den benötigten Abhängigkeiten, wenn erforderlich)
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
# Standardbefehl: Ausführen von main.py
CMD ["python", "run.py"]
