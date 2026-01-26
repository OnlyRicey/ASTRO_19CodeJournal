import math
import numpy as py

def sin_table():
  values_x = py.linspace(0.0, 2.0, 1000)
  sin_val = py.sin(values_x)
  return sin_val, values_x

  
def main():
  x = sin_table()
  print(f"{'x':<10} | {'sin(x)':<10}")
  print("-" * 20)
  for i in range(1000):
        print(f"{x[1][i]:<10.5f} | {x[0][i]:<10.5f}")
    

if __name__ == "__main__":
    main()
