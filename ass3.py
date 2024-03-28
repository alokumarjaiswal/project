'''           DECORATORS           '''
import time


def log_execution_time(func):  # func is the function to be decorated
    def wrapper(*args, **kwargs):  # *args and **kwargs are used to accept any number of positional and keyword arguments
        start_time = time.time()
        result = func(*args, **kwargs)  # Call the function with the arguments
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result  # Return the result of the function

    return wrapper  # Return the wrapper function


# Example usage
@log_execution_time  # it is equivalent to calculate_pi = log_execution_time(calculate_pi)
def calculate_pi(n_terms):
    pi = 0
    for i in range(n_terms):
        pi += 4 * ((-1) ** i) / (2 * i + 1)
    print(f"Calculated value of pi: {pi}")


calculate_pi(1000000)


'''           lambda function           '''
# Lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression
# Example:
add = lambda x, y : x + y
print(add(5, 3))
print((lambda x, y : x + y)(5, 3))