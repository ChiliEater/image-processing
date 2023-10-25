import matplotlib.pyplot as plt
import pathlib
from utils import read_im, save_im
output_dir = pathlib.Path("image_solutions")
output_dir.mkdir(exist_ok=True)


im = read_im(pathlib.Path("images", "duck.jpeg"))
plt.imshow(im)


greayscale_weights = [0.212, 0.7152, 0.0722]
def greyscale(im):
    """ Converts an RGB image to greyscale

    Args:
        im ([type]): [np.array of shape [H, W, 3]]

    Returns:
        im ([type]): [np.array of shape [H, W]]
    """

    return im[:, :, 0] * greayscale_weights[0] + im[:, :, 1] * greayscale_weights[1] + im[:, :, 2] * greayscale_weights[2]


im_greyscale = greyscale(im)
save_im(output_dir.joinpath("duck_greyscale.jpg"), im_greyscale, cmap="gray")
plt.imshow(im_greyscale, cmap="gray")


def inverse(im):
    """ Finds the inverse of the greyscale image

    Args:
        im ([type]): [np.array of shape [H, W]]

    Returns:
        im ([type]): [np.array of shape [H, W]]
    """
    return 1.0 - im[:, :]

im_inverse = inverse(im_greyscale)
save_im(output_dir.joinpath("duck_intense.jpeg"), im_inverse, cmap="gray")
plt.imshow(im_inverse, cmap="gray")
