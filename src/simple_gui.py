from PyQt5.QtWidgets import (
    QApplication, QDialog, QStyleFactory, QVBoxLayout, QLabel,
    QFormLayout, QSpinBox, QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QIcon

class MyWindow(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        # Create main layout
        layout = QVBoxLayout()

        # Add into text
        infoText = 'Please, provide the following parameters'
        infoLabel = QLabel(infoText)
        layout.addWidget(infoLabel)

        # Create the form layout
        formLayout = QFormLayout()

        # Add the widgets for the parameters
        firstParameterWidget = QSpinBox()
        formLayout.addRow('First parameter:', firstParameterWidget)

        # Add the form layout to main layout
        layout.addLayout(formLayout)

        # Create push buttons
        cancelButton = QPushButton('Cancel')
        okButton = QPushButton('Ok')

        # Add buttons to a horizontal box layout
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(cancelButton)
        buttonsLayout.addWidget(okButton)

        # Connect buttons 
        okButton.clicked.connect(self.ok_cb)

        # Add buttons layout and set main layout
        layout.addLayout(buttonsLayout)
        self.setLayout(layout)
    
    def ok_cb(self):
        print('Ok button clicked. Have a good day!')
        self.close()
    
    def cancel_cb(self):
        print('Cancel button clicked. Have a good day!')
        self.close()


def create_app():
    """Create a PyQt5 application instance, set the style and the icon

    Returns
    -------
    QtWidgets.QApplication
        The initialized PyQt5 application
    """    
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    app.setPalette(app.style().standardPalette())
    app.setWindowIcon(QIcon('src/icon.svg'))
    return app

def run():
    """Run the application and display the window
    """    
    app = create_app()
    win = MyWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    run()