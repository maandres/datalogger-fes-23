import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from plotly.offline import plot

#inicializar la gràfica
fig, ax = plt.subplots()
#Dades x i y
xdata, ydata = [], []
#ro, son els punts vermells per mostrar a la gràfica
ln, = ax.plot([], [], 'ro')

#limits eix x i eix y
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

#Funció per actualitzar els punts
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

#part de la gràfica
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()

#how to pass data grphic python to html page
#hem de mostrar les dades al html
#plot(fig, filename='grafico.html')
