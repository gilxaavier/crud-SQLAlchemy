from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome="Maxwell", idade=22)
    print(pessoa)
    pessoa.save()
    
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome="Gil Xavier").first()
    print(pessoa.idade)
    
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Gil Xavier").first()
    pessoa.nome = "Gildásio"
    pessoa.save()
    
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Gildásio").first()
    pessoa.delete()

if __name__ ==  "__main__":
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
    