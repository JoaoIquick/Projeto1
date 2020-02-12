import sys
import unittest
import io
import atributos
from funcoes import perguntar, Alternativas


# ----- Garantindo que a função não será alterada
class Test_Funcao(unittest.TestCase):

    def test_Alternativas(self):
        class Aux:
            def __init__(self):
                self.alternativa = ['I. 1', 'II. 2', 'III. 3', 'IV. 4']
                self.letra = ['I', 'II', 'III', 'IV']
                self.pergunta = 'p'
        obj = Aux()
        obj2 = Alternativas('p', ['I','1'], ['II','2'], ['III','3'], ['IV','4'])
        self.assertEqual(obj2.__dict__, obj.__dict__,
                         'Função "Perguntas" foi alterada')
    # Testando função "perguntar"
    # Primeiro verificando se o objeto como parametro é o desejado

    def test_Pergunta(self):
        boolean = True
        
        def testaFuncao(n, objeto):
            xx = sys.stdin
            x = io.StringIO(n)
            sys.stdin = x
            perguntar(objeto)
            x.close()
            sys.stdin = xx

        try:
            obj2 = Alternativas('p', ['I','1'], ['C','2'], ['O','3'], ['A','4'])
            for c in range(1,5):
                testaFuncao(str(c), obj2)
        except:
            boolean = False
        self.assertTrue(boolean, 'teste')

    def test_Pergunta2(self):
        def testaFuncao_Perguntar(n, objeto):
            xx = sys.stdin
            x = io.StringIO(n)
            sys.stdin = x
            perguntar(objeto)
            x.close()
            sys.stdin = xx

        #Verificando se a atribuição está correta
        atributos.contAlternativas = [0, 0, 0, 0]
        testaFuncao_Perguntar('1', Alternativas('p', ['I', '1'], ['C', '2'], ['O', '3'], ['A', '4']))
        x = atributos.contAlternativas
        print(x)
        if x == [1, 0, 0, 0]:
            testaFuncao_Perguntar('2', Alternativas('p', ['I', '1'], ['C', '2'], ['O', '3'], ['A', '4']))
            x = atributos.contAlternativas
            print(x)
            if x == [1, 1, 0, 0]:
                testaFuncao_Perguntar('3', Alternativas('p', ['I', '1'], ['C', '2'], ['O', '3'], ['A', '4']))
                x = atributos.contAlternativas
                print(x)
                if x == [1, 1, 1, 0]:
                    testaFuncao_Perguntar('4', Alternativas('p', ['I', '1'], ['C', '2'], ['O', '3'], ['A', '4']))
                    x = atributos.contAlternativas
                    print(x)
                    if x == [1, 1, 1, 1]:
                        boolean = True
                        print(x)
                        print('True')
                    else:
                        boolean = False
                        print('False 1')
                else:
                    boolean = False
                    print('False 2')
            else:
                boolean = False
                print('False 3')
        else:
            boolean = False
            print('False 4')

        self.assertTrue(boolean, 'erro')






if __name__ == '__main__':
    unittest.main()

