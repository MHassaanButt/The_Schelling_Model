## The Schelling Model
### The Schelling model of segregation is an agent-based model that elucidates how individual preferences for neighbours might result in segregation. When agents represent householders who relocate to the city, the model is particularly efficient for studying ethnic group residential segregation. 


## Environment Requirements

* python version => 3.9+

* pip => 19.0.1
* Jupyter Notebook
* Anaconda/Miniconda (If you are using conda enviroment for installation of libraires)

## Required Libraires:

* Numpy
* math
* random
* matplotlib
* scipy.spatial 

## How to Install dependencies 

* You can use pip or conda for installation of above libraries

### Note: If a version error occurs during installation, you can try to delete the old version and re-run the script

## Task Descrption

Make program that performs a simulation of the Schelling Model. You can use your favorite programming
language.

• The world is a 40 × 40 grid, for a total of G = 1600 cells
• The population P is expressed as a fraction of the cells. Consider P = 0.9.
• The agents are always 50% X and 50% O.
• The satisfaction threshold is set to t = {3, 4}.
• Agents are updated according to the cell they occupy, left-to-right, top-to-bottom. Start at
the top-left corner in the grid, move left-to-right along the first row, and update all the agents
you encounter. Once done with the row, move down to the leftmost cell of the second row,
and repeat the above steps.
• Unsatisfied agents move to the closest cell that makes them satisfied. Use an 8-Chebyshev
distance to find the closest cell. If no satisfactory cell is found in an 8-Chebyshev distance
radius, you can move the agent to a randomly selected empty cell in the grid.
