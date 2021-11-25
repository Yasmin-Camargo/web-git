from leitorarquivo import LeitorArquivo

import numpy as np
import matplotlib.pyplot as plt

def main():
    leitor = LeitorArquivo("data.txt")
    valores = leitor.getValores()
    print(valores)
    
    plt.subplot(1, 2, 1)
    
    plt.xlabel('Amostragem')
    plt.ylabel('Valores de entrada')
    
    for i in range(len(valores)):
        plt.plot(valores[i], label='Série '+ str(i+1))
        
    plt.title('Gráfico de linhas')
    plt.legend(loc='upper left')
    
    plt.subplot(1, 2, 2)
    medias = leitor.calculoMedias()
    xvalues = np.arange(1, len(medias) + 1)
    plt.bar(xvalues, medias)
    plt.xticks(xvalues, ['Séries ' + str(x) for x in xvalues])
    plt.title('Média das séries')
    
    plt.show()
    
main()