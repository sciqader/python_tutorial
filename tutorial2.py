##################################################
# In this tutorial we will generate random samples
# from a normal distribution (in numpy various
# distributions are implemented) and plot it in 
# a histogram
#
# example values: 
# mu, sig =0, .4  #  mean and std of the normal distr.
# sample_size = 10000 
#
# usage example:
# python3 tutorial2.py
#
##################################################


import numpy as np
import matplotlib.pyplot as plt

mu, sig, sample_size =0, 0.4, 10000 

sample = np.random.normal(mu, sig, sample_size) # generate a rand sample

count, bins, ignored = plt.hist(s, 100, density=True) # plot the histogram, bin number =100

plt.show()