from models import *

# def get_denuncia():


#     # pega denuncia do site

#     return

def post_denuncia(endereco, pessoa, descricao):

    
    Denuncia.create(fk_endereco = endereco,fk_pessoa = pessoa, descricao = descricao )

    return


# def get_pessoa(cpf):

#     Pessoa.select().where(Pessoa.cpf == cpf)

#     return

# def post_pessoa():
#     return

# def cadastrar_usuario(cpf,email,senha):

#     return

# def get_sensor(id):
#     return

# def post_sensor():
#     return

# def get_all_leituras_endereco():



#     return


# def get_leitura(id):
#     return

# def post_leitura():
#     return

# def get_denuncia(id):
#     return

