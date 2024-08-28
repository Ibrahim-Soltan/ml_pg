import spacy
nlp = spacy.load("en_core_web_md")

doc1 = nlp("We eat pizza")
doc2 = nlp("We like to eat pasta")

token1 = doc1[2]
token2 = doc2[4]

span1 = doc1[1:]
span2 = doc2[1:]


# print(f"Similarity between \"{span1}\" and \'{span2}\" = ",
#       round(span1.similarity(span2),3))

# print(f"Similarity between \"{doc1[1:]}\" and \'{doc2[3:]}\" = ",
#       round(doc1[1:].similarity(doc2[3:]),3))






# print(f"Similarity between {token1} and {token2} = ",
#       round(token1.similarity(token2),3))