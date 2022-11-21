import json,os


def create_database (nome_aquivo):
  '''nome_aquivo => nome do aquivo que sera salvo
    decrição=> cria um aquivo na mesma pasta em que o scrip
  '''
    #criada aquivo .json
    loading=os.getcwd()
    start={
    "oi": "ola",
    "Oi": "oi",
    "Quem E?": "quem e?",
    "Eu Quem": "eu quem"} #base de dados inicial
    for file in os.listdir(loading):
        if file == f'{nome_aquivo}.json':
            return f'{nome_aquivo}.json'
        #verifica se a um aquivo com o nome caso nao cria com uma base da variavel start
    a=open(nome_aquivo+'.json','w')
    a.close()
    with open(f'{nome_aquivo}.json','w') as lfile:
        json.dump(start,lfile)
        print(f'aquivo {nome_aquivo}.json foi criado') 
        return f'{nome_aquivo}.json'
     

def database_joson(chave,valor,database='database'):
    with open(f'{database}.json','r') as  databaseLoad:
        aquivoload=json.load(databaseLoad)#carrega o que esta salvo na base de dados ecoloca em uma variavel /dicionario
        aquivoload[chave]=valor# salva chave e valor informado em uma variavel
        with open(f'{database}.json','w') as  databasesave:
            json.dump(aquivoload,databasesave,indent=4)

def load ():
  #carrega os dados do aquivo e tranforma em um dicionario
    a=create_database('database')
    with open(a,'r') as file:
        dir=json.load(file)
    return dir


def chat():
    os.system('cls')
    dir=load()
    while True:
        chat=input('diga algo=>')
        if chat in dir :
            print(f'REPOSTA:{dir[chat]}')
            chat=input('.........=> ')
        else:
            autosave=input(f'o que devo responder a "{chat}" ??')
            dir[chat]=str(autosave)
            database_joson(dir[chat],autosave)
            chat=input(f'=>{autosave}...?   \n ')
     
        if chat =='sair':
            break
chat()
