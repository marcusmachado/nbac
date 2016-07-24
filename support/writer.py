
import codecs
from utils import Utils

class Writer(object):

    OUTPUT_PATH = './output'

    # Save the result data.
    # TODO: Save the classification result in JSON format
    def save(self, data):
        print "\n", "Saving results..."
        try:
            _utils = Utils()
            # check if output dir exists
            _utils.makeDir(self.OUTPUT_PATH)
            # define file name
            fileName = self.OUTPUT_PATH + "/result_{}".format(_utils.getDateAsStr()) + ".txt"
            # open file
            file = codecs.open(fileName, 'w', encoding='utf-8', errors='ignore')

            # writing title
            print >> file, "#" * 120
            print >> file, "#" + (" " * 46) + "Naive Bayes Ads Classifier" + (" " * 46) + "#"
            print >> file, "#" * 120

            # writing summary
            # pop the summary of the set last position
            summary = data.pop(-1)
            print >> file, "#" + " Summary of {:d} training cases and {:d} test cases: ".format(summary[0], summary[1]) + \
                           "{:d} correct; accuracy: {:.2f}".format(summary[2], summary[3]) + (" " * 35) + "#"
            print >> file, "#" * 120

            # writing header
            print >> file, "#" + " Text" + (" " * 43) + "#" + \
                           (" " * 5) + "Original Class" + (" " * 5) + "#" + \
                           (" " * 5) + "Suggested Class" + (" " * 4) + "#" + \
                           (" " * 5) + "Correctness" + (" " * 3) + "#"
            print >> file, "#" * 120

            # writing results
            for rst in data:
                # text
                text = (rst[0]).decode("ascii", "ignore") + "..."
                text = text + (" " * (47 - len((rst[0]).decode("ascii", "ignore")))) + (" " * 5)
                # original class
                tclass = rst[1] + (" " * (20 - len(rst[1]))) + (" " * 5)
                # suggested class
                pclass = rst[2] + (" " * (20 - len(rst[2]))) + (" " * 5)
                # correctness
                correct = ("%s" % rst[3]) + (" " * (15 - len(("%s" % rst[3]))))
                # writing data
                print >> file, (text + tclass + pclass + correct)
            file.close()

        except Exception, e:
            print e
            pass
