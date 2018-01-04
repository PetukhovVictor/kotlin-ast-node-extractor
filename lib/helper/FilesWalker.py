from os import path
import glob

from .TimeLogger import TimeLogger


class FilesWalker:
    @staticmethod
    def walk(folder, callback, extension='json', log_text=None):
        time_logger = TimeLogger()

        for filename in glob.iglob(folder + '/**/*.' + extension, recursive=True):
            if path.isfile(filename):
                callback(filename)

        return time_logger.finish(task_name=log_text if log_text else 'Walking files in ' + folder + ' directory')
