# Dados Abertos PRF

Este é um projeto de Machine Learning desenvolvido com Flask e Visual Studio Code, que inclui web scraping https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes e autenticação básica.

A saber, O Portal Brasileiro de Dados Abertos é a ferramenta disponibilizada pelo governo para que todos possam encontrar e utilizar os dados e as informações públicas.

## Link video



## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Web Scraping**: Extrai o csv da página web https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes contendo registro de acidentes de 2024 e 2025.
- **Dados Abertos**: Portal do Governo para exposição de dados dos mais diversos segmentos relacionados a gestão pública.
- **Cache e Documentação**: Implementa cache para otimização e documentação automática com Swagger.

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

```bash
python run.py
```

O aplicativo estará disponível em `http://localhost:5000` ou `http://127.0.0.1:5000`

Acesse a aplicação em `http://localhost:5000`.

### 5. Arquitetura




## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.

## 🤝 Contribuindo

1. Fork este repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.
