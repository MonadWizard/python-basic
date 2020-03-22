"""
"Sine, cos, tan,cot,sec,cosec  Function" are some special function on numpy
"exponential function(e^x)" "logarithmic function(logx)" are also some special function on numpy
"""

import numpy as np
import matplotlib.pyplot as plt

print("""
----------------------------trikonomitic function graph-------------------
""")
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)

y1 = np.cos(x)

y3 = np.tan(x)

plt.plot(x,y)
plt.show()

plt.plot(x,y1)
plt.show()

plt.plot(x,y3)
plt.show()



print("""
------------------------------exponential function-----------------------
""")

ar = np.array([1,2,3,4])
print(np.exp(ar))



print("""
------------------------------logarithmic function-----------------------
""")
print(np.log(ar))

print("""

""")
















