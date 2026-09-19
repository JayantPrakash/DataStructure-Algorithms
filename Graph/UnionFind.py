class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.num_components = n
    def find(self,i):
        # using path compression
        if self.parent[i] == i:
            return i

        x = self.find(self.parent[i])
        #updating parent of every found node
        self.parent[i] = x

        return x

    def unionBySize(self,i,j):

        li = self.find(i)
        lj = self.find(j)

        if li == lj:
            return

        size_i = self.size[i]
        size_j = self.size[j]

        if size_i >= size_j:
            self.parent[lj] = li
            self.size[i] += self.size[j]

        else:
            self.parent[li] = lj
            self.size[j] += self.size[i]

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