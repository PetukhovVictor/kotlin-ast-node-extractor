from os import path
import glob

from .TimeLogger import TimeLogger

class FilesWorker:
    @staticmethod
    def walk(folder, callback, extension='json', is_measure_time=True):
        if is_measure_time:
            time_logger = TimeLogger()

        for filename in glob.iglob(folder + '/**/*.' + extension, recursive=True):
            if path.isfile(filename):
                callback(filename)

        if is_measure_time:
            return time_logger.finish()
