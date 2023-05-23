import spacy

# Import English
from spacy.lang.en import English

nlp = English()

raw = "Hard to judge whether these sides were good. We were grossed " \
      "out by the melted styrofoam and didn't want to eat it for fear of getting sick."

doc = nlp(raw)

if __name__ == "__main__":
      print('test')
      print(doc)
      
      

