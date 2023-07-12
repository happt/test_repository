import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num1", required=True)
parser.add_argument("--num2", required=True)

args = parser.parse_args()
num1 = int(args.num1)
num2 = int(args.num2)

print(f"{num1}+{num2}={num1+num2}")
