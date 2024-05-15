import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper():
    time_start = time.time()
    function()
    time_end = time.time()
    time_diff = time_end - time_start
    print(f"{function.__name__} run speed: {time_diff}s")  
  return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i


slow_function()
fast_function()