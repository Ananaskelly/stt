import sys

import helper
import matplotlib.pyplot as plt
import numpy as np
import hst


def run():

    assert len(sys.argv) == 3, "Wrong number of arguments"

    filename = sys.argv[1]
    beans_num = sys.argv[2]
    data = helper.read_file(filename)

    hist_val = hst.get_hist(data, len(data), int(beans_num))

    plt.bar(hist_val['x_val'][:-1], hist_val['y_val'], hist_val['int_size'], color='m')
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.show()

    print(hist_val['x_val'], hist_val['y_val'])
    print(np.histogram(data, int(beans_num)))

if __name__ == '__main__':
    run()
