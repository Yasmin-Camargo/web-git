class LeitorArquivo:
    def __init__ (self, nomeArq):
        self.arq = open(nomeArq, "r")
        self.valores = []
        for linha in self.arq.readlines():
            lista = [float(x) for x in linha.split()]
            self.valores.append(lista)
        
    def getValores(self):
        return self.valores
    
if __name__ == '__main__':
    leitor = LeitorArquivo("data.txt")
    valores =  leitor.getValores()
    print(valores)