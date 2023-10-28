from collections import defaultdict
import ngram_score as ns

fitness = ns.ngram_score('english_quadgrams.txt')
#abre o texto codificado em binário
bin = open("encoded_sub.txt", "r")

#lê o texto codificado em binário, e separa cada membro em uma lista
binary_list = bin.read().split()

#Cria uma lista para os números convertidos para decimal
char_number_list = []

#itera pela lista de binários
for i in binary_list:
    #converte binário em decimal e o adiciona à lista de números decimais
    char_number_list.append(int(i, 2))

char_number_list = [i for i in char_number_list if i != 32]

count_letters = defaultdict(int)
sentence = []

for char in char_number_list:
    sentence.append(chr(char))
    count_letters[chr(char)] += 1

count_letters = dict(sorted(count_letters.items(), key=lambda item: item[1], reverse=True))
print(sentence)
print(count_letters)



"""
#lista onde serão armazenados os valores de "score" para cada frase gerada
scores_list = []

#onde serão geradas as frases e seus respectivos valores de "score"
for i in range(26):
    #armazena os números ascii modificados a cada iteração
    char_number_newlist = []
    #armazena a nova string, para cálculo do score
    char_string_nova = []


    for n in char_number_list:
        num = i+n
        if num-i == 32:
            char_number_newlist.append(32)
        elif num > 90:
            num = num % 90
            char_number_newlist.append(num + 64)
        else:
            char_number_newlist.append(num)

    for char in char_number_newlist:
        char_novo = chr(char)
        char_string_nova.append(char_novo)
    string_nova = ''.join(char_string_nova)
    scores_list.append(fitness.score(string_nova))"""