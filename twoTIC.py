import matplotlib as mpl
import numpy as np

def get_rgba(intensity, character, data_max, lim=1.0, power=1.0):
    cmap = mpl.cm.get_cmap('gist_heat_r')
    red = cmap(np.power(intensity/data_max*lim, power))
    blue = red[:,:,[2,1,0,3]]
    rgba = (1-character)[:,:,None]*red+(character[:,:,None])*blue
    return red, blue, rgba