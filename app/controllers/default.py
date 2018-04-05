from app import app

@app.route("/index")
@app.route("/") #Decorator: Uma caracteristica do Python que é composta sempre antes de uma função para aplicar uma função em cima da outra.
#Ele determina a rota da minha pagina (pagina que deve trazer o conteúdo a ser tratado na função abaixo) Neste caso o Index que é representado pelo "/"
def index():
	#A função index é uma pagina que está sendo criada.
	#Então quando eu acessar a rota definida acima na minha aplicação eu tenho que ser mandado aqui para essa pagina "index" e essa pagina precisa retornar alguma coisa no "return"
	return "Hello word!"



@app.route("/test/<name>")
@app.route("/test/", defaults={'name': None})
def test(name):
	if name:
		return "Ola, %s" % name
	else:
		return "Ola, usuário!"	