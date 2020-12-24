import time

def func(n):
    print(f"Function called after {n}s")

def job_scheduler(f, n):
    time.sleep(n)
    return f(n)

job_scheduler(func, 5)