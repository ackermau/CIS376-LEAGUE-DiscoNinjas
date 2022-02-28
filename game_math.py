'''Game Math Library
@author YOUR NAMES
@date February 2022
Simple vector/matrix math functions
'''

import math as m

'''
Vector4 is the class all other vectors should inherit from.
You will use this vector most of the time in our engine.
That may not always be the most efficient way to calculate
things though!
'''
class Vector4:
    def __init__(self,x=0,y=0,z=0,w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    '''
    Return a string that represents the vector.  Probably somthing like <a, b, c, d>.
    '''
    def __repr__(self):
        print("<" + self.x + ", " + self.y + ", " + self.z + ", " + self.w + ">")

    '''
    Scale by a scalar value.
    Return a new vector.
    '''
    def scale(self, s):
        v = Vector4()
        v.x = self.x * s
        v.y = self.y * s
        v.z = self.z * s
        v.w = self.w
        return v
   

    '''
    Add a vector to a vector.
    Return the new Vector4 as a vector.
    '''
    def __add__(self, other):
        v  = Vector4()
        v.x = self.x + other.x
        v.y = self.y + other.y
        v.z = self.z + other.z
        if(self.w == 1 and other.w == 1):
            v.w = 0
        elif(self.w == 0 and other.w ==0):
            v.w = 0
        else:
            v.w = 1
        return v


    '''
    Subract a vector from a vector.
    Return the new Vector4 as a vector.
    '''
    def __sub__(self, other):
        v  = Vector4()
        v.x = self.x - other.x
        v.y = self.y - other.y
        v.z = self.z - other.z
        if(self.w == 1 and other.w == 1):
            v.w = 0
        elif(self.w == 0 and other.w == 0):
            v.w = 0
        else:
            v.w = 1
        return v

    
    '''
    Multiply a vector by a vector.
    '''
    def __mul__(self, s):
        scalar = self.x * s.x + self.y * s.y + self.z * s.z
        return scalar

    '''
    Calculate the vector magnitude.
    Return a scalar.
    '''
    def magnitude(self):
        mag = m.sqrt(self.x**2 + self.y**2 + self.z**2)
        return mag

    '''
    Return a normalized (magnitude 1) vector.
    Return a new Vector as always.
    '''
    def normalize(self):
        v = Vector4()
        mag = self.magnitude()
        v.x = self.x / mag
        v.y = self.y / mag
        v.z = self.z / mag
        v.w = self.w
        return v

    '''
    Calculate the cross product of this and another vector.
    Return a new vector.
    '''
    def cross(self, other):
        v = Vector4()
        v.x = self.y * other.z - self.z * other.y
        v.y = self.z * other.x - self.x * other.z
        v.z = self.x * other.y - self.y * other.x
        return v


    '''
    Check if the state of this vector and another are the same.
    Returns a boolean.
    '''
    def __eq__(self, other):
        if(self.w == other.w):
            return True
        return False


'''
Vector3
'''
class Vector3(Vector4):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0

'''
Vector2
'''
class Vector2(Vector3):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.z = 0
        self.w = 0

'''
Matrix defaults to a 4x4.  For out engine we don't need
much else.  Should work with variable sizes to make it more
flexible though.  Just make sure a calculcation is valid
before you try to do it.
'''
class Matrix:
    '''
    Setup the default state to be the identity matrix.
    '''
    def __init__(self, m=4, n=4):
        self.cols = m
        self.rows = n
        self.data = [self.cols] * self.rows
        self.data[0] = [ 1, 0, 0, 0]
        self.data[1] = [ 0, 1, 0, 0]
        self.data[2] = [ 0, 0, 1, 0]
        self.data[3] = [ 0, 0, 0, 1]


    '''
    Return a string representing this matrix.
    '''
    def __repr__(self):
        print("", self.data[0], "\n", self.data[1], "\n", self.data[2], "\n", self.data[3])

    '''
    Multiply this matrix by another (if possible).
    Return a new one.
    '''
    def __mul__(self, other):
        m = Matrix()
        m.data[0] = [0, 0, 0, 0]
        m.data[1] = [0, 0, 0, 0]
        m.data[2] = [0, 0, 0, 0]
        m.data[3] = [0, 0, 0, 0]
        if(self.cols == other.rows):
            for a in range(self.rows):
                for b in range(self.rows):
                    for c in range(self.rows):
                        m.data[a][b] += self.data[a][c] * other.data[c][b]
        return m

    
    '''
    Multiple a vector by this matrix.  Be sure to return a new vector.
    Feel free to only work with Vector4s for this one.
    '''
    def vec_mul(self, other):

        if(other == Vector4()):
            print("suc")
        dat = [0,0,0,0]
        temp = [0,0,0,0] 
        temp[0] = other.x
        temp[1] = other.y
        temp[2] = other.z
        temp[3] = other.w
        v = Vector4()
        for a in range(self.cols):
            for b in range(self.rows):
                dat[a] += self.data[b][a] * temp[b]
        v.x = dat[0]
        v.y = dat[1]
        v.z = dat[2]
        v.w = dat[3]
        return v 
