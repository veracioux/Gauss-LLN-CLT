import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np; from numpy import *
from shared import *
from gauss import *

def plot_binomial(n, approx='Auto'):
    k = range(n+1)
    pmf = stats.binom.pmf(k, n, 0.5) # Generisanje raspodjele
    
    ax = plt.axes()
    import matplotlib.ticker as tck
    ax.xaxis.set_major_locator(tck.MaxNLocator(integer=True)) #Estetika
    
    if approx == 'True' or (approx == 'Auto' and n > 10):
        plt.plot(stats.norm.pdf(k, n/2, sqrt(n)/2),
                 c='orangered', label='De Moivre-\nLaplace')
    plt.stem(pmf, basefmt=' ', label='$p_K(k)$')
        
    # Anotacija
    plt.xlabel('$k$')
    plt.legend(loc='upper right', bbox_to_anchor=(0.99,0.92), framealpha=1)

def plot_fun(f):
    plt.plot(arange(-50, 50), f)
    plt.yticks([], [])
    plt.tight_layout()
    plt.xlabel('$x$'); plt.ylabel('$f(x)$')
    
def plot_convolution(f, n):
    # Formiranje normalizovane konvolucije
    g = convolve_n(f, n)
    g = g / sum(g)
    
    # Formiranje ulazne varijable
    N = len(g)
    x = array(range(N)) - N/2
    
    # Aproksimacija Gauss-ovom funkcijom
    g_approx = approx_gaussian(x, g)
    
    # Plot
    plt.plot(x, g, label='Konvolucija');
    plt.plot(x, g_approx, label='Aproksimacija')
    # Anotacija i estetika
    plt.yticks([], [])
    plt.xlabel('$x$'); plt.ylabel('$g(x)$'); plt.legend()
    
