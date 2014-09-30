#!/bin/bash/python
import re
import numpy as np
import argparse

def parse_equation(equation_string):
    float_regex = "[-+]?(?:\d*\.\d+|\d+)"
    equation_regex = "y=(%s)?x(%s)?" % (float_regex, float_regex)
    re.compile(equation_regex)

    match = re.match(equation_regex, equation_string)

    if match is None or len(match.groups()) < 2:
        raise RuntimeError("Could not parse equation %s" % equation_string)

    coeffcients = map(lambda x: float(x) if x is not None else 0, match.groups())
    return coeffcients

def find_intersection(eq1_coefficients, eq2_coefficients):

    a1, b1 = eq1_coefficients
    a2, b2 = eq2_coefficients

    det = (a2-a1)
    if det == 0:
        raise RuntimeError("Lines are parallel. There are no solutions!")

    x = (b1-b2)/(a2-a1)
    y = (a2*b1 - a1*b2)/(a2-a1)

    return x,y

def solve_equations(equation1, equation2):
    eq1_coefficients = parse_equation(equation1)
    eq2_coefficients = parse_equation(equation2)
    return find_intersection(eq1_coefficients, eq2_coefficients)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve some linear equations.')
    parser.add_argument('equations', metavar='e', type=str, nargs='+',
                       help='a list of equations to find the intersection of.')
    args = parser.parse_args()

    if len(args.equations) < 2:
        raise RuntimeError("Must have at least to equations to find the intersection.")

    solution = solve_equations(*args.equations)
    print solution
