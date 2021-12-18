import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.animation as animation

def render(model): # since model is object, need to unpack it into numpy to plot it
    agent_genders = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        if cell_content:
            cell_content = cell_content.gender
        else:
            cell_content = 2
        agent_genders[x][y] = cell_content

    return agent_genders

def update(frameNum, img, model): # frameNum is a parameter for FuncAnimation
    if model.running:
        model.step()
    img.set_data(render(model))
    return img

def animate(model):
    cmap = colors.ListedColormap(['blue', 'red', 'white'])
    formatter = plt.FuncFormatter(lambda val, loc: ['Male', 'Female', 'Empty'][loc])
    
    fig, ax = plt.subplots()
    img = ax.imshow(render(model), cmap=cmap)
    fig.colorbar(img, ticks=[0,1,2], format=formatter, ax=ax)
    ax.axis('off')
    
    plt.close()
    
    ani = animation.FuncAnimation(fig,
                                  update,
                                  fargs=(img, model,),
                                  frames=200, # number of iterations
                                  interval=500,
                                  save_count=500)
    return ani