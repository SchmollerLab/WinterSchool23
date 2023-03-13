import skimage.io

import matplotlib.pyplot as plt

from models import example_model as model
from A_simple_gui import create_app

from cellacdc import myutils, apps

image = skimage.io.imread('data/blobs.tif')

init_params, segment_params = myutils.getModelArgSpec(model)

app = create_app()
win = apps.QDialogModelParams(
    init_params,
    segment_params,
    'cellpose', initLastParams=False
)
win.exec_()

model = model.Model(**win.init_kwargs)
labels = model.segment(image, **win.segment2D_kwargs)

fig, ax = plt.subplots(1,2)
ax[0].imshow(image)
ax[1].imshow(labels)
plt.show()