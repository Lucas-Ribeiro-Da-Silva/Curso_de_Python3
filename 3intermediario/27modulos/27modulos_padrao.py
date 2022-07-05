"""
https://docs.python.org/3/py-modindex.html

módulos são arquivos .py (que contém código em python) e servem para expandir as funcionalidades padrão da linguagem

Os seguintes itens estão entre os mais importantes:
time;
sys;
os;
math;
random;
pickle;
urllib;
re;
cgi;
socket.
"""

import sys #importando o módulo completo
print(sys.platform) #em qual plataforma o programa está sendo executado

from sys import platform #importando uma função especifica do módulo
print(platform)

from sys import platform as so #renomeando módulos temporariamente
print(so)

import random
print(random.randint(0, 10)) #aleatório entre
for i in range(10):
    print(random.randint(0,10))

from random import * #importa o módulo inteiro

"""
se eu importar um módulo, e receber a mensagem indicando de que este 
não existe na biblioteca, basta ir ao terminal e digitar pip install (nome do módulo)

ou então fazer o mesmo pela interface gráfica
"""


"""
criando seus módulos

https://docs.python.org/3/tutorial/modules.html
"""



"""
criando pacotes

https://docs.python.org/3/tutorial/modules.html
"""