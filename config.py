<<<<<<< HEAD
class Config:
    SECRET_KEY = 'your_secret_key'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Dados Abertos PRF',
        'uiversion': 3,

        "paths": {
                    "/scrape/dadosabertosprf": {
                    "get": {
                        "tags": [
                        "Produção"
                        ],
                        "summary": "Retrieve data from 2025 e 2024 from https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-acidentes (Producao). ",
                        "responses": {
                        "200": {
                            "description": "Successfull",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/scrape/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },
                    "/auth/login": {
                    "post": {
                        "tags": [
                        "Login"
                        ],
    "requestBody": { "required": True, "content": { "application/json": { "schema": { "$ref": "#/components/schemas/LoginRequest" } } } } ,        
    "summary": "HTTP Request for login",
                        "responses": {
                        "200": {
                            "description": "Successful",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/auth/"
                                }
                            }
                            }
                        }
                        }
                        }
                    }
            }
    }

=======
class Config:
    SECRET_KEY = 'your_secret_key'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Embrapa Viti API Service',
        'uiversion': 3,

        "paths": {
                    "/scrape/vitiproducao": {
                    "get": {
                        "tags": [
                        "Produção"
                        ],
                        "summary": "Retrieve all data from http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02 (Producao). The year range available in the web site is processed ",
                        "responses": {
                        "200": {
                            "description": "Successfull",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/scrape/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },  
                    "/scrape/vitiprocessamento": {
                    "get": {
                        "tags": [
                        "Processamento"
                        ],
                        "summary": "Retrieve all data from http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03 (Processamento). The year range available in the web site is processed ",
                        "responses": {
                        "200": {
                            "description": "Successfull",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/scrape/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },     
                    "/scrape/viticomercializacao": {
                    "get": {
                        "tags": [
                        "Comercialização"
                        ],
                        "summary": "Retrieve all data from http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04 (Comercialização). The year range available in the web site is processed ",
                        "responses": {
                        "200": {
                            "description": "Successfull",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/scrape/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },  
                    "/scrape/vitiimportacao": {
                    "get": {
                        "tags": [
                        "Importacao"
                        ],
                        "summary": "Retrieve all data from http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05 (Importação). The year range available in the web site is processed ",
                        "responses": {
                        "200": {
                            "description": "Successfull",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/scrape/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },   
                  "/scrape/vitiexportacao": {
                    "get": {
                        "tags": [
                        "Exportação"
                        ],
                        "summary": "Retrieve all data from http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06 (Exportação). The year range available in the web site is processed ",
                        "responses": {
                        "200": {
                            "description": "Successfull",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/components/schemas/vitiexportacao/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },   
                    "/auth/login": {
                    "post": {
                        "tags": [
                        "Login"
                        ],
    "requestBody": { "required": True, "content": { "application/json": { "schema": { "$ref": "#/components/schemas/LoginRequest" } } } } ,        
    "summary": "HTTP Request for login",
                        "responses": {
                        "200": {
                            "description": "Successful",
                            "content": {
                            "application/json": {
                                "schema": {
                                "$ref": "#/auth/"
                                }
                            }
                            }
                        }
                        }
                        }
                    },
            "components": 
            { "schemas": 
                { "vitiexportacao": 
                    { "type": "object", 
                        "properties": 
                        { "ano": { "type": "string" }, 
                            "paises": { "type": "string" },
                            "quantidade": { "type": "string" },
                            "valor": { "type": "string" },
                            "unidade_medida": { "type": "string" }                                
                        } 
                        },
                    
               "LoginRequest": { "type": "object", "properties": { "username": { "type": "string", "example": "user@example.com" }, "password": { "type": "string", "example": "password123" } }, "required": ["username", "password"] 
                    }
                }                                                    
                }
            }
    }

>>>>>>> 5d8c14d8b292a4a718c24f2f8749b4d5dc2161f8
