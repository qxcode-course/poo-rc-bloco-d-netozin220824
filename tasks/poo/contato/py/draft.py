class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    def isValid(self):
        em = "013456789()."
        return all(e in em for e in self.__number)

    def getId(self):
        return self.__id

    def getNumber(self):
        return self.__number
    
    def __str__(self):
        return f"{self.__id}:{self.__number}"

class Contato:
    def __init__(self, nome: str):
        self.__nome: str = nome
        self.__fone: list = []
        self.__favorited: bool = False

    def addfone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fone.append(fone)
            return
        print("fail: invalid number")

    def rmFone(self, index: int):
        try:
            self.__fone.pop(index)
        except:
            print("fail: index invalido")

    def toggleFavorited(self):
        self.__favorited = not self.__favorited

    def getFones(self):
        return self.__fone
    def __str__(self):
        frag = "@" if self.__favorited else "-"
        return f"{frag} {self.__nome} [" + ", ".join(str(e) for e in self.__fone)+"]"

    def isFavorited(self):
        return self.__favorited

def main():
    contato = Contato("")

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(contato)


    
