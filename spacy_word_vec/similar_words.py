import numpy as np
import spacy
nlp = spacy.load("en_core_web_md")

word = "computer"

most_similar_words = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]]), n= 5)

words = [nlp.vocab.strings[w] for w in most_similar_words[0][0]]
print(words)