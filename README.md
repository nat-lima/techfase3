# Dados Abertos PRF

Este é um projeto de Machine Learning desenvolvido com Flask e Visual Studio Code, que inclui web scraping https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes e autenticação básica.

A saber, O Portal Brasileiro de Dados Abertos é a ferramenta disponibilizada pelo governo para que todos possam encontrar e utilizar os dados e as informações públicas.

## Link video

https://drive.google.com/file/d/1cG5NIg3HIAygibd92G8mwSxrQz7wMYcO/view?usp=sharing

## Arquitetura

![image](https://github.com/user-attachments/assets/c7513ab8-dfd5-45ed-8940-c17c5ee2066b)


## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Web Scraping**: Extrai o csv da página web https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes contendo registro de acidentes de 2024 e 2025.
- **Mineração, análise exploratória e outras análises**: Desenvolvimento utilizando VScode, Notebook Jubyter, Pandas, Firebase Admin, Nupy, matplotlib e seaborn.
- **Cache e Documentação**: Implementa cache para otimização e documentação automática com Swagger.
- **Apresentação dos Dados**: PowerBI (https://app.powerbi.com/groups/me/reports/cd22ec7c-7e34-4af8-a141-ac4fa8a34b8a/434fe304679f8fc8be24?ctid=11dbbfe2-89b8-4549-be10-cec364e59551&experience=power-bi) requer registro de usuário no portal.

## 📁 Estrutura do Projeto

```bash
techfase3/
├── app/
│   ├── __init__.py
│   ├── csv/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── dadosabertosprf.py
│   ├── key/
│   ├── route/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── scrape.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   │   ├── links.py
│   └── config.py
├── 1 Projeto EDA.ipynb
├── 2 Machine Learning Classificacao.ipynb
├── 3 LDA para topic model.ipynb
├── util/
│   └── grid_search.py
├── resultados/
├── requirements.txt
├── README.md
└── run.py
└── scrape_detratan.py
```

- **`app/`**: Diretório principal do aplicativo.
  - **`csv/`**: Após captura dos arquivos apartir do site dados abertos do governo, os arquivos são salvos nessa estrutura.
  - **`data/`**: estrutura para leitura dos dados e persistência em base de dados remota.
  - **`key/`**: key do cloud firestore onde a coleção foi criada. 
  - **`routes/`**: Contém a rota responsável por invocar o processamento dos dados provenientes do site dados abertos.
  - **`utils/`**: Utilitários, como autenticação e links no site.
  - **`config.py`**: Configurações da aplicação Flask.
- **`1 Projeto EDA.ipynb`**: Análise exploratória dos dados.
- **` 2 Machine Learning Classificacao.ipynb`**: Modelo de classificação.
- **`3 LDA para topic model.ipynb`**:  Modelo não supervisionado de modelagem de tópicos
- **`util/`**:
-   - **`grid_search.py`**: Grid Search para o LDA.
- **`dados/`**: Em caso de estouro da quota do firebase, é possível utilizar o csv original do site apartir dessa pasta. 
- **`resultados/`**: Contém o modelo PKL, CSV para o dashboard e Dashboard.
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Documentação do projeto.

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/nat-lima/techfase3
cd techfase3
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

API - Para baixa e persistencia dos dados abertos PRF 
O aplicativo estará disponível em `http://localhost:5000` ou `http://127.0.0.1:5000`
```bash
python run.py
```

Modelos ML - Faz-se necessário executar o notebook abaixo:
```bash
1 Projeto EDA.ipynb
```
### 5. Chave para acesso ao Cloud Firestore
https://drive.google.com/drive/u/0/folders/1xNLDnPaPQGgXunZYPvIJ9tO1uOFNWHIh
Também disponível em: techfase3/app/key

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.

## 🤝 Contribuindo

1. Fork este repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.
