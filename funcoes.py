import io
import os
import sys
from pip._vendor.distlib.compat import raw_input
from prettytable import PrettyTable


# ---------------- Criação do Obejeto ----------------
# Primeiro parametro é a pergunta
# Segundo parametro um vetor onde a primera posição é:
# [0] = Letra [1] = Alternativa
import atributos


class Alternativas:
    def __init__(self, pergunta, vet1, vet2, vet3, vet4):
        '''Garantindo que ela receberá sempre os mesmo parametros

        >>> x = Alternativas('p', ['I','1'],
        ...                  ['II','2'], ['III','3'], ['IV','4'])
        >>> x.__dict__ == {'alternativa':['I. 1', 'II. 2', 'III. 3', 'IV. 4'],
        ...               'letra': ['I', 'II', 'III', 'IV'], 'pergunta': 'p'}
        True

        '''
        self.alternativa = []
        self.letra = []
        self.pergunta = pergunta
        self.alternativa.append('I. ' + vet1[1])
        self.letra.append(vet1[0])
        self.alternativa.append('II. ' + vet2[1])
        self.letra.append(vet2[0])
        self.alternativa.append('III. ' + vet3[1])
        self.letra.append(vet3[0])
        self.alternativa.append('IV. ' + vet4[1])
        self.letra.append(vet4[0])



# ---------------- Função para exibir a pergunta ----------------
def perguntar(obj):
    ''' Testando se a função recebe o parametro correto,
    verificando se está sendo feita a atribuição correta

    >>> x = atributos.contAlternativas
    >>> testaFuncao_Perguntar('1', Alternativas('p', ['I','1'], ['C','2'], ['O','3'], ['A','4']) )
    p
    <BLANKLINE>
    I. 1
    II. 2
    III. 3
    IV. 4
    <BLANKLINE>
    Escolha um das alternativa: "1", "2", "3" ou "4":
    >>> x == [1, 0, 0, 0]
    True

    >>> x = atributos.contAlternativas
    >>> testaFuncao_Perguntar('2', Alternativas('p', ['I','1'], ['C','2'], ['O','3'], ['A','4']) )
    p
    <BLANKLINE>
    I. 1
    II. 2
    III. 3
    IV. 4
    <BLANKLINE>
    Escolha um das alternativa: "1", "2", "3" ou "4":
    >>> x == [1, 1, 0, 0]
    True

    >>> x = atributos.contAlternativas
    >>> testaFuncao_Perguntar('3', Alternativas('p', ['I','1'], ['C','2'], ['O','3'], ['A','4']) )
    p
    <BLANKLINE>
    I. 1
    II. 2
    III. 3
    IV. 4
    <BLANKLINE>
    Escolha um das alternativa: "1", "2", "3" ou "4":
    >>> x == [1, 1, 1, 0]
    True

    >>> x = atributos.contAlternativas
    >>> testaFuncao_Perguntar('4', Alternativas('p', ['I','1'], ['C','2'], ['O','3'], ['A','4']) )
    p
    <BLANKLINE>
    I. 1
    II. 2
    III. 3
    IV. 4
    <BLANKLINE>
    Escolha um das alternativa: "1", "2", "3" ou "4":
    >>> x == [1, 1, 1, 1]
    True


    '''

    global contAlternativas
    print(obj.pergunta + '\n')
    print(obj.alternativa[0])
    print(obj.alternativa[1])
    print(obj.alternativa[2])
    print(obj.alternativa[3] + '\n')
    condicao = True
    while (condicao):
        condicao = False
        try:
            # ------ Pergunta para o usuário qua é a resposta
            res = int(raw_input('Escolha um das alternativa: "1", "2", "3" ou "4":'))
            if res not in range(1, 5):
                print('Opção Inválida!')
                condicao = True
        except ValueError:
            res = print('Informação não númerica!')
            condicao = True
    if obj.letra[res - 1] == 'I':
        atributos.contAlternativas[0] += 1
    elif obj.letra[res - 1] == 'C':
        atributos.contAlternativas[1] += 1
    elif obj.letra[res - 1] == 'O':
        atributos.contAlternativas[2] += 1
    elif obj.letra[res - 1] == 'A':
        atributos.contAlternativas[3] += 1
    os.system("cls")

# ---------------- Função para exibir resultado ----------------

