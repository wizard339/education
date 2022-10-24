import sys


class OptimalBST:
    def __init__(self, p: list, q: list):
        self.p = p
        self.q = q
        self.n = len(p)
        self.root = [[0 for i in range(self.n + 1)] for j in range(self.n + 1)]

    def optimal_bst(self) -> tuple:
        e = [[self.q[i - 1] for i in range(1, self.n + 2)] for j in range(self.n + 2)]
        w = [[self.q[i - 1] for i in range(1, self.n + 2)] for j in range(self.n + 2)]

        for lnt in range(1, self.n + 1):

            for i in range(1, self.n - lnt + 2):
                j = i + lnt - 1
                e[i][j] = sys.maxsize
                w[i][j] = round((w[i][j - 1] + self.p[j - 1] + self.q[j]), 2)

                for r in range(i, j + 1):
                    t = round((e[i][r - 1] + e[r + 1][j] + w[i][j]), 2)

                    if t < e[i][j]:
                        e[i][j] = t
                        self.root[i][j] = r
        return e, self.root

    def construct_obst(self, root: list) -> str:
        k = self.root[1][self.n]
        print(f"k[{k}] is the root")
        left, right = [(1, k - 1)], [(k + 1, self.n)]
        p = [k]
        
        while p:
            
            if left:
                i, j = left.pop(0)
                
                if j < i:
                    print(f"d[{j}] is the left child of k[{p[0]}]")
                else:
                    k = self.root[i][j]
                    print(f"k[{k}] is the left child of k[{p[0]}]")
                    p[:0] = [k]
                    left.insert(0, (i, k - 1))
                    right.insert(0, (k + 1, j))
                    
            else:
                i, j = right.pop(0)
                
                if j < i:
                    print(f"d[{j}] is the right child of k[{p.pop(0)}]")
                else:
                    k = self.root[i][j]
                    print(f"k[{k}] is the right child of k[{p.pop(0)}]")
                    p[:0] = [k]
                    left.insert(0, (i, k - 1))
                    right.insert(0, (k + 1, j))        


if __name__ == '__main__':
    p = [.15, .10, .05, .10, .20]
    q = [.05, .10, .05, .05, .05, .10]
    obst = OptimalBST(p, q)
    root = obst.optimal_bst()[1]
    print(root)
    print(obst.construct_obst(root))
