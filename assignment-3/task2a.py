import numpy as np
import skimage
import utils
import pathlib
import matplotlib.pyplot as plt

def otsu_thresholding(im: np.ndarray) -> int:
    """
        Otsu's thresholding algorithm that segments an image into 1 or 0 (True or False)
        The function takes in a grayscale image and outputs a threshold value

        args:
            im: np.ndarray of shape (H, W) in the range [0, 255] (dtype=np.uint8)
        return:
            (int) the computed thresholding value
    """
    assert im.dtype == np.uint8
    # START YOUR CODE HERE ### (You can change anything inside this block)
    # You can also define other helper functions
    
    # Similar to example on Wikipedia
    def otsu_intraclass_variance(image, threshold):
        # Sum of all products
        return np.nansum([
            # Product of class mean and class variance
            np.mean(cls) * np.var(image, where=cls) 
            # Select all pixels above threshold then all pixels below threshold
            for cls in [image >= threshold, image < threshold]
        ])

    # Compute intraclass variance for all possible pixel values and extract minimum value
    return min(
        range(np.min(im) + 1, np.max(im)),
        key = lambda th: otsu_intraclass_variance(im, th)
    )
    ### END YOUR CODE HERE ###


if __name__ == "__main__":
    # DO NOT CHANGE
    impaths_to_segment = [
        pathlib.Path("thumbprint.png"),
        pathlib.Path("rice-shaded.png")
    ]
    for impath in impaths_to_segment:
        im = utils.read_image(impath)
        threshold = otsu_thresholding(im)
        print("Found optimal threshold:", threshold)

        # Segment the image by threshold
        segmented_image = (im >= threshold)
        assert im.shape == segmented_image.shape, "Expected image shape ({}) to be same as thresholded image shape ({})".format(
            im.shape, segmented_image.shape)
        assert segmented_image.dtype == bool, "Expected thresholded image dtype to be bool. Was: {}".format(
            segmented_image.dtype)

        segmented_image = utils.to_uint8(segmented_image)

        save_path = "{}-segmented.png".format(impath.stem)
        utils.save_im(save_path, segmented_image)
