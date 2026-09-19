class UnionFind:
    # Initially each element leads its own singleton set; component count starts at n.
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.num_components = n
    # A representative is a root whose parent is itself; all members of a set share that root.
    def find(self,i):
        if self.parent[i] == i:
            return i

        x = self.find(self.parent[i])
        # Path compression redirects this node straight to the root, speeding up later finds.
        self.parent[i] = x

        return x

    # Find both roots first; merging only different roots preserves the partition of elements.
    def unionBySize(self,i,j):

        li = self.find(i)
        lj = self.find(j)

        # A redundant union changes neither the parent structure nor the component count.
        if li == lj:
            return

        # This version reads and updates sizes at i/j rather than roots li/lj.
        # Connectivity still merges roots, but size metadata can be wrong, so the usual size-balancing guarantee does not apply.
        size_i = self.size[i]
        size_j = self.size[j]

        if size_i >= size_j:
            self.parent[lj] = li
            self.size[i] += self.size[j]

        else:
            self.parent[li] = lj
            self.size[j] += self.size[i]

        # One successful merge replaces two components with one.
        self.num_components -= 1

def main():
    n = 5
    edges = [[0, 1], [2, 3], [0, 4]]
    unionFind = UnionFind(n)

    # Perform union operations
    for edge in edges:
        unionFind.unionBySize(edge[0], edge[1])

    # Print the representative of each element after unions
    for i in range(n):
        print("Element {}: Representative = {}".format(i, unionFind.find(i)))
    print("Components::", unionFind.num_components)


main()
"""
T(n) = O(n)
S(n) = O(n)
"""