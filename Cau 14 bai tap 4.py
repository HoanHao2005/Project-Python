import numpy as np

a=np.arange(-5,6,1)
top = 3
bot = -3
a[a>top]=top
a[a<bot]=bot
print(a)