# fiap_tech_challenge_fase3
🛫 Análise Preditiva e Clusterização de Atrasos em Voos nos EUA | Projeto da Fase 3 do Tech Challenge - Pós Tech FIAP (Machine Learning Engineering)

---

## 📌 Visão geral
Este repositório contém notebooks e utilitários para **pré-processamento**, **análise exploratória** e **modelagem** de dados de voos (atrasos). Abaixo está a ordem de execução para reproduzir os resultados e entender o fluxo do projeto.

---

## 🚦 Ordem de execução (passo a passo)
1. **Configurar o ambiente** ⚙️
   - Crie um ambiente virtual e instale dependências:
     - Windows PowerShell:
       ```ps1
       python -m venv .venv
       .\.venv\Scripts\activate
       pip install -r requirements.txt
       ```
   - Certifique-se de usar o mesmo kernel/interpreter nos notebooks (o kernel deve conter os pacotes do `requirements.txt`).

2. **Pré-processamento** — `Pre_Processamento.ipynb` 🔧
   - Execute este notebook **primeiro**. Ele carrega os dados brutos em `Data/`, realiza limpeza, transformações e gera os conjuntos de dados prontos para análise e modelagem.
   - Alguns resultados intermediários podem ser salvos (ver células do notebook). Execute todas as células na ordem indicada.
   - O Arquivo é gerado em parquet com o nome "flights_merged.parquet"

3. **Análise exploratória** — `analise_exploratoria.ipynb` 📊
   - Rode este notebook após o pré-processamento para gerar visualizações, estatísticas e insights dos dados limpos.
   - Este notebook depende dos artefatos/resultados produzidos em `Pre_Processamento.ipynb`.
    - O Arquivo é gerado em parquet com o nome "DF_to_model.parquet"

4. **Redução de dimensionalidade** — `Models/pca.ipynb` 📉
   - Use este notebook para aplicar PCA e entender a representatividade das variáveis.

5. **Modelagem / Classificação** — `Models/classificacao.ipynb` 🤖
   - Treine e avalie modelos de classificação (ex.: prever atraso, classes, etc.).
   - Depende de dados pré-processados e de transformações aplicadas no PCA.

6. **Código utilitário** — `utils.py` 🧩
   - Contém funções reutilizáveis usadas nos notebooks (leitura, limpeza, transformação, métricas).

---

## 📂 Estrutura de arquivos (resumo)
- `analise_exploratoria.ipynb` — EDA e visualizações
- `Pre_Processamento.ipynb` — Limpeza e preparação dos dados
- `Models/classificacao.ipynb` — Treinamento e avaliação de modelos
- `Models/pca.ipynb` — Análise de componentes principais
- `utils.py` — Funções utilitárias
- `requirements.txt` — Dependências do projeto
- `Data/` — Dados brutos: `airlines.csv`, `airports.csv`, etc.

---

## 💡 Boas práticas
- Sempre execute os notebooks de cima para baixo (top-to-bottom) para garantir que todas as variáveis e artefatos estejam disponíveis.
- Use um ambiente virtual limpo para evitar incompatibilidades.

---

## 🤝 Integrantes
- Iago Victor
- Jaderson Damasceno
- Luis Rodrigues
- Vitor Santiago

---

**Boa execução!** ✅
