# geru-chalenge

*Para rodar o projeto em um docker:*

Em linux: com o terminal aberto no diretório da aplicação digite:
'''
sudo docker build -t test-geru .
'''

Com o término do build digite:
'''
sudo docker run -p 8080:8080 test-geru
'''

Após isso é só acessar a porta 8080 de seu localhost.

*Para rodar o projeto usando uma env em python:*
pré-requisitos:
* Ter o Python3 instalado;
* Ter o pip do python3 instalado;

Caso você não tenha a virtualenv instalada, basta inserir no terminal:

'''
pip3 install virtualenv
'''

Abra o terminal na raiz do diretório e crie uma env:

'''
virtualenv -p python3 env
'''

Ative sua env:

linux:
'''
source env/bin/activate
'''

windows:
'''
env\Scripts\activate
'''

Com sua env ativa, você deve instalar as dependências:
'''
pip install -r requirements.txt
'''

Agora o sistema está configurado para executar. Para executar no terminal:
'''
python app.py
'''

Neste caso você precisará sempre ativar a sua env para rodar a aplicação, pois nela conterá todas as dependências necessárias para sua execução. Com uma env você terá um ambiente para rodar sua aplicação sem instalar as bibliotecas de maneira solta em sua máquina. Obs: Dentro de uma env não é necessário dizer a versão do python que está sendo usada já que ela foi inicializada com uma versão base.
