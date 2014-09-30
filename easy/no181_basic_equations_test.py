import unittest
import numpy as np
from no181_basic_equations import *

class BasicEquationsTester(unittest.TestCase):

    def test_basic(self):
        equations = ["y=2x+2", "y=5x-4"]
        expected_solution = (2,6)

        actual_solution = solve_equations(*equations)
        np.testing.assert_almost_equal(expected_solution, actual_solution)

    def test_intercept_is_zero(self):
        equations = ["y=-5x", "y=-4x+1"]
        expected_solution = (-1, 5)

        actual_solution = solve_equations(*equations)
        np.testing.assert_almost_equal(expected_solution, actual_solution)

    def test_float_coefficients(self):
        equations = ["y=0.5x+1.3", "y=-1.4x-0.2"]
        expected_solution = (-0.7894737,  0.9052632)

        actual_solution = solve_equations(*equations)
        np.testing.assert_almost_equal(expected_solution, actual_solution)

    def test_no_solutions(self):
        equations = ["y=x+2", "y=x+3"]
        self.assertRaises(RuntimeError, solve_equations, *equations)

if __name__ == "__main__":
    unittest.main()
