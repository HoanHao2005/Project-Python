
#Bai 2
import string

sentence = "Lap trinh Python va AI - Truong Cong nghe va thiet ke - Dai Hoc UEH Thanh Pho Ho Chi Minh."


sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()

letter_counts = {}

for letter in sentence:
    if letter.isalpha():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

for letter, count in letter_counts.items():
    print(f"{letter}: {count}")