def make_sentence(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

x=12
y="気温"
z=22.4

print(make_sentence(x, y, z))