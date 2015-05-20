__author__ = 'Vicky Zhang'

l = ['chocolate brown','brown', 'chocolate']

sentence = "The jeans is chocolate brown in color and has brown colored pockets"

for word in l:
    sentence_new = sentence.replace(word + ' ', '')

    sentence = sentence_new

print(sentence)