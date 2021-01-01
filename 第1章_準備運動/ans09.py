import random
import re

def typoglycemia(org_sentence, seed=0):
    random.seed(seed)
    word_list = re.split(r'\s|,|:|\.', org_sentence)
    random_sentence = [w[0] + ''.join(random.sample(w[1:-1], len(w[1:-1]))) + w[-1] if len(w) > 4 else w for w in word_list]
    return " ".join(random_sentence)

org_sentence = "I couldn’t believe that I could actually understand what I was reading: the phenomenal power of the human mind."
print(typoglycemia(org_sentence))

