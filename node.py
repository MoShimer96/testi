class Node:
    def __init__(self, children=None):
        self.children = children if children is not None else []


def count_nodes_with_equal_subtrees(node):
    if not node.children:
        # Jos solmu on lehti, palautetaan 1
        return 1
    else:
        # Lasketaan kaikkien lasten alipuiden solmujen määrät
        child_subtree_sizes = [count_nodes_with_equal_subtrees(child) for child in node.children]
        
        # Tarkistetaan, ovatko alipuiden solmumäärät samat
        if all(count == child_subtree_sizes[0] for count in child_subtree_sizes):
            # Jos samat, lisätään tämä solmu mukaan laskentaan
            return 1 + sum(child_subtree_sizes)
        else:
            # Muuten jätetään tämä solmu laskennasta pois
            return sum(child_subtree_sizes)


tree = Node(children=[Node(children=[]), Node(children=[Node(children=[])])])

result = count_nodes_with_equal_subtrees(tree)
print(result)
