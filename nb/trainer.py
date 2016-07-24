
from feature import Feature
from nb.tokenizer import Tokenizer

class Trainer(object):

    def __init__(self):
        super(Trainer, self).__init__()
        self.tokenizer = Tokenizer()
        self.feature = Feature()

    # Training data using the given text and class.
    def train(self, text, className):
        # increase class
        self.feature.increaseClass(className)
        # tokenize text
        tokens = self.tokenizer.tokenize(text)
        # increase token
        for token in tokens:
            self.feature.increaseToken(token, className)
