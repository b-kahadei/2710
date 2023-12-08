import argparse

parser = argparse.ArgumentParser(description='Це простий додаток, щоб познайомитися.')


parser.add_argument('pos',
                    help='A required integer positional argument')
parser.add_argument('-name',
                    help='A required integer positional argument')
parser.add_argument('--age',
                    help='A required integer positional argument',
                    required=True)

args = parser.parse_args()


print(args)