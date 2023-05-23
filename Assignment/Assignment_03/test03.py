import string
from collections import Counter
import spacy
def find_top_five(my_file_name):
    top_five_tokens = {}
    # load english language model
    nlp = spacy.load('en_core_web_sm')
    with open(my_file_name,'r') as file:

        # convert all characters to lower case and ignore all the punctuation
        text = file.read().lower().translate(str.maketrans('','',string.punctuation))

        # process the text using Spacy language model
        doc = nlp(text)

        # count the tokens
        token_counts = Counter(token.text for token in doc if token.text.isalnum())

    top_five_tokens = token_counts.most_common(5)

    return(print(top_five_tokens))



if __name__ == "__main__":
    find_top_five('Assignment\Assignment_03\corpus.txt')
