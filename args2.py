import argparse

parser = argparse.ArgumentParser(description="Description")
parser.add_argument('arg1', help="help arg 1")
args = parser.parse_args()
arg1 = args.arg1
