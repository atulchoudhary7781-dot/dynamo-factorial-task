import sys
import math

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Number must be non-negative")
            sys.exit(1)
            
        result = math.factorial(num)
        print(result)
        with open('/app/output.txt', 'w') as f:
            f.write(str(result))
    except ValueError:
        print("Invalid input - must be an integer")
        sys.exit(1)

if __name__ == "__main__":
    main()
