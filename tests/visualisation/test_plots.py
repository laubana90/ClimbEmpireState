import pytest
from unittest.mock import patch
import matplotlib.pyplot as plt
import numpy as np
from src.visualisation.plots import plot_random_walk, histogram_endpoints


  
@patch("src.visualisation.plots.plt")
def test_random_walk_plot(mock_plt):
    f, ax = plt.subplots()
    random_walk = [i for i in range(10)]
    minimum = 5
        
    @patch("src.visualisation.plots.show")
    def test_plot_correct_line(mock_show):
        f, ax = plt.subplots()
        plot_random_walk(random_walk, minimum)
        x_plot, y_plot = ax.lines[0].get_xydata().T
        np.testing.assert_array_equal(y_plot, random_walk)
        
@patch("src.visualisation.plots.plt")
def test_histogram_endpoints(mock_plt):
    f, ax = plt.subplots()
    ends = np.array([i for i in range(50)])
    minimum = 5
    probability = 10.0
        
    @patch("src.visualisation.plots.show")
    def test_plot_correct_line(mock_show):
        f, ax = plt.subplots()
        histogram_endpoints(ends, probability, minimum)
        x_plot, y_plot = ax.lines[0].get_xydata().T
        np.testing.assert_array_equal(y_plot, ends)
        
        
