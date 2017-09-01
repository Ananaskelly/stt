import matplotlib.pyplot as plt
import argparse

import helper
import hst
import numpy as np

parser = argparse.ArgumentParser(description='Build histogram for given array.')
parser.add_argument('-f', metavar='filename', type=str, nargs=1,
                    help='path to file with data')
parser.add_argument('-b', metavar='num_of_bins', type=int, nargs=1,
                    help='number of bins')


def run():

    args = parser.parse_args()
    args_dict = vars(args)
    filename = args_dict['f'][0]
    beans_num = args_dict['b'][0]
    data = helper.read_file(filename)

    hist_val = hst.get_hist(data, len(data), beans_num)

    # visualisation
    plt.bar(hist_val['x_val'][:-1], hist_val['y_val'], hist_val['int_size'], color='m')
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == '__main__':
    run()
