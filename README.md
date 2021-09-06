# **ACM-Research-Coding-Challenge-F21**

For this Python program, I used the VADER (Valence Aware Dictionary and sEntiment Reasoner) library from the NLTK package to analyze the input file. In order to determine an overall sentiment score, I read in the contents of the input file and passed the contents to the sia.polarity\_scores() method. I also used the word\_tokenize() method to split the text into individual words and determined separate sentiment scores for the first and latter half of the words. Moreover, I separated each sentence of the input file using the sent\_tokenize() method and then determined the sentiment score for each sentence.

The output of the program includes the overall sentiment score (along with the distribution of positive, negative, and neutral scores) of the entire file and a table displaying the individual sentence scores.

The overall sentiment score of the text is 0.9982, with the breakdown being *{'neg': 0.065, 'neu': 0.748, 'pos': 0.187, 'compound': 0.9982}*. This score is based on a scale from -1 to +1, with the thresholds for positive, neutral, and negative sentiment specified below:

  *1. positive sentiment: compound score >= 0.05*  
  *2. neutral sentiment: (compound score > -0.05) and (compound score < 0.05)*  
  *3. negative sentiment: compound score <= -0.05*

0.9982 is greater than 0.05, which indicates that this text most likely has a positive sentiment.

I did expect a fairly positive sentiment score upon initially reading the input file, especially due to the positive descriptors used in the latter half of the text, but I was not confident in the strength of the positive descriptors because of the more forceful, negative words in the first half. This is what led me to include an analysis of the 1st half and 2nd half of the text, divided by word count. The program output indeed shows that the proportion of negative words is higher for the 1st than the 2nd, although both halves still had positive sentiment overall:

  *1st half sentiment score: {'neg': 0.099, 'neu': 0.76, 'pos': 0.141, 'compound': 0.8766}*  
  *2nd half sentiment score: {'neg': 0.055, 'neu': 0.731, 'pos': 0.213, 'compound': 0.9968}*

### Sources
[https://github.com/cjhutto/vaderSentiment#about-the-scoring](https://github.com/cjhutto/vaderSentiment#about-the-scoring)

[https://realpython.com/python-nltk-sentiment-analysis/](https://realpython.com/python-nltk-sentiment-analysis/)

[https://github.com/tristaneljed/Sentiment-Analysis-Movie-Reviews-NLTK/blob/master/sentiment\_analysis.ipynb](https://github.com/tristaneljed/Sentiment-Analysis-Movie-Reviews-NLTK/blob/master/sentiment_analysis.ipynb)
