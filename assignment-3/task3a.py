import utils
import skimage
import skimage.morphology as morph
import numpy as np

def create_circle_array(size):
    arr = np.zeros((size, size))
    y, x = np.ogrid[:size, :size]
    center = size // 2
    radius = size // 2
    
    mask = (x - center)**2 + (y - center)**2 <= radius**2
    arr[mask] = 1
    
    return arr


def remove_noise(im: np.ndarray) -> np.ndarray:
    """
        A function that removes noise in the input image.
        args:
            im: np.ndarray of shape (H, W) with boolean values (dtype=bool)
        return:
            (np.ndarray) of shape (H, W). dtype=bool
    """
    # START YOUR CODE HERE ### (You can change anything inside this block)
    # You can also define other helper functions
    footprint = create_circle_array(16)
    im = morph.binary_closing(im, footprint=footprint)
    im = morph.binary_opening(im, footprint=footprint)
    return im
    ### END YOUR CODE HERE ###


if __name__ == "__main__":
    # DO NOT CHANGE
    im = utils.read_image("noisy.png")

    binary_image = (im != 0)
    noise_free_image = remove_noise(binary_image)

    assert im.shape == noise_free_image.shape, "Expected image shape ({}) to be same as resulting image shape ({})".format(
        im.shape, noise_free_image.shape)
    assert noise_free_image.dtype == bool, "Expected resulting image dtype to be bool. Was: {}".format(
        noise_free_image.dtype)

    noise_free_image = utils.to_uint8(noise_free_image)
    utils.save_im("noisy-filtered.png", noise_free_image)