def resultado(res):

    i = str(res[0] * 4)
    c = str(res[1] * 4)
    o = str(res[2] * 4)
    a = str(res[3] * 4)
    #Topico das colunas
    x = PrettyTable(["Emocional (lado direito do cérebro) ",
                     "Racional(lado esquerdo do cérebro) "])

    # Alinha as colunas
    x.align["Emocional (lado direito do cérebro) "] = "l"
    x.align["Racional(lado esquerdo do cérebro) "] = "l"
    # Deixa um espaço entre a borda das colunas e o conteúdo (default)
    x.padding_width = 1
    x.add_row(["        Águia       Gato        ",
                "       Tubarão      Lobo        "])
    x.add_row(["         " + i + "%          " + c + "%       ",
               "         " + a + "%          " + o + "%       "])
    print(x)
    # -------- Exibe o "Compreendendo os resultados ------
    y = PrettyTable(["  ", "ÁGUIA", "GATO", "TUBARÃO", "LOBO"])
    y.padding_width = 2
    y.add_row(['COMPORTAMENTOS',
                        'Fazer diferente Criativo Intuitivo Foco no futuro\n'
                        ' Distraído Curioso Informal/Casual Flexível',
                       'Fazer junto Sensível Relacionamentos Time Tradicionalistas\n '
                       'Contribuição Busca Harmonia Delega autoridade',
                       'Fazer rápido Senso de urgência Ação iniciativa Impulsivo, '
                       'prático Vencer\n desafios Aqui e agora Auto suficiente Não gosta'
                       'de delegar poder',
                       'Fazer certo Detalhista Organizado Estrategista Busca do \n'
                       'conhecimento Pontual Conservador Previsível'])

    y.add_row(['\nPONTOS FORTES',
                       '\nIdealização Provoca mudanças radicais Antecipar o \n'
                       'futuro Criatividade',
                       '\nComunicação Manter comunicação harmoniosa Desenvolver\n'
                       ' e manter a cultura empresarial Comunicação aberta ',
                       '\nAção Fazer que ocorra Parar com burocracia Motivação',
                       '\nOrganização Passado, presente e futuro Consistência,\n'
                       'conformidade e qualidade Lealdade e segurança Regras e\n'
                       ' responsabilidade'])
    y.add_row(['\nPONTOS DE MELHORIA',
                       '\n Idealização Falta de atenção para o aqui e agora \n'
                       'Impaciência e rebeldia Defende',
                       '\n Comunicação Esconder conflitos Felicidade acima dos \n'
                       'resultados Manipulação através dos sentimentos',
                       '\nAção Socialmente um desastre Faz do modo mais fácil \n'
                       'Relacionamento complicado',
                       '\nOrganização Dificuldades de se adaptar ás mudanças \n'
                       'Pode impedir o progresso Detalhista, estruturado e \n'
                       'demasiadamente sistematizado'])
    y.add_row(['\n\nMOTIVAÇÕES',
                       '\n Liberdade de expressão Ausência de controles rígidos\n'
                       'Ambiente de trabalho descentralizado Liberdade para \n'
                       'fazer exceções Oportunidade para delegar tar',
                       '\nSegurança Aceitação social Construir o consenso \n'
                       'Reconhecimento da equipe Supervisão compreensiva \n'
                       'Ambiente harmônico Trabalho em grupo',
                       '\nLiberdade para agir individualmente Controle \n'
                       'das próprias atividades Resolver os problemas do \n'
                       'seu jeito Competição individual Variedade de \n'
                       'atividades Não ter que repetir tarefas.',
                       '\nCerteza, compreensão exata de quais são as \n'
                       'regras Conhecimento específico do trabalho Ausência\n'
                       ' de riscos e erros Ver produto aca '])
    y.add_row(['\nVALORES O QUE MOVE?',
                       '\nCriatividade e Liberdade (inspira idéias).',
                       '\nFelicidade e igualdade (cultura da empresa – pensa nos outros).',
                       '\nResultados.',
                       'Ordem e controle.'])
    print(y)


def testaFuncao_Perguntar(n, objeto):
    #Função recebe como parametro:
    #n = reposta do input
    #objeto = objeto que será usado como parametro na funcao perguntar()
            xx = sys.stdin
            x = io.StringIO(n)
            sys.stdin = x
            perguntar(objeto)
            x.close()
            sys.stdin = xx


if __name__ == "__main__":
    import doctest
    doctest.testmod()