#Data: 22/03/2018
#Criador: Bruno Tomas Santos Buzzo
#OBS: Primeiro estudo atrávés de leitura e pesquisa em documentação Flask


from flask import Flask
#importando o Framework
#importanto a instancia da classe Flask para poder utilizar o Framework em questão

app = Flask(__name__) 
#Instanciando a classe Flask e nomeando a como "app"
#Essa instancia recebe uma variavel chamada __name__ é uma variavel especial qu eo interpretador Python cria  quando está executando o arquivo e ele sempre atribui um valor que determina qual tipo de arquivo esta executando
# EX: se é um arquivo principal que está executando ou se é um arquivo secundário
#se for um arquivo secundário ele fará referencia ao módulo em questão, se for o arquivo principal ele vai atribuir o "main" a variavel.


@app.route("/") #Decorator: Uma caracteristica do Python que é composta sempre antes de uma função para aplicar uma função em cima da outra.
#Ele determina a rota da minha pagina (pagina que deve trazer o conteúdo a ser tratado na função abaixo) Neste caso o Index que é representado pelo "/"
def index():
	#A função index é uma pagina que está sendo criada.
	#Então quando eu acessar a rota definida acima na minha aplicação eu tenho que ser mandado aqui para essa pagina "index" e essa pagina precisa retornar alguma coisa no "return"
	return "Hello word!"

if __name__ == "__main__": # OBS: Auto explicativo, se o arquivo que foi atribuito a variavel __name__ for o principal ele vai executar o procedimento que estará identado abaixo...
	#aqui será uma questão de segurança, somente será executado se o que estou tentando executar é o arquivo principal, i.é, o Flask só vai "dar" o Run se o arquivo em questão é o arquivo principal
	app.run()


#Para testar, abra o cmd, vá até o diretório que esta salvo seu arquivo e digite: python app.py para rodar o servidor
#Abra o navegador e digite: localhost:5000 e veja o resultado.
