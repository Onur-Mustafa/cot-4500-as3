import numpy as np

def f(t, y):
    return t - y**2

def euler_method(f, t0, y0, h, n):
    t = t0
    y = y0
    
    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h
    
    return y

def runge_kutta_method(f, t0, y0, h, n):
    t = t0
    y = y0
    
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h/2, y + (h/2)*k1)
        k3 = f(t + h/2, y + (h/2)*k2)
        k4 = f(t + h, y + h*k3)
        
        y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t = t + h
    
    return y

def main():
    # Initial conditions
    t0 = 0
    y0 = 1
    t_final = 2
    n = 10
    h = (t_final - t0) / n
    
    # Calculate using Euler method
    euler_result = euler_method(f, t0, y0, h, n)
    print(euler_result)
    
    # Calculate using Runge-Kutta method
    rk_result = runge_kutta_method(f, t0, y0, h, n)
    print(rk_result)

if __name__ == "__main__":
    main() 