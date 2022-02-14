import matplotlib.pyplot as plt
import os

def plot_random_walk(random_walk, minimum):
    '''
    Create a simple line plot from the list that contains the steps
    
    Parameters
    ----------
    random_walk: list
      Each element corresponds to each step from each dice roll.
    minimum: int
      Minimum step to reach at the end

    '''
    
    fig = plt.plot(random_walk)
    
    # Make the plot readable
    plt.xlabel("Number of dice rolls")
    plt.ylabel("Position")
    plt.title("Random walk")
    plt.axhline(minimum, color='Gray', linestyle='--', linewidth=0.7)
    plt.text(0,minimum*0.93,"Want to have the end point above this mark")

    # Save the figure
    create_dir('figures')
    plt.savefig('figures/random_walk.png')
    
def histogram_endpoints(ends, probability, minimum):
    '''
    Create a histogram from the end points of the set of random walks
    
    Parameters
    ----------
    ends: numpy array
       Each element corresponds to the end-point of a random walk
    minimum: int
      Minimum step to reach at the end

    '''
    __, ax = plt.subplots()
    plt.hist(ends, bins=30)
    
    # Make the plot readable
    plt.xlabel("Final step")
    plt.ylabel("Counts")
    plt.title("Distribution of end points")
    plt.text(0.05,0.8,"Probability: "+ str(probability)+"%", transform=ax.transAxes)
    plt.axvline(minimum, color='Tomato', linestyle='--')
 
    # Save the figure
    create_dir('figures')
    plt.savefig('figures/histogram_endpoints.png')

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
