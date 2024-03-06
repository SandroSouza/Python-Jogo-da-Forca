import random

class No:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista_tentativa:
    def __init__(self):
        self.head = None
    
    # adiciona uma letra pra lista
    def append(self, letra):
        novo_no = No(letra)

        if self.head == None:
            self.head = novo_no
            return
        
        atual_no = self.head

        while atual_no.next:
            atual_no = atual_no.next

        atual_no.next = novo_no
        return 
    
    #limpa a lista
    def clear(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node
        self.head = None
    
    # mostra a lista
    def display(self):
        conteudo = self.head
        letras = " "
        if conteudo is None:
            print("\n")
        
        while conteudo:
            
            letras += conteudo.data
            conteudo = conteudo.next
            
        return letras

class Lista:
    def __init__(self):
        self.head = None

    # adiciona uma palavra pra lista
    def append(self):
        palavra = input("escreva uma palavra para adicionar na forca:")
        novo_no = No(palavra)

        if self.head == None:
            self.head = novo_no
            return
        
        atual_no = self.head

        while atual_no.next:
            atual_no = atual_no.next

        atual_no.next = novo_no
        return

    # trasforma a lista encadeada em lista normal pro python
    def to_list(self):
        no_data = []
        atual_no = self.head

        while atual_no:
            no_data.append(atual_no.data)
            atual_no = atual_no.next
        return no_data

    #função para limpar a lista
    def clear(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node
        self.head = None

    #função do  jogo
    def play(self, tipo, d):
        palavras = tipo
        sorteio = random.choice(palavras)
        palavra = sorteio.replace('\n', '')

        qtd = len(palavra)


        letras =[]
        chances = d
        ganhou = False
            

        while True:
            #------------------if para mostar o desenho da forca
            if d == 5:
                if chances == 5:
                    print("|-------------|")
                    print("|             |")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                elif chances == 4:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                elif chances == 3:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|            <|")
                    print("|              ")
                    print("|              ")
                elif chances == 2:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|            <|>")
                    print("|              ")
                    print("|              ")
                elif chances == 1:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|            <|>")
                    print("|            / ")
                    print("|              ")
            elif d == 4:
                if chances == 4:
                    print("|-------------|")
                    print("|             |")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                elif chances == 3:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                elif chances == 2:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|            <|>")
                    print("|              ")
                    print("|              ")
                elif chances == 1:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|            <|>")
                    print("|            / ")
                    print("|              ")
            elif d == 3:
                if chances == 3:
                    print("|-------------|")
                    print("|             |")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                elif chances == 2:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|              ")
                    print("|              ")
                    print("|              ")
                elif chances == 1:
                    print("|-------------|")
                    print("|             |")
                    print("|             O")
                    print("|            <|>")
                    print("|              ")
                    print("|              ")

            for letra in palavra:
                
                if letra.lower() in letras:
                    print(letra, end=" ")
                else:
                    print("_", end=" ")

            #-----------------------------------------------------------------
            print(f"\nA palavra tem {qtd} letras")
            
            #------------------------mostra letras usadas---------------------
            mostrar = lt.display()
            print("\n""letras usadas: \n" + mostrar)

            print(f"Você tem {chances} chances")
            tentativa = input("Escolha uma letra para adivinhar: ")
            lt.append(tentativa)
            letras.append(tentativa.lower()) 
            if tentativa.lower() not in palavra.lower():
                chances -= 1
            
            
            #-------------------------codigos de definicao dos status do jogo---------------------
            ganhou = True
            for letra in palavra:
                if letra.lower() not in letras:
                    ganhou = False
            
            if chances == 0 or ganhou:
                break
        #-----------------if para conferir o status--------------------        
        if ganhou:
            print()
            print("|-------------------------------------------------|")
            print(f"|Parabéns, você ganhou. A palavra era: {palavra} |")
            print("|-------------------------------------------------|")
            print()
            jogo.limpar()

        else:
            print()
            print("|-------------|")
            print("|             |")
            print("|             O")
            print("|            <|>")
            print("|            / ` ")
            print("|              ")
            print("|-----------------------------------------------|")
            print(f"Você perdeu! A palavra era: {palavra}          |")
            print("|-----------------------------------------------|")
            print()
            jogo.limpar()

    #função que limpa todas as listas para poder jogar denovo
    def limpar(self):
        lt.clear()
        jogo.clear()
        jogo.replay()

    #função para definir a dificuldade
    def dificuldade(self, palavra):
        print("|--------------------------------------|")
        print("|        Escolha uma Dificuldade       |")
        print("|                                      |")
        print("|             1 - Fácil                |")
        print("|             2 - Médio                |")
        print("|             3 - Dificil              |")
        print("|                                      |")
        print("|--------------------------------------|")
        d = input("Digite: ")
        match d:
            case "1":
                print("\n" * 130)
                jogo.play(palavra, 5)
            case "2":
                print("\n" * 130)
                jogo.play(palavra, 4)
            case "3":
                print("\n" * 130)
                jogo.play(palavra, 3)

    #função para tratar os arquivos da seleção de categoria
    def generos(self, g):
        match g:
            case "1":
                with open("Linguagens.txt", "r") as arquivo:
                    texto = arquivo.readlines()
                    jogo.dificuldade(texto)
            case "2":
                with open("Eletronicos.txt", "r") as arquivo:
                    texto = arquivo.readlines()
                    jogo.dificuldade(texto)
            case "3":
                with open("Pecas.txt", "r") as arquivo:
                    texto = arquivo.readlines()
                    jogo.dificuldade(texto)

    #função para a seleção de categoria
    def opcao(self, o):
        match o:
            case "1":
                print("|--------------------------------------|")
                print("|         Escolha uma Categoria        |")
                print("|                                      |")
                print("|     1 - Lingugem de programação      |")
                print("|     2 - Eletrônicos                  |")
                print("|     3 - Peças de Computador          |")
                print("|                                      |")
                print("|--------------------------------------|")
                g = input("Digite:")
                jogo.generos(g)
            case "2":
                qtd = input("Quantas palavras quer adicionar?:")
                for i in range(int(qtd)):
                    jogo.append()
                lista = jogo.to_list()
                jogo.dificuldade(lista)

    #função para escolher o modo de jogo
    def escolha(self, v):
        match v:
            case "1":
                print("|-----------------|----------------|")
                print("|                 |                |")
                print("|    Jogar com    |    Jogar com   |")
                print("|     palavras    |     palavras   |")
                print("|    aleatorias   |     escritas   |")
                print("|       [1]       |       [2]      |")
                print("|-----------------|----------------|")
                o = input("Digite:")
                jogo.opcao(o)
            case "2":
                SystemExit
            case _:
                print("Não existe essa opção!")

    #função de restart do jogo
    def replay(self):
        print("|-------------------------------------------------------------------|")
        print("|                                                                   |")
        print("|                        Forca Do Perneta                           |")
        print("|                                                                   |")
        print("|                        |------|                                   |")
        print("|                        |      O                                   |")
        print("|                        |     <|>                                  |")
        print("|                        |     / `                                  |")
        print("|                        |___                                       |")
        print("|                                                                   |")
        print("|                     Deseja jogar novamente?                       |")
        print("|                                                                   |")
        print("|                     Sim - Digite um                               |")
        print("|                     Não - Digite dois                             |")
        print("|-------------------------------------------------------------------|")
        jogo.escolha(input("Digite:"))

jogo = Lista()
lt = Lista_tentativa()

print("|-------------------------------------------------------------------|")
print("|                                                                   |")
print("|                        Forca Do Perneta                           |")
print("|                                                                   |")
print("|                        |------|                                   |")
print("|                        |      O                                   |")
print("|                        |     <|>                                  |")
print("|                        |     / `                                  |")
print("|                        |___                                       |")
print("|                                                                   |")
print("|                         Deseja iniciar?                           |")
print("|                                                                   |")
print("|                     Sim - Digite um                               |")
print("|                     Não - Digite dois                             |")
print("|-------------------------------------------------------------------|")
jogo.escolha(input("Digite:"))