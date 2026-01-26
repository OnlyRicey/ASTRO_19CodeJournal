import math
import numpy as py

def sin_table():
  values_x = py.linspace(0.0, 2.0, 1000)
  sin_val = py.sin(values_x)
  return sin_val, values_x

  
def main():
  x = sin_table()
  print(f"{'x':<15} | {'sin(x)':<15}")
  print("-" * 33)
  for i in range(1000):
        print(f"{x[1][i]:<15.4f} | {x[0][i]:<15.4f}")
    

if __name__ == "__main__":
    main()
