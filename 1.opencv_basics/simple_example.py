import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="Enter your name", type=str)
args = vars(ap.parse_args())

print(args)

print(f"Hi there nice to meet you {args['name']}")

