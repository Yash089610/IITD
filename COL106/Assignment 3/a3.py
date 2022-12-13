class PointDatabase:
    class Node:
        def __init__(self, val, tree, left, right, range):
            self.val = val
            self.tree = tree
            self.left = left
            self.right = right
            self.range = range

    def __init__(self, pointlist):
        pointlist.sort()
        self.treex = pointlist
        self.treey = sorted(pointlist, key=lambda x: x[1])
        if len(pointlist) > 0:
            self.root = self.buildtree(self.treex, self.treey)
        else:
            self.root = None
        # res = []
        # def inorderTraversal(root):
        #     if root:
        #         inorderTraversal(root.left)
        #         if root.left == root.right == None:
        #             res.append((root.val, root.tree))
        #         inorderTraversal(root.right)
        #     return res
        # print(inorderTraversal(root))

    def buildtree(self, px, py):
        if len(px) == 1:
            return self.Node(px[0][0], py, None, None, (px[0][0], px[0][0]))
        mid = len(px)//2
        val = px[mid]
        leftx = px[0:mid]
        rightx = px[mid:]
        lefty, righty = [], []
        for i in py:
            if i[0] < val[0]:
                lefty.append(i)
            else:
                righty.append(i)
        return self.Node(val[0], py, self.buildtree(leftx, lefty), self.buildtree(rightx, righty), (px[0][0], px[-1][0]))

    def query2(self, root, x, y):
        if not root:
            return []
        # print(x, y, root.val, root.range)
        if root.left == root.right == None:
            if x[1] >= root.tree[0][0] >= x[0] and y[1] >= root.tree[0][1] >= y[0]:
                return root.tree
            else:
                return []
        if root.range[1] < x[0] or root.range[0] > x[1]:
            return []
        elif root.val > x[1]:
            return self.query2(root.left, x, y)
        elif root.val <= x[0]:
            return self.query2(root.right, x, y)
        elif root.range[0] >= x[0] and root.range[1] <= x[1]:
            if root.tree[0][1] > y[1] or root.tree[-1][1] < y[0]:
                return []
            return self.bins(y, root.tree)
        else:
            if root.tree[0][1] > y[1] or root.tree[-1][1] < y[0]:
                return []
            return self.query2(root.left, x, y)+self.query2(root.right, x, y)

    def bins(self, y, l):
        mid = len(l)//2
        if len(l) == 1:
            if y[1] >= l[0][1] >= y[0]:
                return l
            else:
                return []
        if l[0][1] >= y[0] and l[-1][1] <= y[1]:
            return l
        elif l[-1][1] < y[0] or l[0][1] > y[1]:
            return []
        elif l[mid][1] > y[1]:
            return self.bins(y, l[:mid])
        elif l[mid][1] <= y[0]:
            return self.bins(y, l[mid:])
        else:
            return self.bins(y, l[:mid])+self.bins(y, l[mid:])

    def searchNearby(self, q, d):
        return self.query2(self.root, (q[0]-d, q[0]+d), (q[1]-d, q[1]+d))


# pointDbObject = PointDatabase([(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10),
#                                (9, 2), (10, 5)])

# # pointDbObject = PointDatabase([])
# print(pointDbObject.searchNearby((5, 5), 1))
# # []
# print(pointDbObject.searchNearby((4, 8), 2))
# # [(3, 7), (4, 9)]
# print(pointDbObject.searchNearby((10, 2), 1.5))
# # [(9, 2)]
