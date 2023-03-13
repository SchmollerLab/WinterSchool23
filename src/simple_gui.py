from PyQt5.QtWidgets import (
    QApplication, QDialog, QStyleFactory, QVBoxLayout, QLabel,
    QFormLayout, QSpinBox, QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QIcon

class MyWindow(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        layout = QVBoxLayout()

        infoText = 'Please, provide the following parameters'
        infoLabel = QLabel(infoText)
        layout.addWidget(infoLabel)

        formLayout = QFormLayout()

        firstParameterWidget = QSpinBox()
        formLayout.addRow('First parameter:', firstParameterWidget)

        layout.addLayout(formLayout)

        cancelButton = QPushButton('Cancel')
        okButton = QPushButton('Ok')

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(cancelButton)
        buttonsLayout.addWidget(okButton)

        layout.addLayout(buttonsLayout)

        self.setLayout(layout)


def create_app():
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    app.setPalette(app.style().standardPalette())
    app.setWindowIcon(QIcon('snowman.svg'))
    return app

def run():
    app = create_app()
    win = MyWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    run()