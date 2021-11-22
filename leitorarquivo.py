class LeitorArquivo:
    def _init_ (self, nomeArq):
        self.arq = open(nomeArq, "r")
        self.valores = [float(x) for x in self.arq.readline().split()]
        
    def getValores(self):
        return self.valores
    
if nomeArq == '_main_':
    leitor = LeitorArquivo("data.txt")
    valores =  leitor.getValores()
    print(valores)