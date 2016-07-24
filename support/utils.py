
import os
from time import localtime, strftime, gmtime, time

class Utils(object):

    # Start timer.
    def startTimer(self):
        self.startedTime = time()
        print "> Start Time: ", strftime("%a, %d %b %Y %H:%M:%S", localtime()), "\n"

    # Stop timer.
    def stopTimer(self):
        print "\n", "> Completed at: {:s}  /  Total: {:s}".format(
            strftime("%a, %d %b %Y %H:%M:%S", localtime()), strftime("%H:%M:%S", gmtime((time() - self.startedTime))) )

    # Get the date as string.
    def getDateAsStr(self):
        return strftime("%Y_%m_%d_%H_%M_%S", localtime())

    # Get the file list of a given directory.
    def listDir(self, dir):
        _return = None
        for file in os.listdir(dir):
            _path = os.path.join(dir, file)
            try:
                # check the file
                if os.path.isfile(_path):
                    if _return is None:
                        _return = []
                    _return.append(_path)
            except Exception, e:
                print e
        return _return

    # Check if file exists in the directory.
    def checkFileDir(self, dir, file):
        files = self.listDir(dir)
        if files is not None:
            for file_path in files:
                if os.path.split(file_path)[1] == file:
                    return True
                else:
                    return False

    # Check if dir exists.
    def checkDir(self, dir):
        if os.path.exists(dir):
            return True
        else:
            return False

    # Create a directory.
    def makeDir(self, dir):
        # if the directory does not exist
        if not os.path.exists(dir):
            # make the directory
            os.makedirs(dir)

    # Clean a directory.
    def cleanDir(self, dir):
        files = self.listDir(dir)
        if files is not None:
            # removes all files in a folder
            for file_path in files:
                try:
                    # unlink (delete) the file
                    os.unlink(file_path)
                except Exception, e:
                    print e
                    return -1
