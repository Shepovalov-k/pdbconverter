#!/usr/bin/env python3.9

import argparse
import numpy as np


vdwradii = {
   'H':  0.12,
   'C':  0.17,
   'N':  0.155,
   'O':  0.152,
   'F':  0.147,
   'P':  0.18,
   'S':  0.18,
  'Cl':  0.175}


"XX YY ZZ XY XZ YX YZ ZX ZY"


def metric_tensor(XX, YY, ZZ, *off_diag):
    """XX YY ZZ XY XZ YX YZ ZX ZY"""
    if off_diag:
        XY, XZ, YX, YZ, ZX, ZY = off_diag
        return np.array([[XX, XY, XZ],
                         [YX, YY, YZ],
                         [ZX, ZY, ZZ]])
    else:
        return np.diag([XX, YY, ZZ])


def read_xyz(fname):
    return np.genfromtxt(fname, skip_header=2,
               names = ['atom','x', 'y', 'z'],
               dtype = "S5,f4,f4,f4")

def read_gro(fname):
    with open(fname) as f:
        *_, last_line = f.readlines()
        del _
        box_vector = tuple(map(float, last_line.split()))
    return np.genfromtxt(fname, skip_header=2, skip_footer=1,
               names = ['mid', 'mol', 'atom', 'id', 'x', 'y', 'z'],
               dtype = "i4,S5,S6,i4,f4,f4,f4",
               invalid_raise=True, autostrip=True,
               encoding='utf-8',
               delimiter=[5,5,5,5,8,8,8]), metric_tensor(*box_vector)



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
