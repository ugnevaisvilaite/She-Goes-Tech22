# TODO
# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course


import matplotlib.pyplot as plt


plt.style.use('_mpl-gallery')


x = list(range(-10, 11))
y = [(n+5)**3 for n in x]

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=1.0)


plt.show()