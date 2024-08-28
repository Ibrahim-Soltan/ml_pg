import spacy
nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

# Text ->
# Tokenizer => Tagger => Parser => NER => ...
# -> Doc

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
print(other_pipes)
nlp.disable_pipes(*other_pipes)