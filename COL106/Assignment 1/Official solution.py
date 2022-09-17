class Stack:
    def __init__(self):
        """
        constructor method for stack class
        capacity: initial capacity for the stack
        container: conatins values stored in the stack
        size: class variable storing the current size of the stack
        """
        self.capacity = 100000
        self.container = [0] * self.capacity
        self.size = 0
    
    def size(self):
        """
        returns the current size of the stack
        """
        return self.size

    def push(self, val):
        """
        adds an element to the top of the stack in O(1)
        Args:
        val: value to be pushed
        """
        if(self.size == self.capacity):
            # if the stack has reached its current maximum capacity,
            # resize the stack to double its current capacity
            temp = self.container
            self.capacity = 2 * self.capacity
            self.container = [0] * self.capacity
            for i in range(0, self.size):
                self.container[i] = temp[i]
    
        self.container[self.size] = val
        self.size = self.size + 1


    def pop(self):
        """
        removes and returns the top element of stack in O(1)
        """
        self.size = self.size - 1
        return self.container[self.size]
    
    def top(self):
        """
        returns the top element of the stack in O(1)
        """
        return self.container[self.size - 1]
    
def update_top1(st, d):
    """
    increments the top element of the stack by d
    Args:
    st: stack object
    d: the amount by which the top element needs to be incremented
    """
    top_ele = st.pop()
    st.push(top_ele + d)

def update_top3(st, dx, dy, dz):
    """
    increments the top element (3-tuple) of the stack by (dx,dy,dz)
    Args:
    st: stack object
    dx: the amount by which the first element of the tuple needs to be incremented
    dy: the amount by which the second element of the tuple needs to be incremented
    dz: the amount by which the third element of the tuple needs to be incremented
    """
    top_ele = st.pop()
    st.push([top_ele[0] + dx, top_ele[1] + dy, top_ele[2] + dz])

def findPositionandDistance(s):
    """
    At any point in the iteration:
    i) top of positions stack contains the position of the drone had it started at origin on accepting the latest special instruction
    ii) top of distances stack contains the distance travelled by the drone after accepting the latest special instruction
    iii) top of multiplier stack contains the number of times the program within the latest special instruction needs to repeated

    Note that, before receiving any special instruction:
    i) positions stack contains just one element which is the actual position of the drone 
    ii) distance stack also contains just one element which is the actual distance travelled by the drone
    iii) multiplier stack is empty
    """

    # initialization of stack objects
    positions = Stack()
    distances = Stack()
    multiplier = Stack()
    positions.push([0,0,0])
    distances.push(0)

    i = 0
    while(i < len(s)):
        # we read each character of the given string
        if(s[i] == '('):
            positions.push([0,0,0])
            distances.push(0)
            i = i + 1
        elif(s[i] >= '0' and s[i] <= '9'):
            # reads the current multiplier
            curr_multiplier = ""
            while(s[i] >= '0' and s[i] <= '9'):
                curr_multiplier = curr_multiplier + s[i]
                i = i + 1
            multiplier.push(int(curr_multiplier))
        elif(s[i] == ')'):
            # by the time we reach ')', we have already process the string between the parenthesis
            # the amount by which positions and distance need to be incremented due to the string 
            # processed between current parenthesis lies on the top of the positions and distance
            # stack. We multiply these by the multiplier and update the stacks. 
            last_pos = positions.pop()
            last_mult = multiplier.pop()
            last_pos = [coor * last_mult for coor in last_pos]
            update_top3(positions, last_pos[0], last_pos[1], last_pos[2])

            last_dist = distances.pop()
            update_top1(distances, last_mult * last_dist)
            i = i + 1
        else:
            if(s[i] == '+'):
                i = i + 1
                # distance travelled incremented since X,Y,Z all correspond to unit distance
                update_top1(distances, 1)
                if(s[i] == 'X'):
                    # positive X denotes unit increment of first coordinate
                    update_top3(positions, 1, 0, 0)
                elif(s[i] == 'Y'):
                    update_top3(positions, 0, 1, 0)
                elif(s[i] == 'Z'):
                    update_top3(positions, 0, 0, 1)
            elif(s[i] == '-'):
                i = i + 1
                update_top1(distances, 1)
                if(s[i] == 'X'):
                    update_top3(positions, -1, 0, 0)
                elif(s[i] == 'Y'):
                    update_top3(positions, 0, -1, 0)
                elif(s[i] == 'Z'):
                    update_top3(positions, 0, 0, -1)
            i = i + 1
    ans = positions.top()
    ans.append(distances.top())
    return ans