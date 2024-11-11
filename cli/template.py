import os
import argparse
import json



def create(arguments):
    print(f"Created: {arguments.create[0]}")

def read(arguments):
    print(f"Read: {arguments.read[0]}")

def update(arguments):
    print(f"Updated: {arguments.update}")

def delete(arguments):
    print(f"Deleted: {arguments.delete}")


if __name__ == "__main__":
    # Create parser object
    parser = argparse.ArgumentParser("A cli tool!")

    # Define arguments for parser object
    parser.add_argument('-c', '--create', type=str, nargs=1, metavar='filename', default=None, help="Create the specified file!")
    parser.add_argument('-r', '--read', type=str, nargs=1, metavar='filename', default=None, help="Read the specified file!")
    parser.add_argument('-u', '--update', type=str, nargs=1, metavar='filename', default=None, help="Update the specified file!")
    parser.add_argument('-d', '--delete', type=str, nargs='*', metavar='filename', default=None, help="Delete the specified file!")
    parser.add_argument('catch', type=str, nargs='*', metavar='?', default=None, help="Catch input!")


    # Parse args from standard input
    args = parser.parse_args()


    if args.create:
        create(args)
    if args.read:
        read(args)
    if args.update:
        update(args)
    if args.delete:
        delete(args)
    
    print(f"Extra Arguments: {', '.join(args.catch)}")














