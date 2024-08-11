import math

def main():
    a = int(input())
    b = int(input())

    angle = math.degrees(math.atan2(a, b))  # Calculate angle in degrees

    print(int(round(angle)))  # Round to nearest integer and print

if __name__ == "__main__":
    main()
