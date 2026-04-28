# stress-tester
FastAPI Stress Tester & Observability Stack

Este projeto é um laboratório de SRE e DevOps projetado para demonstrar o ciclo completo de observabilidade: instrumentação, coleta de métricas e visualização de dados em tempo real.

A aplicação consiste em uma API que gera carga sintética na CPU, permitindo observar o comportamento do sistema através de dashboards dinâmicos.
🛠️ Tecnologias Utilizadas

    Backend: Python 3.10 + FastAPI

    Servidor ASGI: Uvicorn

    Monitoramento: Prometheus

    Visualização: Grafana

    Containerização: Docker & Docker Compose

    Instrumentação: Prometheus FastAPI Instrumentator

🏗️ Arquitetura do Projeto

O ecossistema é orquestrado via Docker Compose, dividindo-se em três camadas:

    Application Layer: API FastAPI expondo endpoints de negócio e um endpoint /metrics.

    Collection Layer: Prometheus realizando scraping (coleta) dos dados a cada 5 segundos.

    Visualization Layer: Grafana conectado ao Prometheus para exibição de dashboards.

    🚀 Como Executar
Pré-requisitos

    Docker

    Docker Compose V2

Passo a Passo

    Clone o repositório:
    Bash

    git clone https://github.com/seu-usuario/stress-tester-sre.git
    cd stress-tester-sre

    Suba o ambiente:
    Bash

    docker compose up --build -d

    Acesse as ferramentas:

        API: http://localhost:8000

        Prometheus: http://localhost:9090

        Grafana: http://localhost:3000 (Login/Senha: admin/admin)

📈 Testando a Observabilidade

Para gerar carga e visualizar o pico nos gráficos do Grafana, faça uma requisição para o endpoint de estresse:
Bash

curl "http://localhost:8000/stress?duration=60"

No Grafana, utilize a seguinte query PromQL para visualizar o consumo de CPU:
rate(process_cpu_seconds_total[1m]) * 100
📝 Lições Aprendidas

    Configuração de redes internas no Docker para comunicação entre serviços.

    Exposição de métricas no padrão OpenMetrics.

    Configuração de targets e scrape intervals no Prometheus.

    Criação de dashboards dinâmicos no Grafana.
