import matplotlib.image as mpimg
import numpy as np


def cellpose_img_load(img_path=None, img_data=None):
    """
    Function to load images from the cellpose dataset (see www.cellpose.org) for visualization.
    Images are stored as png and contain data in either one (only G) or two channels (R+G).
    Function loads the image data and returns 1- or 3-channel array respectively.
    If input is R+G, returns RGB image using R+B channels.
    If input is only G, returns grayscale image.
    """
    if img_path:
        img_data = mpimg.imread(img_path)
    channel_sums = img_data.sum(axis=(0,1))
    if sum(channel_sums>0) == 1:
        return img_data[:,:,1]
    elif sum(channel_sums>0) == 2:
        return_arr = np.array([
            np.zeros(img_data.shape[:2]),
            img_data[:,:,1],
            img_data[:,:,0]
        ])
        return np.moveaxis(return_arr, 0, 2)
    else:
        raise ValueError('Received input with more than two non-zero channels.')
    

def dense_from_acdc(gt):
    """
    Highly important for segmentation evaluation:
    take gt, transform to dense vector, where each number from 0 to max(gt) is used (no values missing)
    """
    # TODO: use numba here?
    unique_ids = sorted(list(np.unique(gt)))
    new_ids = list(range(len(unique_ids)))
    mapping = dict(zip(unique_ids, new_ids))
    return np.vectorize(mapping.__getitem__)(gt)