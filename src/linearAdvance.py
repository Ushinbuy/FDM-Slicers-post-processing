#!/usr/bin/env python3

import sys
import re

from gcodeFileManager import GcodeFileHandler

class SimplifyLinearAdvance(GcodeFileHandler):
    def _searchLaValue(self):
        searchString = "; LA value "
        indexStart = self._fileBuffer.find(searchString)
        indexStop = self._fileBuffer.find("\n", indexStart)
        tempString = self._fileBuffer[indexStart + len(searchString): indexStop]
        anotherIndexStop = tempString.find(",")
        if(anotherIndexStop > 0):
            print(tempString)
            indexStop = anotherIndexStop + indexStart + len(searchString)
            print(indexStart,indexStop)
        self.maxValueLA = self._fileBuffer[indexStart + len(searchString): indexStop]

        listOfValue = re.findall("[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", self.maxValueLA)
        self.minValueLA = self.maxValueLA.replace(str(listOfValue[-1]), '0')

    def _patchBuffer(self):
        delimeter = "; layer 2"
        tempBuffer = self._fileBuffer.split(delimeter)
        if len(tempBuffer) == 1:
            self.uncorrectSlicerInArguments()
        tempBuffer[1] = delimeter + tempBuffer[1]
        tempBuffer[1] = tempBuffer[1].replace("perimeter\nG", "perimeter\n" + self.maxValueLA + "\nG")
        tempBuffer[1] = tempBuffer[1].replace("; solid layer\n", "; solid layer\n" + self.minValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace("fill\n", "fill\n" + self.minValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace("; skirt\nG", "; skirt\n" + self.minValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace("; bridge\n", "; bridge\n" + self.minValueLA + "\n")
        self._fileBuffer = "".join(tempBuffer)


class PrusaSlicerLinearAdvance(GcodeFileHandler):
    def _searchLaValue(self):
        searchString = "; LA value "
        indexStart = self._fileBuffer.find(searchString)
        indexStop = self._fileBuffer.find("\n", indexStart)
        tempString = self._fileBuffer[indexStart + len(searchString): indexStop]
        anotherIndexStop = tempString.find(",")
        if(anotherIndexStop > 0):
            print(tempString)
            indexStop = anotherIndexStop + indexStart + len(searchString)
            print(indexStart,indexStop)
        self.maxValueLA = self._fileBuffer[indexStart + len(searchString): indexStop]
        listOfValue = re.findall("[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", self.maxValueLA)
        self.minValueLA = self.maxValueLA.replace(str(listOfValue[-1]), '0')

    def _patchBuffer(self):
        delimeter = "layer (1)"
        tempBuffer = self._fileBuffer.split(delimeter)
        if len(tempBuffer) == 1:
            self.uncorrectSlicerInArguments()
        tempBuffer[1] = delimeter + tempBuffer[1]
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:External perimeter\n", ";TYPE:External perimeter\n" + self.maxValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:Perimeter\n", ";TYPE:Perimeter\n" + self.maxValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:Top solid infill\n", ";TYPE:Top solid infill\n" + self.maxValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:Overhang perimeter\n", ";TYPE:Overhang perimeterr\n" + self.minValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:Internal infill\n", ";TYPE:Internal infill\n" + self.minValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:Solid infill\n", ";TYPE:Solid infill\n" + self.minValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:Bridge infill\n", ";TYPE:Bridge infill\n" + self.minValueLA + "\n")
        tempBuffer[1] = tempBuffer[1].replace(";TYPE:Skirt/Brim\n", ";TYPE:Skirt/Brim\n" + self.minValueLA + "\n")
        self._fileBuffer = "".join(tempBuffer)

if __name__ == "__main__":
    try:
        slicerArgument = str(sys.argv[2]).lower()
        print(str(sys.argv[1]))
        print(slicerArgument)

        if(slicerArgument == "-s3d"):
            do_file = SimplifyLinearAdvance(str(sys.argv[1]))
        elif(slicerArgument == "-ps"):
            do_file = PrusaSlicerLinearAdvance(str(sys.argv[1]))
        else:
            print("Error in slicer argument")
            print("Args is " + str(sys.argv))
            # print("Arg 2 is " + slicerArgument)
            sys.exit(0)
        newFilename = do_file.automatic_work()
        print("Success " + newFilename)
    except FileExistsError:
        print("Uncorrect name")
    except Exception as e:
        print(str(e))