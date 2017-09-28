from sys import stdin
import string
dict = dict.fromkeys(string.ascii_lowercase, '')

def flexradix(A, d):
    i = 0
    sorted_list = []
    reduced_list = []
    lists = []
    for word in A:
        if any(str.isalpha(c) for c in word):
            place_word_in_dict(word, i)
    for key, value in dict.items():
        if value:
            lists = value.split()
            while
            reduced_list = reduced_list + lists
    print(reduced_list)
    for words in reduced_list:
        return
    while i < d:
        for word in reduced_list:
            if len(word) > i:
                place_word_in_dict(word, i)
                print(dict)
        i += 1






    # Du må mest sannsynlig lage egne hjelpefunksjoner for denne funksjonen for å løse oppgaven.
    # Funksjonen skal returnere listen A sortert.
    # SKRIV DIN KODE HER
def place_word_in_dict(word, index):
    s = word[index]
    dict[s]+=(word + ' ')

def get_character_value(word, index):
    return ord(word[index])

# helper to find the lowest(first) word
def string_compare(word1, word2):
    if len(word1) < len(word2):
        length = len(word1)
        i = True
    elif len(word2) < len(word1):
        length = len(word2)
        i = False
    else:
        length = len(word1)
    for x in range(length):
        if word1[x] < word2[x]:
            return word1
        elif word2[x] < word1[x]:
            return word2
    # if word1 is shortest return it
    if i:
        return word1
    return word2
def place_in_order(list):
    for words in list:
        return


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)

    for string in A:
        print(string)


if __name__ == "__main__":
    main()
