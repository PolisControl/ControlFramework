import numpy as np 

class Simulation:
    def __init__(self, type):
        self.type = type
    
    def wrongtype(self, array):
        if not(isinstance(array, np.ndarray)):
            return True
        else:
            return False

    def State_Space(self, A, B, C, D):
        if self.wrongtype(A) or self.wrongtype(B) or self.wrongtype(C) or self.wrongtype(D):
            raise TypeError

        self.A = A
        self.B = B
        self.C = C
        self.D = D
    
    def Euler(self, x0, u, h):
        x_1 = self.A*x0 + self.B*u
        x = x0 + x_1*h
        y_1 = self.C*x + self.D*u
        return x, y_1

    def numericalIV(self, start, end, method, npts, input):    
        
        if method == "Euler":
            x =  np.zeros([self.A.shape[0], 1], dtype = float)
            y =  np.zeros([self.C.shape[0], 1], dtype = float)
            xt = np.array([x])
            yt = np.array([y])
            time = np.array([0])
            k = 0
            for timer in np.linspace(start, end, npts):
                time = np.append(time, timer)
                h = (end-start)/npts
                xi, yi = self.Euler(xt[k], input, h)
                xt = np.append(xt, xi)
                yt = np.append(yt, yi)