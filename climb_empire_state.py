from src.utils import simulate_random_walk, generate_multiple_walks, compute_probability
from src.plots import plot_random_walk, histogram_endpoints
from configparser import ConfigParser

def main():

    # Read input file
    config = ConfigParser()
    config.read('input/config.ini')
    number_of_dice_rolls = int(config.get('main','number_of_dice_rolls'))
    minimum_step = int(config.get('main','minimum_step'))
    number_of_pseudoexperiments = int(config.get('main','number_of_pseudoexperiments'))

    # Create one sample random walk and visualize it
    walk = simulate_random_walk(number_of_dice_rolls)
    plot_random_walk(walk, minimum_step)

    # Create an ensemble of random walks
    set_of_walks, end_points = generate_multiple_walks(number_of_pseudoexperiments, number_of_dice_rolls)

    # Compute the probability of reaching step 'minimum' after 'number_of_dice_rolls' rolls
    probability = compute_probability(end_points,number_of_pseudoexperiments, minimum_step)

    # Visualise the set of random walks and display the resulting probability
    histogram_endpoints(end_points, probability, minimum_step)

if __name__ == "__main__":
    main()
