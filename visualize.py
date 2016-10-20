import sys, os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from importclass import testclass

abspath = '/Users/sandre/Desktop/variational_code/optimal_solver/DATA/'
inst1 = testclass(abspath)
inst1.filetype('0_')

inst1.indexvalue(100)
inst1.getparams()
print(inst1.params)
inst1.construct_grid()
inst1.plot_tempstream()

