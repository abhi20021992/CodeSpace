from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('t', help='please add t')

print(parser.parse_args())