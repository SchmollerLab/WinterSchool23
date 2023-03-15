import skimage.io

import matplotlib.pyplot as plt

from models import example_model as model
from simple_gui import create_app

from cellacdc import myutils, apps

# Load the image data
image = skimage.io.imread('data/blobs.tif')

# Read the model parameters
init_params, segment_params = myutils.getModelArgSpec(model)

# Prompt user to set the parameters in a GUI widget
app = create_app()
win = apps.QDialogModelParams(
    init_params,
    segment_params,
    'cellpose', initLastParams=False
)
win.exec_()

# Initialize model and segment image data
model = model.Model(**win.init_kwargs)
labels = model.segment(image, **win.segment2D_kwargs)

# Display results
fig, ax = plt.subplots(1,2)
ax[0].imshow(image)
ax[1].imshow(labels)
plt.show()