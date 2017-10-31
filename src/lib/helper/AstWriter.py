import json

class AstWriter:
    @staticmethod
    def write(filename, nodes):
        f = open(filename, 'w')
        nodes = json.dumps(nodes)
        f.write(nodes)
        f.close()
