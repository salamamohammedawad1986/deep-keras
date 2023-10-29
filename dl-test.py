import pandas as pd
import numpy as np



print('salama')

def odd_even():
    for num in np.arange(2,10):
        if(num %2) == 0:
            print('Even :', num)
        else:
            print('Odd:', num)   

odd_even()        