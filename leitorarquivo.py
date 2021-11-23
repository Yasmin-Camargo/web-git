class LeitorArquivo:
    def __init__ (self, nomeArq):
        self.arq = open(nomeArq, "r")
        self.valores = [float(x) for x in self.arq.readline().split()]
        
    def getValores(self):
        return self.valores
    
if __name__ == '__main__':
    leitor = LeitorArquivo("data.txt")
    valores =  leitor.getValores()
    print(valores)