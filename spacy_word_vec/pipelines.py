import spacy

blank_nlp = spacy.blank("en")
blank_nlp.add_pipe("sentencizer")
doc = blank_nlp("Hello, my name is Ibrahim. I am 21 years old.")

print(blank_nlp.analyze_pipes(pretty=True))
print([sent for sent in doc.sents])