import spacy
import spacy.displacy
nlp = spacy.load("en_core_web_md")


# POS tagging

# text = "My cat will fish for a fish tomorrow in a fishy way."
# print([(token.text, token.pos_,spacy.explain(token.pos_)) for token in nlp(text)])

# Dependency Parsing 

text = "We understand the differences."
# spacy.displacy.serve(nlp(text),style="dep")



print([(token.text, token.dep_, spacy.explain(token.dep_)) for token in nlp(text)])
