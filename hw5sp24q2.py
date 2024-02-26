from scipy.optimize import fsolve
import numpy as np
import warnings

"""
I didn't love the answers I was getting (I used ChatGPT to help, by providing
pseudo code and walking it through finding the correct answer). 
It was giving a large amount of intersection points, several of which,
being almost exactly the same. Hence, the 'find if the points are the same'
section.
"""


def func1(x):
    """Function 1: f(x) = x^2 - 10"""
    return x-3 * np.cos(x)


def func2(x):
    """Function 2: g(x) = x^3 + 6"""
    return np.cos(2*x) * x**3


def intersection_function(x):
    """Difference between function 1 and function 2 to find intersections."""
    return func1(x) - func2(x)


def find_roots(func, initial_guesses):
    """
    Finds unique roots for a given function within a range of initial guesses.
    Reduces redundancy by filtering out near-duplicate roots.
    """
    roots = []
    for guess in initial_guesses:
        try:
            root, = fsolve(func, guess, xtol=1e-8)
            # Check if this root is essentially a duplicate of an already found root
            if not any(np.isclose(root, existing, atol=1e-4) for existing in roots):
                roots.append(root)
        except Exception as e:
            pass  # Ignore errors and move on to the next guess
    return np.unique(np.round(roots, 5))


def find_intersection_points(func, initial_guesses):
    """
    Identifies intersection points by finding roots of the intersection function,
    minimizing redundancy through careful selection and comparison.
    """
    intersections = []
    for i in range(len(initial_guesses) - 1):
        x0 = initial_guesses[i]
        x1 = initial_guesses[i + 1]
        if np.sign(func(x0)) != np.sign(func(x1)):
            try:
                root, = fsolve(func, x0, xtol=1e-8)
                if not intersections or not np.isclose(root, intersections[-1], atol=1e-4):
                    intersections.append(root)
            except Exception as e:
                pass  # Ignore errors and move on
    return np.unique(np.round(intersections, 5))


# Define a range of initial guesses
initial_guesses = np.linspace(-5, 5, 1000)

# Suppress specific fsolve warnings to clean up the output
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=RuntimeWarning)

    # Find unique roots for both functions
    unique_roots_func1 = find_roots(func1, initial_guesses)
    unique_roots_func2 = find_roots(func2, initial_guesses)

    # Find intersection points
    intersection_points = find_intersection_points(intersection_function, initial_guesses)

# Display the results
print("All unique roots of func1:", unique_roots_func1)
print("All unique roots of func2:", unique_roots_func2)
print("Filtered potential intersection points at x= :", intersection_points)
