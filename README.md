# Desafio Crawler

O objetivo deste código é criar um crawler que visite o site epocacosmeticos.com.br e salve um arquivo .csv com o nome do produto, o título e a url de cada página de produto encontrada.

Regras:
 
 - Esse arquivo não deve conter entradas duplicadas;
 - Não é permitido usar o sitemap para pegar todas as urls do site; o site deve de fato ser visitado e parseado para se obter as informações.
 - Exceto pelo Scrapy, você pode usar os frameworks e bibliotecas que quiser, desde que a linguagem principal usada seja Python (2.7, 3.x, PyPy... tanto faz).
 
 
# Necessário
 - Python 3
 <!-- - RabbitMq (https://www.rabbitmq.com/) -->
 
# Como Desenvolver

 1. clone o respositório.
 2. crie uma virtualenv com Python 3.5. (https://virtualenv.pypa.io/en/stable/)
 3. Ative o virtualenv.
 4. Instale as dependências.
 5. Instale o projeto
 6. Execute os testes.
 
 ```console
 git clone git@github.com:lffsantos/captura.git
 cd captura
 virtualenv -p python3 .virtualenv
 source .virtualenv/bin/activate
 pip install -r requirements.txt
 py.test
```

# Como Executar:

 - Instalar Requirements e a Aplicação;  
        pip install -r requirements.txt  
        python setup.py install
 
 - Criar  Banco de dados da Aplicação;
		python core/db/database.py
 
 - Rodar Crawler;  
		python core/modules/crawler.py
        
- Rodar o Processor;
        python core/modules/processor.py

- Rodar o Indexer:
        python core/modules/indexer.py

- Utilizando Makefile
	
```console
make run
```

## Módulos (core/modules) 
 
### crawler.py
   - Responsável por capturar os links da url informada.  