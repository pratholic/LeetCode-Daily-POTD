from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def check(mid):
            dsu = DSU(n)
            optional = []
            upgrades = 0

            for u, v, s, must in edges:
                if must == 1: # jo edge must hai, unko include kardo jo mid ko satisfy kare
                    if s < mid:
                        return False

                    if dsu.findUPar(u) == dsu.findUPar(v): # yeh edge pehle aa gaya hai, vapis se aaya means cycle create karega
                        return False

                    dsu.union(u, v)

                else:
                    optional.append((u, v, s)) # yeh must = 0 wale edges

            
            for u, v, s in optional:
                if s >= mid: # jo optional edges hai, agar vo bhi mid ko satisfy kare toh include karlo
                    dsu.union(u, v)

            for u, v, s in optional:
                if s < mid and 2 * s >= mid: # jaha pe upgrade charge hai, vaha if same component hai, toh rhne do else karlo add
                    
                    if dsu.findUPar(u) == dsu.findUPar(v):
                        continue

                    upgrades += 1
                    dsu.union(u, v)

                    if upgrades > k: # more than k upgrades hogye, which is not allowed
                        return False

            root = dsu.findUPar(0)
            for node in range(1, n): # yaha pe hum check kar rhe hai, ki saare nodes same component mein hai na
                if dsu.findUPar(node) != root:
                    return False

            return True

        
        low = 0
        high = max(2 * s for u, v, s, m in edges)
        ans = -1

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans