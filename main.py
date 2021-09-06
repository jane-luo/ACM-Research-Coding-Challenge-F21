# nltk.download(["punkt", "vader_lexicon"])
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from tabulate import tabulate

sia = SentimentIntensityAnalyzer()


# Read in the contents of a file
def read_file(file_name):
    with open(file_name) as f:
        contents = f.read()
    return contents


# Format data for sentence polarity scores in a table
def create_table():
    i = 0
    sentences = sent_tokenize(read_file("input.txt"))
    table = []
    head = ["Sentence", "Polarity Score"]
    while i < len(sentences):
        table.append((i + 1, sia.polarity_scores(sentences[i])))
        i += 1
    return tabulate(table, headers=head, tablefmt="grid")


# Divide the text in half based on word count, and then analyze each half
def half_analysis():
    words = word_tokenize(read_file("input.txt"))
    first_half = ""
    second_half = ""

    i = 0
    for word in words:
        if i < (len(words) / 2):
            first_half += words[i] + " "
        else:
            second_half += words[i] + " "
        i += 1

    print("1st half sentiment score:", sia.polarity_scores(first_half))
    print("2nd half sentiment score:", sia.polarity_scores(second_half), "\n")


def main():
    print("Overall sentiment score:", sia.polarity_scores(read_file("input.txt")))
    half_analysis()
    print(create_table())


if __name__ == "__main__":
    main()
