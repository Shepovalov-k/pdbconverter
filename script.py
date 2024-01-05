#!/usr/bin/env python3.9

import argparse
import numpy as np



def read_xyz(fname):
    return np.genfromtxt(fname, skip_header=2,
               names = ['atom','x', 'y', 'z'],
               dtype = "S5,f4,f4,f4")

def read_gro(fname):
    with open(fname) as f:
        *_, last_line = f.readlines()
    vector = np.fromstring(last_line,
                 dtype=float,
                 sep=' ')
    return np.genfromtxt(fname, skip_header=2, skip_footer=1,
               names = ['mid', 'mol', 'atom', 'id', 'x', 'y', 'z'],
               dtype = "i4,S5,S6,i4,f4,f4,f4",
               invalid_raise=True, autostrip=True,
               delimiter=[5,5,5,5,8,8,8]), vector



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="the name of xyz-file")
    args = parser.parse_args()
    filename = args.filename
    if filename.endswith(".xyz"):
        print(read_xyz(filename))
    elif filename.endswith(".gro"):
        print(read_gro(args.filename))


if __name__ == "__main__":
    main()
