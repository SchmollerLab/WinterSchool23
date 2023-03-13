from models import example_model, cellpose
from A_simple_gui import create_app

from cellacdc import myutils, apps

init_params, segment_params = myutils.getModelArgSpec(cellpose)

print('*'*100)
print(init_params)
print(segment_params)
print('*'*100)

app = create_app()
win = apps.QDialogModelParams(
    init_params,
    segment_params,
    'cellpose', initLastParams=False
)
win.exec_()