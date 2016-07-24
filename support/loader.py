
import codecs
import json
from utils import Utils

class Loader(object):

    INPUT_PATH = './input'

    # Check if the set range is valid. Returns the training set range of file.
    def checkSetRange(self, file, setRange):
        try:
            # parse setRange to float or int
            setRange = float(setRange) if '.' in setRange else int(setRange)
            # read file
            with codecs.open(file, 'r') as fi:
                # get file length
                total = len(fi.readlines())
                # check if the range is int
                if isinstance(setRange, int):
                    # check if range is invalid
                    if setRange > total:
                        return None
                    # return range
                    return setRange
                # check if the range is float
                elif isinstance(setRange, float):
                    # check if range is invalid
                    if setRange >= 1.0:
                        return None
                    # return range
                    return int(total * setRange)
                else:
                    print "Error: The range must be a int or float value."
                    return None
        except:
            return None

    # Amend line.
    def amendLine(self, file):
        _return = file.replace("[", "")
        _return = _return.replace("]", "")
        _return = _return.replace("},", "}")
        _return = _return.replace("\r\n", "")
        _return = _return.replace("\r","").replace("\n","")
        return _return

    # Load input data.
    def load(self, trainingSetRange):
        _return = []
        _utils = Utils()
        # check if input dir exists
        if not _utils.checkDir(self.INPUT_PATH):
            print "Error: Input data not found."
            return None
        # check if input files exists
        _files = _utils.listDir(self.INPUT_PATH)
        if _files is None:
            print "Error: Input data not found."
            return None

        # class name
        _className = ""
        # load data files
        for file in _files:
            print "Loading data from file... : {:s}".format(file)
            # check if training set range is valid
            _limit = self.checkSetRange(file, trainingSetRange)
            if (_limit is None) or (_limit <= 0):
                print "Error: The test set is out of range."
                return None
            # open file to read data
            _partialSet = []
            # TODO: Run NBAC with multiple categories on single file
            with codecs.open(file, mode='r', encoding='utf-8', errors='ignore') as fi:
                # training set
                _trainingSet = []
                # test set
                _testSet = []
                # iterator
                _it = 0
                # run file
                for line in fi:
                    # amend line
                    line = self.amendLine(line)
                    # check if line is empty
                    if line in ["", u'\n', u'\r\n']:
                        continue
                    # load line as json
                    _json = json.loads(line)
                    _info = ""
                    # get data
                    for key, value in _json.items():
                        # get category
                        if key == "category":
                            _className = value
                        else:
                        # get text (concatenation: "subject" + "body")
                            _info += value
                    # check if its not the end of training range...
                    if _it < _limit:
                        # set training data
                        _trainingSet.append(_info.encode("utf-8"))
                        # increment iterator
                        _it += 1
                        continue
                    # ...otherwise, its test range
                    else:
                        # set test data
                        _testSet.append(_info.encode("utf-8"))
                        # increment iterator
                        _it += 1
                        continue
                # end of file

                # store partial data
                _partialSet.append(_className)
                _partialSet.append(_trainingSet)
                _partialSet.append(_testSet)

            # return all data
            _return.append(_partialSet)
        print ""
        return _return
