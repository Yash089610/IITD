# Algorithm :
# (a) Sort the pointlist in terms of x co-ordinate, now only this x-sorted list will be used for all further
#  considerations. This pre-computation takes O(nlogn).
# (b) Construct a segment tree for sub-intervals which stores sorted list in y co-ordinate for these sub-intervals at each
#  node of the tree(which is represented by a sorted list and an interval).
# Pre-computations end here.
# (c) Now for each query,in the x-sorted array find the range of x which satisfies the distance condition with the
# reference co-ordinate, which would just be two iterators at the ends of the list.
# (d) We find the sub-intervals in the segment tree which would contruct the above found x-range interval, there will be
# O(logn) such sub-intervals, and as each of these intervals are sorted in y, we do binary search in these sub-intervals
# which is O(logn), thus we get m points in O(m + (logn)2), which is the required complexity.
import time


class Node:
    # This Class stores a tuple and a list, this list is the sorted list in y co-ordinate(in context with this assignment)
    # for the interval represented by the tuple.
    def __init__(self, tup, lst, left=None, right=None):
        self.tuple = tup
        self.sort = lst
        self.left = left
        self.right = right


class PointDatabase:
    def __init__(self, pointlist):
        pointlists = [None]*len(pointlist)
        # to avoid usage of tuples, which cause issue in assignment and copying.
        for i in range(len(pointlist)):
            pointlists[i] = list(pointlist[i])
        if (len(pointlists) == 0):  # taking into account an edge case.
            self.sort_x = []
            self.segment_tree_y = Node(None, None)
        else:
            self.sort(pointlists)
            self.sort_x = pointlists.copy()
            self.segment_tree_y = self.segment_tree(pointlists)

    def sort(self, lst):
        def Merge_Sort(lst, l, r):
            mid = int((l+r)/2)
            if (l != r):
                Merge_Sort(lst, l, mid)
                Merge_Sort(lst, mid+1, r)
                Merge(lst, l, mid, r)
            return

        def Merge(lst, l, mid, r):
            a = lst[l:mid+1]
            b = lst[mid+1:r+1]
            i = 0
            j = 0
            k = l
            while (i < mid+1-l) and (j < r-mid):
                if (a[i] < b[j]):
                    lst[k] = a[i]
                    k += 1
                    i += 1
                else:
                    lst[k] = b[j]
                    k += 1
                    j += 1
            while (i < mid-l+1):
                lst[k] = a[i]
                k += 1
                i += 1
            while (j < r-mid):
                lst[k] = b[j]
                k += 1
                j += 1
        Merge_Sort(lst, 0, len(lst)-1)
        return

    def search_min_x(self, x):
        lst = self.sort_x

        def search_min_help(lst, l, r, x):
            mid = int((l+r+1)/2)
            if (lst[mid][0] < x):
                if (mid == len(lst)-1):
                    return -1
                else:
                    return search_min_help(lst, mid+1, r, x)
            else:
                if (mid == 0):
                    return mid
                elif (lst[mid-1][0] < x):
                    return mid
                else:
                    return search_min_help(lst, l, mid-1, x)
        return search_min_help(lst, 0, len(lst)-1, x)

    def search_max_x(self, x):
        lst = self.sort_x

        def search_max_help(lst, l, r, x):
            mid = int((l+r+1)/2)
            if (lst[mid][0] > x):
                if (mid == 0):
                    return -1
                else:
                    return search_max_help(lst, l, mid-1, x)
            else:
                if (mid == len(lst)-1):
                    return len(lst)-1
                elif (lst[mid+1][0] > x):
                    return mid
                else:
                    return search_max_help(lst, mid+1, r, x)
        return search_max_help(lst, 0, len(lst)-1, x)

    def segment_tree(self, lst):
        def Merge_Sort(lst, l, r):
            mid = int((l+r)/2)
            if (l == r):
                a = lst[l:l+1]
                node = Node((lst[l], lst[l]), a)
                return node
            else:
                left = Merge_Sort(lst, l, mid)
                right = Merge_Sort(lst, mid+1, r)
                Merge(lst, l, mid, r)
                a = lst[l:r+1]
                node = Node((lst[l], lst[r]), a, left, right)
                return node

        def Merge(lst, l, mid, r):
            a = lst[l:mid+1]
            b = lst[mid+1:r+1]
            i = 0
            j = 0
            k = l
            while (i < mid+1-l) and (j < r-mid):
                if (a[i][1] < b[j][1]):
                    lst[k] = a[i]
                    k += 1
                    i += 1
                else:
                    lst[k] = b[j]
                    k += 1
                    j += 1
            while (i < mid-l+1):
                lst[k] = a[i]
                k += 1
                i += 1
            while (j < r-mid):
                lst[k] = b[j]
                k += 1
                j += 1
            return lst[l:r+1]
        root = Merge_Sort(lst, 0, len(lst)-1)
        return root

    # def range_interval_x(self,tup,d):
    #     lower = tup[0] - d
    #     upper = tup[0] + d
    #     lower_index = self.search_min_x(lower)
    #     upper_index = self.search_max_x(upper)
    #     if(lower_index == -1) or (upper_index == -1):
    #         return None
    #     else:
    #         return (lower_index,upper_index)

    def check_interval(self, range, range_check):
        # 1 tree interval completlty contains x correct interval
        # 0 tree interval is partially contained in x correct interval
        # -1 tree interval is completly outside x correct interval
        # 2 tree interval is completly inside x correct interval
        if (range_check[0] < range[0]):
            if (range_check[1] < range[0]):
                return -1
            else:
                if (range_check[1] > range[1]):
                    return 1
                else:
                    return 0
        else:
            if (range_check[0] > range[1]):
                return -1
            else:
                if (range_check[1] > range[1]):
                    return 0
                else:
                    return 2

    def tree_traverse(self, tup, d):
        def search_min_y(lst, y):
            def search_min_help(lst, l, r, y):
                mid = int((l+r+1)/2)
                if (lst[mid][1] < y):
                    if (mid == len(lst)-1):
                        return -1
                    else:
                        return search_min_help(lst, mid+1, r, y)
                else:
                    if (mid == 0):
                        return mid
                    elif (lst[mid-1][1] < y):
                        return mid
                    else:
                        return search_min_help(lst, l, mid-1, y)
            return search_min_help(lst, 0, len(lst)-1, y)

        def search_max_y(lst, y):
            def search_max_help(lst, l, r, y):
                mid = int((l+r+1)/2)
                if (lst[mid][1] > y):
                    if (mid == 0):
                        return -1
                    else:
                        return search_max_help(lst, l, mid-1, y)
                else:
                    if (mid == len(lst)-1):
                        return len(lst)-1
                    elif (lst[mid+1][1] > y):
                        return mid
                    else:
                        return search_max_help(lst, mid+1, r, y)
            return search_max_help(lst, 0, len(lst)-1, y)

        range_x = (self.sort_x[0], self.sort_x[len(self.sort_x)-1])
        root = self.segment_tree_y
        ans = []
        if (range_x == None):
            return ans

        def tree_traverse_help(ans, root, tup, d):
            lower_y = tup[1] - d
            upper_y = tup[1] + d
            if (self.check_interval(range_x, root.tuple) == 1) or (self.check_interval(range_x, root.tuple) == 0):
                if (root.left):
                    tree_traverse_help(ans, root.left, tup, d)
                if (root.right):
                    tree_traverse_help(ans, root.right, tup, d)
                return
            elif (self.check_interval(range_x, root.tuple) == -1):
                return
            else:
                lower_index = search_min_y(root.sort, lower_y)
                upper_index = search_max_y(root.sort, upper_y)
                if (lower_index != -1) and (upper_index != -1):
                    i = lower_index
                    while (i < upper_index + 1):
                        ans.append(tuple(root.sort[i]))
                        i += 1
                return
        tree_traverse_help(ans, root, tup, d)
        return ans

    def searchNearby(self, tup, d):
        if (self.sort_x == []):
            return []
        return self.tree_traverse(tup, d)


# pointDbObject = PointDatabase(
#     [(2, 4), (9, 2), (5, 1), (7, 8), (3, 7), (10, 5), (4, 9), (8, 10), (1, 6), (6, 3)])
# start_time = time.time()
# # pointDbObject = PointDatabase([])
# print(pointDbObject.searchNearby((5, 5), 3))
# print(pointDbObject.searchNearby((4, 8), 2))
# print(pointDbObject.searchNearby((10, 2), 1.5))
# print(time.time() - start_time)
