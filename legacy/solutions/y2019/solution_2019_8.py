import sys  # isort:skip
import os  # isort:skip

sys.path.insert(0, os.path.dirname(sys.path[0][:-7]) + "/")  # NOQA: E402

from numpy import asarray, array, count_nonzero
from PIL import Image

from lib.helper import execution_timer, read_input


@execution_timer
def solution(data):
    dimensions = (25, 6)

    sif_data = [int(digit) for digit in data.strip()]

    sif_layers = array(sif_data).reshape((-1, dimensions[1], dimensions[0]))

    idx = count_nonzero(sif_layers, axis=(1, 2)).argmax()

    # 0 = black
    # 1 = white
    # 2 = transparent
    layer = 0
    composite = [2] * sif_layers[layer].size

    while layer <= sif_layers.shape[0] - 1:
        sif_layer = sif_layers[layer].flatten()

        for composite_idx, pixel in enumerate(composite):
            if pixel == 2:
                composite[composite_idx] = sif_layer[composite_idx]

        layer += 1

    composite = asarray(composite).reshape((dimensions[1], dimensions[0]))

    Image.fromarray(composite == 1).show()

    return sif_layers[idx][sif_layers[idx] == 1].size * sif_layers[idx][sif_layers[idx] == 2].size


def main():
    puzzle_input = read_input('2019_8.txt')

    print(f'Solution: {solution(puzzle_input)}\n')


if __name__ == '__main__':
    main()
