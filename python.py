class NPC:
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print(self.nome)
        print(self.time)
        print(self.forca)
        print(self.municao)
        print(self.vivo)
        print(self.energia)
        print('--'*20)

class soldado(NPC):
    def __init__(self,nome,time):
        self.forca=200
        self.municao=200
        super().__init__(nome,time,self.forca,self.municao)
    def info(self):
        super().info()

class guarda(NPC):
    def __init__(self,nome,time):
        self.forca=200
        self.municao = 100
        super().__init__(nome,time,self.forca,self.municao)
    def info(self):
        super().info()

s1=soldado('andre1',2)
g1=guarda('valdisney','10')

g1.info()
s1.info()

   
