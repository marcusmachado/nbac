
import re
from vocabulary import Vocabulary

class Tokenizer(object):

    # Tokenize a text.
    def tokenize(self, text):
        # remove all special characters and punctuation
        text = re.sub('\W+', ' ', text)
        # clean up text
        cleanText = self.cleanUpText(text)
        # check if text is valid
        if cleanText:
            return cleanText
        else:
            return text.lower().split(' ')

    # Clean up text by removing the stopwords.
    def cleanUpText(self, text):
        cleanedWords = []
        # perform lowercase
        words = text.lower().split(' ')
        # get vocabulary
        vocab = Vocabulary()
        for word in words:
            # check Portuguese stopwords
            # TODO: Implement other languages tokenizers
            if not (word in vocab.getPTStopWords()):
                cleanedWords.append(word)
        return cleanedWords
