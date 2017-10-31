class AstNodeExtractor:
    def __init__(self, root, target):
        self.root = root
        self.target = target

    def extract(self):
        return self._walk(self.root, [], self.target)

    def _walk(self, node, target_nodes, target):
        if node['type'] == target:
            target_nodes.append(node)
        else:
            if 'children' in node:
                for child_node in node['children']:
                    target_nodes = self._walk(child_node, target_nodes, target)

        return target_nodes
