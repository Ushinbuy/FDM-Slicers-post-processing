#!/usr/bin/env python3

from pathlib import Path
debug = False

class GcodeFileHandler:
    maxValueLA = ""
    minValueLA = ""

    def __init__(self, filename) -> None:
        self.__fileName = filename

    @property
    def property_filename(self):
        return self.__fileName

    @property_filename.setter
    def property_filename(self, filename):
        print(filename)
        self.__fileName = filename

    def __checkPropertyIsEmpty(self):
        if self.__fileName is None:
            raise FileNotFoundError
        elif self._fileBuffer is None:
            raise BufferError

    def __readFileToFileBuffer(self):
        if self.__fileName is None:
            raise FileNotFoundError
        with open(self.__fileName, 'r') as file_to_read:
            self._fileBuffer = str(file_to_read.read())
        file_to_read.close()

    def __write_buffer2new_file(self):
        self.__checkPropertyIsEmpty()
        if(debug):
            new_filename = self.__fileName.replace(Path(self.__fileName).name, "Copy_" + Path(self.__fileName).name)
        else:
            new_filename = self.__fileName
        file_to_write = open(new_filename, 'wb')
        file_to_write.write(self._fileBuffer.encode())
        file_to_write.close()
        return new_filename

    def _searchLaValue(self):
        pass

    def _patchBuffer(self):
        pass

    def automatic_work(self):
        self.__readFileToFileBuffer()
        self._searchLaValue()
        self._patchBuffer()
        return self.__write_buffer2new_file()

    def uncorrectSlicerInArguments(self):
        print("Uncorrect slicer choosen")
        print("'-s3D'   for Simplify3D")
        print("'-ps'    for PrusaSlicer")
        raise ValueError