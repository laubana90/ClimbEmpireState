import numpy as np

def simulate_random_walk(n_rolls):
    '''
    Simulates a random walk given a number of dice rolls and returns the outcome.
    Takes into account that the lower possible step is 0 and that
    there is a 0.1% chance of falling down and having to start from 0.
    
    Each movement is based in the outcome of a dice roll:
    - 1/2 : go one step down
    - 3/4/5: go one step up
    - 6: throw again and go up the resulting number of steps
    

    Parameters
    ----------
    n_rolls: int
      Number of dice rolls

    Returns
    -------
    random_walk: list
      Final walk. Each element corresponds to the actual step based on the
      roll outcome and the previous position

    '''
    
    random_walk = [0]
    for n in range(n_rolls):
        # Take as initial position the previous step
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            # Prevent step from being negative
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # Account for 0.1% chances of falling down
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    return random_walk
    
def generate_multiple_walks(n_pseudoexperiments, n_rolls):
    '''
    Generates a number of random walks and stores the outcomes
    as a numpy array. It uses the function simulate_random_walk
    
    Parameters
    ----------
    n_pseudoexperiments: int
      Number of pseudoexperiments
    n_rolls: int
      Number of dice rolls

    Returns
    -------
    all_random_walk: 2d-numpy array
      Each element corresponds to one complete random walk
    ends: numpy array
       Each element corresponds to the end-point of a random walk

    '''
    
    if n_pseudoexperiments == 0:
        return 0,0
    
    # Generate the set of random walks
    all_walks = []
    for i in range(n_pseudoexperiments):
        random_walk = simulate_random_walk(n_rolls)
        # Create a list of lists
        all_walks.append(random_walk)

    # Transform all walks into a 2d-numpy array and transpose it
    all_walks_np = np.array(all_walks)
    all_walks_np_t = np.transpose(all_walks_np)

    # Select last row from all_walks_np_t
    ends = all_walks_np_t[-1,:]
    
    return all_walks_np_t, ends
    
def compute_probability(ends,n_pseudoexperiments, minimum):
    '''
    Compute the probability of reaching at least step 'minimum' after 'n_rolls' dice rolls
    
    Parameters
    ----------
    ends: numpy array
       Each element corresponds to the end-point of a random walk
    n_pseudoexperiments: int
      Number of pseudoexperiments
    minimum: int
      Minimum step to reach at the end
      
    Returns
    -------
    probability: float
        probability of reaching at least step 'minimum' after 'n_rolls' dice rolls

    '''
    if n_pseudoexperiments == 0:
        return 0.0
    probability = (np.count_nonzero(ends >= minimum)/n_pseudoexperiments)*100
    print("Probability of reaching step {0} is: {1}%".format(minimum, probability))    
    return probability
