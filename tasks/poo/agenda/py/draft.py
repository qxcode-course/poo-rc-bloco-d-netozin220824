class Telefone:
    def __init__(self, id: str, numero: str):
        self.__id: str = id
        self.__numero: str = numero

    def isValid(self):
        permitidos = "013456789()."
        return all(ch in permitidos for ch in self.__numero)

    def getId(self):
        return self.__id

    def getNumero(self):
        return self.__numero
    
    def __str__(self):
        return f"{self.__id}:{self.__numero}"
    
class Contato:
    def __init__(self, nome: str):
        self.__nome: str = nome
        self.__telefones: list = []
        self.__favorited: bool = False

    def addTelefone(self, id: str, numero: str):
        tel = Telefone(id, numero)
        if tel.isValid():
            self.__telefones.append(tel)
            return
        print("fail: número inválido")

    def rmTelefone(self, index: int):
        try:
            self.__telefones.pop(index)
        except:
            print("fail: índice inválido")
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: indice invalido")

    def toggleFavorited(self):
        self.__favorited = not self.__favorited

    def getTelefones(self):
        return self.__telefones
    def __str__(self):
        frag = "@" if self.__favorited else "-"
        return f"{frag} {self.__nome} [" + ", ".join(str(e) for e in self.__telefones)+"]"

    def isFavorited(self):
        return self.__favorited
    def getName(self):
        return self.__nome
    def getTelefones(self):
        return self.__telefones
    def setNome(self, nome: str):
        self.__nome = nome
class Agenda:
    def __init__(self):
        self.__contatos={}
    def addContato(self,nome:str,telefones:list):
        if nome not in self.__contatos:
            self.__contatos[nome] = Contato(nome)
            
        contato = self.__contatos[nome]

        for id_, num in telefones:
            contato.addTelefone(id_, num)
    def rmContato(self,nome:str):
        if nome in self.__contatos:
            del self.__contatos[nome]
        else:
            print("fail: contato nao existe")
    def favorite(self, name: str):
        if nome in self.__contatos:
            self.__contatos[nome].toggleFavorited()
        else:
            print("fail: contato nao existe")
def main():
    agenda = Agenda()
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(contato)

        elif args[0] == "init":
            contato = Contato(args[1])

        elif args[0] == "add":
            contato.addTelefone(args[1], args[2])

        elif args[0] == "rm":
            contato.rmTelefone(int(args[1]))

        elif args[0] == "tfav":
            contato.toggleFavorited()
        else:
            print("fail:comando invalido")
main()