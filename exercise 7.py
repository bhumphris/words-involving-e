word_without_e = 0
word_with_e = 0
total_words = 0

fin = open('word.txt')
print('words containing no letter E\n')


def no_e(word):
    if 'e' in word:
        return False
    else:
        return True
for line in fin:
    word = line.strip()
    if word != '  ':
        total_words += 1
        word_without_e(word)
        if word_without_e(word) is True:
            word_with_e += 1
            print word
        else:
            word_with_e += 1

percent = 100 * (word_without_e / float(total_words))
print('\nTotal number of words in file with no letter E: ' + str(word_without_e))
print('\nTotal number of words in file containing the letter E: ' + str(word_with_e))
print('\nTotal number of words in file: ' + str(total_words))
print('\nPercentage of words in file with no letter E is: ' + str(round(percent, 4)) + '%')
