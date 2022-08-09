'''  Leandro Ceron Durau
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de 
entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
 {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de 
entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que 
podem existir em um arquivo de testes para o programa que você irá desenvolver: 

3 
abbaba 
abababb 
bbabbaaab 

Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será 
representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e 
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado 
da validação conforme o formato indicado a seguir: 
abbaba: não pertence.   
A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será 
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída. 
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes 
devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor 
irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de 
testes criado pelo próprio professor
'''


from logging import _FormatStyle
from operator import truediv
from pickle import FALSE
import re


def Reconhecedor(texto):
    caracter = texto[-1]
    if(caracter=='a'):
        if(Analisador(texto)):#-1 caracter
            return True
        return False
    if(caracter=='b'):
        if(Reconhecedor(texto,0)):#-1
            return True 
        return False
    if(caracter=='c'):
        if(Recusador(texto)):#-1
            return True 
        return False
    if(caracter==''):#acabou a string
        return True 
    #Para caracteres fora do  alfabeto
    Recusador(texto)
    return False
        


def Analisador(texto,n_b):
    caracter = texto[-1]
    if(caracter=='b' and n_b==1):
        if(Reconhecedor(texto)):
            return True
        return False
    if(caracter=='b'):
        if(Analisador(texto,1)):
            return True
        return False 
    if(caracter=='a' or caracter=='c'):
        if(Reconhecedor(texto)):
            return True 
        return False 
    if(caracter==''):#acabou a string
        return False 
    #Para caracteres fora do  alfabeto
    Recusador(texto)
    return False
        


def Recusador(texto):
    return False

