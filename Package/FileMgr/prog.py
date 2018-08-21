import argparse


class CmdArg(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--square", help="display a square of a given number", type=int)
        parser.add_argument("-c", "--cubic", help="display a cubic of a given number", type=int)
        parser.add_argument("-v", "--verbosity", type=int, choices=[1, 2, 3],  help="increase output verbosity")
        args = parser.parse_args()
        if args.square:
            print(args.square**2)
        elif args.cubic:
            print(args.cubic**3)
        elif args.verbosity:
            print(args.verbosity)
        else:
            parser.parse_args(['-h'])
