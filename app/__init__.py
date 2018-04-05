#Data: 22/03/2018
#Criador: Bruno Tomas Santos Buzzo
#OBS: Primeiro estudo atrávés de leitura e pesquisa em documentação Flask


from flask import Flask
#importando o Framework
#importanto a instancia da classe Flask para poder utilizar o Framework em questão

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config') 
#Instanciando a classe Flask e nomeando a como "app"
#Essa instancia recebe uma variavel chamada __name__ é uma variavel especial qu eo interpretador Python cria  quando está executando o arquivo e ele sempre atribui um valor que determina qual tipo de arquivo esta executando
# EX: se é um arquivo principal que está executando ou se é um arquivo secundário
#se for um arquivo secundário ele fará referencia ao módulo em questão, se for o arquivo principal ele vai atribuir o "main" a variavel.

db= SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)




#Para testar, abra o cmd, vá até o diretório que esta salvo seu arquivo e digite: python app.py para rodar o servidor
#Abra o navegador e digite: localhost:5000 e veja o resultado.

from app.controllers import default