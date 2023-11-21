import utils
import numpy as np


def region_growing(im: np.ndarray, seed_points: list, T: int) -> np.ndarray:
    """
        A region growing algorithm that segments an image into 1 or 0 (True or False).
        Finds candidate pixels with a Moore-neighborhood (8-connectedness). 
        Uses pixel intensity thresholding with the threshold T as the homogeneity criteria.
        The function takes in a grayscale image and outputs a boolean image

        args:
            im: np.ndarray of shape (H, W) in the range [0, 255] (dtype=np.uint8)
            seed_points: list of list containing seed points (row, col). Ex:
                [[row1, col1], [row2, col2], ...]
            T: integer value defining the threshold to used for the homogeneity criteria.
        return:
            (np.ndarray) of shape (H, W). dtype=bool
    """
    # START YOUR CODE HERE ### (You can change anything inside this block)
    # You can also define other helper functions
    segmented = np.zeros_like(im).astype(bool)
    im = im.astype(float)

    # Checks if the neighbor is part of the segment or not
    def segment_neighbor(x: int, y: int, p: float) -> bool:
        if segmented[x, y]:
            return False
        if not segmented[x, y] and abs(p - im[x, y]) < T:
            segmented[*neighbor] = True
            return True
        return False

    
    # Returns 8 neighbors clockwise from the top-center
    def get_neighbors(x: int, y: int) -> np.ndarray:
        neighbors = np.array([
            [-1,  0],
            [-1,  1],
            [ 0,  1],
            [ 1,  1],
            [ 1,  0],
            [ 1, -1],
            [ 0, -1],
            [-1, -1],
        ])
        return neighbors + np.array([[x, y]])


    for row, col in seed_points:
        # Setup active list and reference intensity
        active = [[row, col]]
        intensity = im[*active[0]]
        while True:
            seed = active.pop()
            neighbors = get_neighbors(*seed)
            for neighbor in neighbors:
                if segment_neighbor(*neighbor, intensity):
                    active.append(neighbor)
            # Iterate until no more work is left
            if len(active) == 0:
                break

    return segmented
    ### END YOUR CODE HERE ###


if __name__ == "__main__":
    # DO NOT CHANGE
    im = utils.read_image("defective-weld.png")

    seed_points = [  # (row, column)
        [254, 138],  # Seed point 1
        [253, 296],  # Seed point 2
        [233, 436],  # Seed point 3
        [232, 417],  # Seed point 4
    ]
    intensity_threshold = 50
    segmented_image = region_growing(im, seed_points, intensity_threshold)

    assert im.shape == segmented_image.shape, "Expected image shape ({}) to be same as thresholded image shape ({})".format(
        im.shape, segmented_image.shape)
    assert segmented_image.dtype == bool, "Expected thresholded image dtype to be bool. Was: {}".format(
        segmented_image.dtype)

    segmented_image = utils.to_uint8(segmented_image)
    utils.save_im("defective-weld-segmented.png", segmented_image)
