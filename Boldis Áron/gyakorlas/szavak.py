word1 = input("Adj meg egy szót: ")
word2 = input("Adj meg egy másik szót: ")

word1_len = len(word1)
word2_len = len(word2)

if word1_len > word2_len:
    print("A hosszabb szó: ", word1)
elif word1_len < word2_len:
    print("A hosszabb szó: ", word2)
else:
    print("A két szó egyforma hosszú.")