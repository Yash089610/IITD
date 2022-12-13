class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.ylist = []
        self.xlist = []


def Build2DTree(L: list):  # L is sorted list
    if len(L) == 1:
        t = Node(L[0])
        t.ylist.append(L[0])
        t.xlist.append(L[0])
        return t
    else:
        start = 0
        end = len(L) - 1
        mid = (start+end)//2
        L_left = L[:mid+1]  # Change in 1D
        L_right = L[(mid+1):]
        tree = Node(L[mid])
        t_left = Build2DTree(L_left)
        t_right = Build2DTree(L_right)
        tree.left = t_left
        tree.left.parent = tree
        tree.right = t_right
        tree.right.parent = tree
        if tree.left != None:
            ylist_left = tree.left.ylist
            xlist_left = tree.left.xlist
        if tree.right != None:
            ylist_right = tree.right.ylist
            xlist_right = tree.right.xlist
        i, j = 0, 0
        list_ylist = []
        list_xlist = []
        while i < len(ylist_left) and j < len(ylist_right):
            if ylist_left[i][1] < ylist_right[j][1]:
                list_ylist.append(ylist_left[i])
                i += 1
            else:
                list_ylist.append(ylist_right[j])
                j += 1
        a, b = 0, 0
        while a < len(xlist_left) and b < len(xlist_right):
            if xlist_left[a][0] < xlist_right[b][0]:
                list_xlist.append(xlist_left[a])
                a += 1
            else:
                list_xlist.append(xlist_right[b])
                b += 1

        list_ylist = list_ylist + ylist_left[i:]+ylist_right[j:]
        list_xlist = list_xlist + xlist_left[a:]+xlist_right[b:]
        tree.ylist = tree.ylist+list_ylist
        tree.xlist = tree.xlist+list_xlist
        return tree


def Query1D(ylist, y1, y2):
    finallist = []
    start = 0
    end = len(ylist)-1
    if(ylist[end][1] < y1 or ylist[start][1] > y2):
        return finallist

    while(start < end):
        mid = (start+end)//2
        if(ylist[mid][1] < y1):
            start = mid+1
        else:
            end = mid

    index1 = start

    start = 0
    end = len(ylist)-1
    while(start < end):
        mid = (start+end)//2
        if(ylist[mid+1][1] <= y2):
            start = mid+1
        else:
            end = mid

    index2 = start

    for i in range(index1, index2+1):
        finallist.append(ylist[i])

    return finallist


def Query2D(tree: Node, x1, x2, y1, y2):
    l = []
    if tree.left == None and tree.right == None:
        if tree.data[0] >= x1 and tree.data[0] <= x2 and tree.data[1] >= y1 and tree.data[1] <= y2:
            l.append(tree.data)
            return l
        else:
            return l
    rx1 = tree.xlist[0][0]
    rx2 = tree.xlist[-1][0]
    if rx1 >= x1 and rx2 <= x2:
        l = l + Query1D(tree.ylist, y1, y2)
    else:
        l = l+Query2D(tree.left, x1, x2, y1, y2) + \
            Query2D(tree.right, x1, x2, y1, y2)
    return l


class PointDatabase:
    def __init__(self, pointlist: list):
        if len(pointlist) == 0:
            self.tree = Node(None)
        else:
            self.list = pointlist
            self.list.sort()
            self.tree = Build2DTree(self.list)

    def searchNearby(self, q, d):
        if self.tree.data == None:
            return []
        x1 = q[0]-d
        x2 = q[0]+d
        y1 = q[1]-d
        y2 = q[1]+d
        l = []
        l = l + Query2D(self.tree, x1, x2, y1, y2)
        return l


# pointDbObject = PointDatabase(
#     [(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10), (9, 2), (10, 5)])
# print(pointDbObject.searchNearby((5, 5), 1))
# print(pointDbObject.searchNearby((4, 8), 2))
# print(pointDbObject.searchNearby((10, 2), 1.5))
