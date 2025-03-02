
s = "Un aa chasseur sachant chasser sait chasser sans son chien"

# Trouver le mot le plus petit
#word = []
# word = s.split(" ")
# word_len = []
# for e in word:
#     word_len.append(len(e))
#
# print(word)
#
# print("Le mot le plus court est : ",min(word, key=len),".")
# print("Le mot le plus long est : ",max(word, key=len),".")

def min_max_words(sentence):
    word = sentence.split(" ")
    _min_word = min(word, key=len)
    _max_word = max(word, key=len)
    return _min_word, _max_word



def get_min_max_words_sorted(sentence):
    word = sentence.split(" ")
    min_w, max_w = min_max_words(sentence)

    all_min_words = [w for w in word if len(w) == len(min_w)]
    all_max_words = [w for w in word if len(w) == len(max_w)]

    all_max_words.sort()
    all_min_words.sort()
    return all_min_words[0], all_max_words[0]

# I prefered this one :

def get_min_max_words_sorted2(sentense):
    words = sentense.split()
    words.sort()
    min_wor_sorted = min(words, key=len)
    max_word_sorted = max(words, key=len)
    return min_wor_sorted, max_word_sorted


min_word, max_word = get_min_max_words_sorted2(s)
print(f"Le mot le plus court dans la phrase est : '{min_word}' et le plus long est : '{max_word}'.")

