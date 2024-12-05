import matplotlib as mpl
import numpy as np

def get_rgba(intensity, character, data_max, lim=1.0, power=1.0):
    cmap = mpl.cm.get_cmap('gist_heat_r')
    red = cmap(np.power(intensity/data_max*lim, power))
    blue = red[:,:,[2,1,0,3]]
    rgba = (1-character)[:,:,None]*red+(character[:,:,None])*blue
    return red, blue, rgba

def get_rgba_three(intensity, character, data_max, lim=1.0, power=1.0):
    cmap = mpl.cm.get_cmap('gist_heat_r')
    red = cmap(np.power(intensity/data_max*lim, power))
    blue = red[:,:,[2,1,0,3]]
    green = red[:,:,[1,0,2,3]]
    rgba = (character)[:,:,0,None]*red+(character[:,:,1,None])*green+(character[:,:,2,None])*blue
    return red, green, blue, rgba