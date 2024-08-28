import spacy

nlp = spacy.blank("en")

entity_ruler = nlp.add_pipe("entity_ruler")

patterns = [
    {"label":"ORG","pattern":"Microsoft"},        
    {"label":"GPE","pattern":[{"LOWER":"san"},{"LOWER":"francisco"}]}
            ]

entity_ruler.add_patterns(patterns)


doc = nlp("Microsoft is hiring software developer in San Francisco.")

entity_ruler.to_disk("my_entity_ruler")

print([(ent.text, ent.label_) for ent in doc.ents])