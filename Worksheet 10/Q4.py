import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
data = []
f = lambda x,a,b : np.exp(-a*x**2)/(x**2+b**2)
for i in (0,1,2):
    for j in (1,2,3):
        result = quad(f,-np.inf,np.inf,args=(i,j))
        data.append(result[0])
table = np.array_split(data,3)
df = pd.DataFrame(table,columns = ['1', '2', '3'],index=['0','1','2'])
print df