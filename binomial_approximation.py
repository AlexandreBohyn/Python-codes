import numpy as np;
import matplotlib.pyplot as plt;

# Define parameter values
n = 10;
p = 0.5;
xvec = (np.linspace(10,5000,100)).tolist();

y = [];

# Compute mean
np.random.seed(795920)
for x in xvec:
   temp = np.mean(np.random.binomial(n,p,int(x)))
   y.append(temp)

# Plot the results
fig, ax = plt.subplots()
ax.plot(xvec, y)
ax.hlines(y=5, xmin=0, xmax=5000, linewidth=1, linestyles= "dashed", color='r')
ax.legend(['Approximation', 'True value']);
plt.xlabel('Number of iterations');
plt.ylabel('Value');
plt.title('Binomial approximation')
plt.show();
