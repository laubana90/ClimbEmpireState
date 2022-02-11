import pytest
import numpy as np
from src.compute.utils import simulate_random_walk, generate_multiple_walks, compute_probability

class TestSimulateRandomWalk(object):

    def test_zero_rolls(self):
        actual = simulate_random_walk(0)
        expected = [0]
        assert actual == expected, "Expected: {0}, actual: {1}".format(expected, actual)
        
    def test_len_random_walk_0(self):
        actual = len(simulate_random_walk(0))
        expected = 1
        assert actual == expected, "Expected: {0}, actual: {1}".format(expected, actual)
        
    def test_len_random_walk_10(self):
        actual = len(simulate_random_walk(10))
        expected = 11
        assert actual == expected, "Expected: {0}, actual: {1}".format(expected, actual)
        
    def test_not_higher_than_six_per_step(self):
        actual = simulate_random_walk(10)
        assert all([step <= 6*roll for roll,step in enumerate(actual)]), "Have more than 6 steps in one roll"
        
class TestGenerateMultipleWalks(object):

    def test_all_walks_np_t_size(self):
        actual_walks, actual_ends = generate_multiple_walks(3,100)
        expected_walks = (101,3)
        expected_ends = 3
        assert actual_walks.shape == expected_walks, "Expected: {0}, actual: {1}".format(expected_walks, actual_walks)
        assert actual_ends.size == expected_ends, "Expected: {0}, actual: {1}".format(expected_ends, actual_ends)
        
    def test_zero_rolls(self):
        actual_walks, actual_ends = generate_multiple_walks(10,0)
        expected_ends = np.zeros(10, dtype=int)
        assert all(actual_ends == expected_ends), "Expected: {0}, actual: {1}".format(expected_ends, actual_ends)
        
    def test_zero_pseudoexperiments(self):
        actual_walks, actual_ends = generate_multiple_walks(0,10)
        expected_ends = 0
        expected_walks = 0
        assert actual_walks == expected_walks, "Expected: {0}, actual: {1}".format(expected_walks, actual_walks)
        assert actual_ends == expected_ends, "Expected: {0}, actual: {1}".format(expected_ends, actual_ends)
        
class TestComputeProbability(object):

    def test_possitive(self):
        ends = np.random.randint(1,301,500)
        actual = compute_probability(ends,500,60)
        assert actual > 0, "Probability should be positive"
        
    def test_smaller_100(self):
        ends = np.random.randint(1,301,500)
        actual = compute_probability(ends,500,60)
        assert actual <=100, "Probability should be smaller or equal than 100"
        
    def test_probability_zero_rolls(self):
        ends = np.zeros(500, dtype=int)
        actual = compute_probability(ends,500,60)
        expected = np.zeros(500, dtype=int)
        assert all(actual == expected), "Expected: {0}, actual: {1}".format(expected, actual)
        
    def test_probability_zero_pseudoexperiments(self):
        ends = np.random.randint(1,301,500)
        actual = compute_probability(ends,0,60)
        expected = 0.0
        assert actual == expected, "Expected: {0}, actual: {1}".format(expected, actual)
