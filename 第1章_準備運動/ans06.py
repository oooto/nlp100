def ngram(seq, n):
    return [seq[i: i+n] for i in range(len(seq)-n+1)]

org_str1 = "paraparaparadise"
org_str2 = "paragraph"

X = set(ngram(org_str1, 2))
Y = set(ngram(org_str2, 2))

print("XとYの和集合: {}".format(X | Y))
print("XとYの積集合: {}".format(X & Y))
print("XとYの差集合: {}".format(X - Y))

print("'se'がXに含まれている: {}".format("se" in X))
print("'se'がYに含まれている: {}".format("se" in Y))
