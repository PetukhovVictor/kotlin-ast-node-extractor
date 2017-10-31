import os
import json

class AstWriter:
    @staticmethod
    def write(path, filename, nodes):
        basename = os.path.basename(filename)
        dirname = path + '/' + os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        f = open(dirname + '/' + basename, 'w')
        nodes = json.dumps(nodes)
        f.write(nodes)
        f.close()
