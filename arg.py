import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--gene1", required=True)
parser.add_argument("--gene2", required=True)

args = parser.parse_args()
gene1 = args.gene1
gene2 = args.gene2

print(f"GENE1: {gene1}")
print(f"GENE2: {gene2}")
