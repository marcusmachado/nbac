
class Feature(object):

    def __init__(self):
        self.docCountOfClasses = {}
        self.frequencies = {}

    # Increase class of a document.
    def increaseClass(self, className):
        self.docCountOfClasses[className] = self.docCountOfClasses.get(className, 0) + 1

    # Increase token of a class.
    def increaseToken(self, token, className):
        if not token in self.frequencies:
            self.frequencies[token] = {}
        self.frequencies[token][className] = self.frequencies[token].get(className, 0) + 1

    # Get all documents count.
    def getDocCount(self):
        return sum(self.docCountOfClasses.values())

    # Get the available classes as list.
    def getClasses(self):
        return self.docCountOfClasses.keys()

    # Get the class count of the document. Returns None if it was not found.
    def getClassDocCount(self, className):
        return self.docCountOfClasses.get(className, None)

    # Get frequency of a token in the class. Returns None if it was not found.
    def getFrequency(self, token, className):
        try:
            foundToken = self.frequencies[token]
            return foundToken[className]
        except:
            return None
