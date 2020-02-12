from funcoes import Alternativas
# ------- Contador de cada alternativa -------
contAlternativas = [0, 0, 0, 0]

# ------- Criando os objetos -------
prgt1 = Alternativas('1. Eu sou... ',
                     ['I', 'Idealista, criativo e visionário'],
                     ['C', 'Divertido, espiritual e benéfico'],
                     ['O', 'Confiável, meticuloso e previsíve'],
                     ['A', 'Focado, determinado e persistente'])
prgt2 = Alternativas('2. Eu gosto de... ',
                     ['A', 'Ser piloto'],
                     ['C', 'Conversar com os passageiros'],
                     ['O', 'Planejar a viagem'],
                     ['I', 'Explorar novas rotas'])
prgt3 = Alternativas('3. Se você quiser se dar bem comigo... ',
                     ['I', 'Me dê liberdade'],
                     ['O', 'Me deixe saber sua expectativa'],
                     ['A', 'Lidere, siga ou saia do caminho'],
                     ['C', 'Seja amigável, carinhoso e compreensivo'])
prgt4 = Alternativas('4. Para conseguir obter bons resultados é preciso...  ',
                     ['I', 'Ter incertezas'],
                     ['O', 'Controlar o essencial'],
                     ['C', 'Diversão e celebração'],
                     ['A', 'Planejar e obter recursos'])
prgt5 = Alternativas('5. Eu me divirto quando... ',
                     ['A', 'Me dê liberdade'],
                     ['I', 'Me deixe saber sua expectativa'],
                     ['C', 'Lidere, siga ou saia do caminho'],
                     ['O', 'Seja amigável, carinhoso e compreensivo'])
prgt6 = Alternativas('6. Eu penso que...  ',
                     ['C', 'Unidos venceremos, divididos perderemos'],
                     ['A', 'O ataque é melhor que a defesa'],
                     ['I', 'É bom ser manso, mas andar com um porrete'],
                     ['O', 'Um homem prevenido vale por dois'])
prgt7 = Alternativas('7. Minha preocupação é... ',
                     ['I', 'Gerar a ideia globa'],
                     ['C', 'Fazer com que as pessoas gostem'],
                     ['O', 'Fazer com que funcione'],
                     ['A', 'Fazer com que aconteça'])
prgt8 = Alternativas('8. Eu prefiro... ',
                     ['I', 'Perguntas a respostas '],
                     ['O', 'Ter todos os detalhes '],
                     ['A', 'Vantagens a meu favor'],
                     ['C', 'Que todos tenham a chance de ser ouvidos'])
prgt9 = Alternativas('9. Eu gosto de... ',
                     ['A', 'Fazer progresso'],
                     ['C', 'Construir memórias'],
                     ['O', 'Fazer sentido'],
                     ['I', 'Tornar as pessoas confortáveis'])
prgt10 = Alternativas('10. Eu gosto de chegar... ',
                     ['A', 'Na frente'],
                     ['C', 'Junto'],
                     ['O', 'Na hora'],
                     ['I', 'Em outro lugar'])
prgt11 = Alternativas('11. Um ótimo dia para mim é quando...  ',
                     ['A', 'Consigo fazer muitas coisas'],
                     ['C', 'Me divirto com meus amigos'],
                     ['O', 'Tudo segue conforme planejado'],
                     ['I', 'Desfruto de coisas novas e estimulantes'])
prgt12 = Alternativas('12. Eu vejo a morte como... ',
                     ['I', 'Uma grande aventura misteriosa'],
                     ['C', 'Oportunidade de rever os falecidos'],
                     ['O', 'Um modo de receber recompensas'],
                     ['A', 'Algo que sempre chega muito cedo'])
prgt13 = Alternativas('13. Minha filosofia de vida é... ',
                     ['A', 'Há ganhadores e perdedores, e eu acredito ser um ganhador'],
                     ['C', 'Para eu ganhar, ninguém precisa perder'],
                     ['O', 'Para ganhar é preciso seguir as regras'],
                     ['I', 'Para ganhar, é necessário inventar novas regras'])
prgt14 = Alternativas('14. Eu sempre gostei de... ',
                     ['I', 'Explorar'],
                     ['O', 'Evitar surpresas'],
                     ['A', 'Focalizar a meta'],
                     ['C', 'Realizar uma abordagem natural'])
prgt15 = Alternativas('15. Eu gosto de mudanças se... ',
                     ['A', 'Me der uma vantagem competitiva'],
                     ['C', 'For divertido e puder ser compartilhado'],
                     ['I', 'Me der mais liberdade e variedade'],
                     ['O', 'Melhorar ou me der mais controle'])
prgt16 = Alternativas('16. Não existe nada de errado em... ',
                     ['A', 'Se colocar na frente'],
                     ['C', 'Colocar os outros na frente'],
                     ['I', 'Mudar de ideia'],
                     ['O', 'Ser consistente'])
prgt17 = Alternativas('17. Eu gosto de buscar conselhos de... ',
                     ['A', 'Pessoas bem-sucedidas'],
                     ['C', 'Anciões e conselheiros'],
                     ['O', 'Autoridades no assunto'],
                     ['I', 'Lugares, os mais estranhos'])
prgt18 = Alternativas('18. Meu lema é... ',
                     ['I', 'Fazer o que precisa ser feito'],
                     ['O', 'Fazer bem feito'],
                     ['C', 'Fazer junto com o grupo'],
                     ['A', 'Simplesmente fazer'])
prgt19 = Alternativas('19. Eu gosto de... ',
                     ['I', 'Complexidade, mesmo se confuso'],
                     ['O', 'Ordem e sistematização'],
                     ['C', 'Calor humano e animação'],
                     ['A', 'Coisas claras e simples'])
prgt20 = Alternativas('20. Tempo para mim é... ',
                     ['A', 'Algo que detesto desperdiçar'],
                     ['C', 'Um grande ciclo'],
                     ['O', 'Uma flecha que leva ao inevitável'],
                     ['I', 'Irrelevante'])
prgt21 = Alternativas('21. Se eu fosse bilionário... ',
                     ['C', 'Faria doações para entidade'],
                     ['O', 'Criaria uma poupança avantajada'],
                     ['I', 'Faria o que desse na cabeça'],
                     ['A', 'Exibiria bastante com algumas pessoas '])
prgt22 = Alternativas('22. Eu acredito que... ',
                     ['A', 'O destino é mais importante que a jornada'],
                     ['C', 'A jornada é mais importante que o destino'],
                     ['O', 'Um centavo economizado é um centavo ganho'],
                     ['I', 'Bastam um navio e uma estrela para navegar'])
prgt23 = Alternativas('23. Eu acredito também que... ',
                     ['A', 'Aquele que hesita está perdido'],
                     ['O', 'De grão em grão a galinha enche o papo'],
                     ['C', 'O que vai, volta'],
                     ['I', 'Um sorriso ou uma careta é o mesmo para quem é cego'])
prgt24 = Alternativas('24. Eu acredito ainda que... ',
                     ['O', 'É melhor prudência do que arrependimento '],
                     ['I', 'A autoridade deve ser desafiada'],
                     ['A', 'Ganhar é fundamental'],
                     ['C', 'O coletivo é mais importante do que o individua'])
prgt25 = Alternativas('25. Eu penso que... ',
                     ['I', 'Não é fácil ficar encurralado'],
                     ['O', 'É preferível olhar, antes de pular'],
                     ['C', 'Duas cabeças pensam melhor que do que uma'],
                     ['A', 'Se você não tem condições de competir, não compita'])