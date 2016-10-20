import numpy as np

class Dog:
    def __init__(self,name):
        self.name = name

class testclass:
    """This class tests the class structure and imports proper thigngs"""
    def __init__(self, impdir):
        self.impdir = impdir #path to the data directory
        self.ftype = ' '     #name of fyletype
        self.xdim = 0  #the number of gridpoints in the x-direction
        self.zdim = 0  #the number of gridpoints in the z-direction
        self.mu = 0   #the value of mu where things where computed
        self.resid = 0 #the residual of the optimality condition
        self.pec1 = 0  #the peclet number computed via \|\nalba \vec{u} \|^2
        self.pec2 = 0  #the peclet number computed via the optimality condition
        self.nu1 = 0   #the nusselt number computed via <sum, w>
        self.nu2 = 0   #the nusselt number computed via the optimality condition
        self.asp = 0   #the aspect ratio of the domain
        self.index = 0 # the import index
        self.dt = 0    # size of timesteps being computed
        self.params = []
    def filetype(self, ftype):
        self.ftype = ftype
    def indexvalue(self, index):
        self.index = index
    def getparams(self):
        path = self.impdir + self.ftype + str(self.index) + '_params.txt'
        self.params = np.loadtxt(open(path,'r'))
        
    def explain_params():
        
        
    
