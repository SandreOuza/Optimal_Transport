import numpy as np
import matplotlib.pyplot as plt
import matplotlib


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
        self.dt1 = 0    # size of timesteps being computed, for the advec-diff
        self.dt2 = 0    # size of timesteps being computed, for the optimality condition
        self.params = []
    def filetype(self, ftype):
        self.ftype = ftype
    def indexvalue(self, index):
        self.index = index
    def getparams(self):
        path = self.impdir + self.ftype + str(self.index) + '_params.txt'
        self.params = np.loadtxt(open(path,'r'))
        self.mu = self.params[0] #this is epsilon for optimal_a? family
        self.asp = self.params[1]
        self.xdim = int(self.params[2])
        self.zdim = int(self.params[3])
        self.dt1 = self.params[4]
        self.dt2 = self.params[5]
        self.pec1 = self.params[6]
        self.nu1 = self.params[7]
        self.pec2 = self.params[8]
        self.nu2 = self.params[9]
        self.resid = self.params[10]
    def construct_grid(self):
        self.xgrid = np.linspace(0,self.asp - 1.0/self.xdim,self.xdim)
        self.zgrid = np.cos(np.linspace(0, np.pi, self.zdim))/2.0 + 0.5
        self.Xgrid, self.Zgrid = np.meshgrid(self.xgrid, self.zgrid)
    def import_field(self,field):
        path = self.impdir + self.ftype + str(self.index) + field + '.txt'
        self.field = np.loadtxt(open(path,'r'))
    def plot_tempstream(self):
        #other good colors for temp include plt.cm.coolwarm and
        print('Plotting assuming theta exists')
        matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
        path = self.impdir + self.ftype + str(self.index) + '_theta' + '.txt'
        tmp = np.loadtxt(open(path,'r'))
        thetafield = tmp.reshape(self.zdim, self.xdim)
        path = self.impdir + self.ftype + str(self.index) + '_stream' + '.txt'
        tmp = np.loadtxt(open(path,'r'))
        streamfield = tmp.reshape(self.zdim, self.xdim)
        pl1=plt.contourf(self.Xgrid, self.Zgrid, 1-self.Zgrid+0.5*thetafield, 513 , cmap = plt.cm.RdYlBu_r)
        plt.colorbar(pl1, shrink=0.8, extend='both')
        pl2=plt.contour(self.Xgrid, self.Zgrid, streamfield, 20, alpha=0.25, colors='k')
        plt.show()
    def plot_tempstream2(self):
        #other good colors for temp include plt.cm.coolwarm and
        print('Plotting assuming sum exists')
        matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
        #get sum
        path = self.impdir + self.ftype + str(self.index) + '_sum' + '.txt'
        tmp = np.loadtxt(open(path,'r'))
        sumfield = tmp.reshape(self.zdim, self.xdim)
        #get dif
        path = self.impdir + self.ftype + str(self.index) + '_dif' + '.txt'
        tmp = np.loadtxt(open(path,'r'))
        diffield = tmp.reshape(self.zdim, self.xdim)
        #get stream
        path = self.impdir + self.ftype + str(self.index) + '_stream' + '.txt'
        tmp = np.loadtxt(open(path,'r'))
        streamfield = tmp.reshape(self.zdim, self.xdim)
        #construct temp
        #self.mu is eps and this needs to be divided by 4 to correspond to a 1.0 z-direction domain
        #sumfield and diffield also need to be divided by two for the same reason
        #the average of sumfield and theta field is what corresponds to theta
        thetafield = 0.5*sumfield*np.sqrt(self.mu/4.0)
        tempfield = (thetafield+diffield*0.5)*0.5
        tempfield += 1.0-self.Zgrid
        pl1=plt.contourf(self.Xgrid, self.Zgrid, tempfield, 513 , cmap = plt.cm.RdYlBu_r)
        plt.colorbar(pl1, shrink=0.8, extend='both')
        #pl2=plt.contour(self.Xgrid, self.Zgrid, streamfield, 20, alpha=0.25, colors='k')
        plt.show()
    def family_options(self):
        print("----------------------------------------------------------------------------------")
        print("0: Family name '0_', Optimal Transport solution where the aspect ratio is maximized")
        print("1: Family name 'optimal_a0_', Optimal Transport solution with fundamental aspect ratio")
        print("2: Family name 'optimal_a1_', Optimal Transport solution with (fundamental aspect ratio)*2^{-1}")
        print("3: Family name 'optimal_a2_', Optimal Transport solution with (fundamental aspect ratio)*2^{-2}")
        print("4: Family name 'optimal_a3_', Optimal Transport solution with (fundamental aspect ratio)*2^{-3}")
        print("5: Family name 'optimal_a4_', Optimal Transport solution with (fundamental aspect ratio)*2^{-4}")
        print("6: Family name 'optimal_a5_', Optimal Transport solution with (fundamental aspect ratio)*2^{-5}")
        print("6: Family name 'optimal_a6_', Optimal Transport solution with (fundamental aspect ratio)*2^{-6}")
        print("7: Family name 'optimal_a7_', Optimal Transport solution with (fundamental aspect ratio)*2^{-7}")
        print("----------------------------------------------------------------------------------")
    def family_set(self, num):
        "Sets the ftype by using index values from family options. "
        if num==0:
            self.ftype = "0_"
        if num>0 and num<8:
            self.ftype = "optimal_a"+str(int(num))+"_"
        else:
            print('No such family. Check self.family_options for more options')

    def get_scalings(self, num1, num2):
        """Get the Nu-Pe scaligns from the params files over a range of indices """
        
        
    
