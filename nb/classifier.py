
from __future__ import division
import operator
from functools import reduce
from tokenizer import Tokenizer

class Classifier(object):

    def __init__(self, feature, totalTrained):
        super(Classifier, self).__init__()
        self.feature = feature
        self.totalTrained = totalTrained
        self.tokenizer = Tokenizer()
        self.defaultProbability = 0.000000001
        self.result = []
        print ""

    # Classify data using the given text.
    def classify(self, text):
        classes = self.feature.getClasses()
        # get only unique tokens
        tokens = list(set(self.tokenizer.tokenize(text)))
        # probabilities of classes
        classesProbabilities = {}
        for className in classes:
            # calculate the probability of each token found in the text of this class
            # P ( Token_i | Class_i )
            tokensProbabilities = [self.getTokenProbability(token, className) for token in tokens]

            # calculate the probability of the set of tokens found in the text of this class
            # P ( Token_1 | Class_i ) * P ( Token_2 | Class_i ) * ... * P ( Token_n | Class_i )
            try:
                tokenSetProbabilities = reduce(lambda a, b: a * b, (i for i in tokensProbabilities if i))
            except:
                tokenSetProbabilities = 0

            classesProbabilities[className] = tokenSetProbabilities * self.getPriorClassProbability(className)

        return sorted(classesProbabilities.items(), key=operator.itemgetter(1), reverse=True)

    # Get the prior probability of class.
    def getPriorClassProbability(self, className):
        return self.feature.getClassDocCount(className) / self.feature.getDocCount()

    # Get the token probability.
    def getTokenProbability(self, token, className):
        # P ( Class_i )
        classDocumentCount = self.feature.getClassDocCount(className)

        # if the token was not found in the training set, then return None to not include it into calculations
        try:
            tokenFrequency = self.feature.getFrequency(token, className)
        except Exception as e:
            return None

        # the token was not found in this class but it was in others
        if tokenFrequency is None:
            return self.defaultProbability
        # calculate token probability
        tokenProbablity = tokenFrequency / classDocumentCount
        return tokenProbablity

    # Set the classification result.
    # 1:text, 2:original class, 3:suggested class, 4:classification is correct?
    def setResult(self, text, originalClass, suggestedClass, correctness):
        self.result.append([text, originalClass, suggestedClass, correctness])

    # Get the final classification result.
    def calculateResult(self):
        # Compute trained
        _trained = self.totalTrained
        # Compute tested
        _tested = len(self.result)
        # Compute correct results
        _correct = len([r[3] for r in self.result if r[3]])
        # Compute and print accuracy
        _accuracy = (_correct / _tested)
        _accuracy *= 100
        return (_trained, _tested, _correct, _accuracy)

    # Set the summary in the last position of result set.
    def setSummary(self):
        (_trained, _tested, _correct, _accuracy) = self.calculateResult()
        self.setResult(_trained, _tested, _correct, _accuracy)

    # Print the final result of classification.
    def printSummary(self):
        (_trained, _tested, _correct, _accuracy) = self.calculateResult()
        print "\n", "Summary of {:d} training cases and {:d} test cases: ".format(_trained, _tested) + \
                    "{:d} correct; accuracy: {:.2f}".format(_correct, _accuracy)
