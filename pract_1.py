def f(x):
    return (x + 3) ** 2

def f_derivative(x):
    return 2 * (x + 3)

def gradient_descent(starting_x, learning_rate, tolerance, max_iters):
    x = starting_x
    for i in range(max_iters):
        grad = f_derivative(x)
        new_x = x - learning_rate * grad
        if abs(new_x - x) < tolerance:
            print(f"Converged at iteration {i+1}")
            break
        x = new_x
    return x

starting_x = 2         # Initial value of x
learning_rate = 0.1    # Step size
tolerance = 1e-6       # Tolerance for convergence
max_iters = 1000       # Maximum number of iterations

local_minimum = gradient_descent(starting_x, learning_rate, tolerance, max_iters)
print("Local minimum at x =", local_minimum)
