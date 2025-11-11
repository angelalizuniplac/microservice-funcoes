# Execução dos serviços locais. 


## Requisitos: 

1. Baixe a imagem do RabbitMQ para rodar em docker:

 ```docker run -d --restart=always --hostname rabbitmq --name rabbitmq -p 8080:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:4.1-management-alpine```

# Ambiente virtual 

1. Criar um ambiente virtual para isolar o projeto:

    ```python -m venv venv```

2. Ativar o ambiente:

    ```venv\Scripts\activate```

3. Instalar a biblioteca Nameko e outras necessárias: 

    ```python -m pip install --upgrade pip setuptools```
    ```pip install nameko```

4. Atualize o arquivo de requeriments

 ```pip freeze > requirements.txt```


# Execução do serviço de Funções

A execução precisa ser realizada através do Nameko

1. Executar através do Nameko: 

 ```nameko run ServiceFuncoes --config config.yaml```

# Execução do serviço de funções
A execução precisa ser realizada através do Nameko

1. Executar através do Nameko: 

 ```nameko run ServiceFuncoes --config config.yaml```

# Testes

1. Em um novo terminal, execute o comando abaixo para abrir um shell nameko (não esqueça do venv):

 ```nameko shell --config config.yaml```

2. No mesmo terminal, para fazer chamadas rcp e testar o serviço execute um por vez:

```
>>> n.rpc.service_funcoes.ValidaEmail(event={'email': 'abc@123'})
>>> n.rpc.service_funcoes.ValidaEmail(event={'email': 'abc@123.com'})
>>> n.rpc.service_funcoes.ValidaEmail(event={'email': 'abc123.com'})
>>> n.rpc.service_funcoes.ValidaEmail(event={'email': 'abc@123.net'})
>>> n.rpc.service_funcoes.ValidaEmail(event={'email': 'abc@123.'})
```
