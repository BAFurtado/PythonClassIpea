# Importe todas as funções de dentro de function3.
# Acesse-as com ponto: exemplo function3.soma()
import function3

# Importe somente a função print_sentences do módulo function1
# Acesse usando o apelido ps
from function1 import print_sentences as ps

# Importe da function2 e use pelo nome direto soma()
from function2 import soma
from function5 import area_circle


if __name__ == '__main__':
    ps()
    soma()
    function3.soma(5, 6)
    print(area_circle(5))
