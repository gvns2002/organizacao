from nltk import ngrams
import ngram_score as ns

fitness = ns.ngram_score('english_quadgrams.txt')

#abre o texto codificado em binário
bin = open("encoded_ces.txt", "r")


#lê o texto codificado em binário, e separa cada membro em uma lista
binary_list = bin.read().split()

#Cria uma lista para os números convertidos para decimal
char_number_list = []

#itera pela lista de binários
for i in binary_list:
    #converte binário em decimal e o adiciona à lista de números decimais
    char_number_list.append(int(i, 2))


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
    scores_list.append(fitness.score(string_nova))

#obtenção da "chave" que dará o deslocamento necessário para obtenção do resultado

#converte todos os valores da lista em seus valores absolutos
scores_list = [abs(i) for i in scores_list]
#procura o menor s
chave = scores_list.index(min(scores_list))

#obtenção e impressão da frase correta
string_correta_list = []
for i in char_number_list:
    num = i + chave
    if num < 65:
        num = 32
    if num > 90:
        num = (num % 90) + 64
    char_correto = chr(num)
    string_correta_list.append(char_correto)

string_correta = ''.join(string_correta_list)
print(string_correta)


