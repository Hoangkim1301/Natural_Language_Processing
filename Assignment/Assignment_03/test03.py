import spacy
from collections import Counter
import string


def find_top_five(my_file_name):
    # Load the English language model in spaCy
    nlp = spacy.load('en_core_web_sm')

    # Read the contents of the file
    with open(my_file_name, 'r') as file:
        text = file.read()

    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text using spaCy
    doc = nlp(text)

    # Filter out stopwords and non-alphabetic tokens
    tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]

    # Count the frequency of each token
    token_counts = Counter(tokens)

    # Get the top five most frequent tokens
    top_five = token_counts.most_common(5)

    # Convert the top five results to a dictionary
    top_five_dict = dict(top_five)

    return top_five_dict


if __name__ == "__main__":
    find_top_five('corpus.txt')
