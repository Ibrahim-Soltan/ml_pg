import spacy
from spacy.matcher import Matcher, PhraseMatcher

nlp = spacy.load("en_core_web_sm")

doc = nlp("Good morning, this is our first day in campus.")


# Matchers
matcher = Matcher(nlp.vocab)

pattern = [{"LOWER":"good"},{"LOWER":{"IN":["morning","evening"]}}]
matcher.add("greeting",[pattern])

matches = matcher(doc)

for match_id, start, end in matches:
    print("Start token: ", start, " | End token", end, " | Matched text", doc[start:end].text)



# PhraseMatchers 


matcher = PhraseMatcher(nlp.vocab)
# Attributes:
# attr = "LOWER" for mathcing all cases
# attr = "SHAPE" figures out the common properties of the terms and match based on it

terms = ["Bill Gates","John Smith"]

patterns = [nlp.make_doc(term) for term in terms]
matcher.add("PeopleOfInterest",patterns)


doc = nlp("Bill Gates met John Smith for an important discussion regarding importance of AI")

matches = matcher(doc)

for match_id, start, end in matches:
    print("Start token: ", start, " | End token", end, " | Matched text", doc[start:end].text)
