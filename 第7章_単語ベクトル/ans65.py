import pathlib

import pandas as pd
from sklearn.metrics import accuracy_score


folder_path = pathlib.Path(__file__).resolve().parent
df = pd.read_pickle(folder_path / "analogy_data.pkl")

tras_dict = {
    'capital-world': "semantic-analogy",
    'city-in-state': "semantic-analogy",
    'currency': "semantic-analogy",
    'capital-common-countries': "semantic-analogy",
    'family': "semantic-analogy",
    'gram1-adjective-to-adverb': "syntactic-analogy",
    'gram2-opposite': "syntactic-analogy",
    'gram3-comparative': "syntactic-analogy",
    'gram4-superlative': "syntactic-analogy",
    'gram5-present-participle': "syntactic-analogy",
    'gram6-nationality-adjective': "syntactic-analogy",
    'gram7-past-tense': "syntactic-analogy",
    'gram8-plural': "syntactic-analogy",
    'gram9-plural-verbs': "syntactic-analogy",
}
df["analogy"] = df["category"].map(tras_dict)
analogy_list = ["semantic-analogy", "syntactic-analogy"]
for analog in analogy_list:
    tmp = df[df["analogy"] == analog]
    print("{} accuracy: {}".format(analog, accuracy_score(tmp["w4"], tmp["word"])))