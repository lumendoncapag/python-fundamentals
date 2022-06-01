class Monstro:
    def __init__(self,nome,poder):
        self.nome = nome
        self.poder = poder


class Dragao(Monstro):
    def __init__(self,nome,poder,asas,arma):
        super().__init__(nome,poder)
        self.asas = asas
        self.arma = arma

    def get_arma(self):
        print(f"A arma que o {self.nome} é : {self.arma}") 
banguela = Dragao("banguela","soltar fogo","asas","nenhuma")
banguela.get_arma()
class Orc(Monstro):
    def __init__(self,nome,poder,arma,magia):
        super().__init__(self,nome,poder)
        self.arma = "machado"
        self.magia = "Nenhuma"

class Vampiro(Monstro):
    def __init__(self,nome,poder,arma,magia):
        super().__init__(self,nome,poder)
        self.arma = "Nenhuma"
        self.magia = "Imortalidade"

class Troll(Monstro):
    def __init__(self,nome,poder,arma,magia):
        super().__init__(self,nome,poder)
        self.arma = "Cacetete"
        self.magia = "Poder de gelo"
