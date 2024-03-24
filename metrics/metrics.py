import time

def measure_time(func, *args, **kwargs):
    """
    Measure the execution time of a function.
    
    Parameters:
    func (function): The function to be measured.
    *args: Variable length argument list.
    **kwargs: Arbitrary keyword arguments.
    
    Returns:
    tuple: A tuple containing the result of the function and the execution time in microseconds.
    """
    total_time = 0
    for _ in range (10):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    
    return total_time * 1e6 /10
