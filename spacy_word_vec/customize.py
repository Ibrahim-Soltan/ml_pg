import spacy
from spacy.training import Example
import random

nlp = spacy.load("en_core_web_sm")

text = "I will visit you in Austin."
annotations = {"entities":[(20,26,"GPE")]}

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

nlp.disable_pipes(*other_pipes)



# optimizer = nlp.begin_training() for trainging from scratch
optimizer = nlp.create_optimizer()

epochs = 10
losses = {}
training_data = zip(text, annotations)
for i in range(epochs):
    random.shuffle(training_data)
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], sgd = optimizer, losses=losses)
ner = nlp.get_pipe("ner")
ner.to_disk("<ner model name>")
ner = nlp.create_pipe("ner")
ner.from_disk("<ner model name>")
nlp.add_pipe(ner, "<ner model name>")