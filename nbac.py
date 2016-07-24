#!/usr/bin/env python

import sys
from nb.classifier import Classifier
from nb.trainer import Trainer
from support.loader import Loader
from support.writer import Writer
from support.utils import Utils

def main():
    print "### NBAC - Naive Bayes Ads Classifier ###","\n"

    # Check if the training set limit was given by argv
    if len(sys.argv) != 2:
        print "Usage: python nbac.py <training-set-limit>"
        # exit
        return -1

    # Initiate Utilities
    utils = Utils()
    utils.startTimer()

    # Initiate Loader
    loader = Loader()
    # Get the training set limit
    limit = sys.argv[1]
    # Load all data
    data = loader.load(limit)
    # Check if data is invalid
    if data is None:
        print "Exiting..."
        utils.stopTimer()
        exit()

    # Initiate Trainer
    trainer = Trainer()
    for _class in data:
        # get the training set
        _trainingData = _class[1]
        # get the class name
        print "Training data...     class:", _class[0]
        for _info in _trainingData:
            # training data
            trainer.train(_info, _class[0])


    # Initiate Classifier
    classifier = Classifier(trainer.feature, sum([len(x[1]) for x in data]))
    for _class in data:
        # get the test set
        _testData = _class[2]
        # get the class name
        print "Classifying data...  class:", _class[0]
        for _info in _testData:
            # classify data
            _classification = classifier.classify(_info)
            # get the suggested class
            _suggestedClass = _classification[0][0]
            # 1:text, 2:original class, 3:suggested class, 4:classification is correct?
            classifier.setResult(_info[:47], _class[0], _suggestedClass, _class[0] == _suggestedClass)

    # Print result
    classifier.printSummary()
    # Save summary in result
    classifier.setSummary()

    # Save data
    writer = Writer()
    writer.save(classifier.result)

    utils.stopTimer()
    # END



if __name__ == "__main__":
    main()
