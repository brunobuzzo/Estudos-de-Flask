from app import manager


if __name__ == "__main__": # OBS: Auto explicativo, se o arquivo que foi atribuito a variavel __name__ for o principal ele vai executar o procedimento que estará identado abaixo...
	#aqui será uma questão de segurança, somente será executado se o que estou tentando executar é o arquivo principal, i.é, o Flask só vai "dar" o Run se o arquivo em questão é o arquivo principal
	manager.run()