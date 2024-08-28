import spacy
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

nlp = spacy.load("en_core_web_md")
# print(nlp.meta["vectors"])

# like_id = nlp.vocab.strings["like"]
# print(like_id)
# print(nlp.vocab.vectors[like_id])

words = ["wonderful", "horrible", 
         "apple", "banana","orange", "watermelon",
         "dog","cat"]

words_vectors = np.vstack([nlp.vocab.vectors[nlp.vocab.strings[w]] for w in words])
pca = PCA(n_components = 2)
words_vectors_transformed = pca.fit_transform(words_vectors)

plt.figure(figsize=(10,8))
plt.scatter(words_vectors_transformed[:,0], words_vectors_transformed[:,1])

for word, coord in zip(words, words_vectors_transformed):
    x, y = coord
    plt.text(x,y,word,size=10)
# plt.savefig("word_vectors_plot.png", format="png")


