import base64
import random

import qrcode
import requests
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from ui_MainWindow import *

API_URL = "http://20.219.141.225:8000/api"

already_registered = []


class QRCodeDialogBox(QDialog):
    def __init__(self, api_key: str, parent=None):
        super().__init__(parent)

        self.api_key = api_key

        self.setWindowTitle("QR Code Registration")

        QBtn = QDialogButtonBox.Retry | QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(QBtn)
        self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        self.button_box.button(QDialogButtonBox.Retry).clicked.connect(
            self.check_registration
        )

        self.button_box.button(QDialogButtonBox.Ok).clicked.connect(
            self.close
        )

        self.dialog_box_layout = QVBoxLayout()
        
        label = QLabel()
        pixmap = QPixmap(self.create_qr_code())
        label.setPixmap(pixmap)

        self.dialog_box_layout.addWidget(label)
        self.dialog_box_layout.addWidget(self.button_box)
        self.setLayout(self.dialog_box_layout)
        self.resize(pixmap.width(), pixmap.height())

    def create_qr_code(self):
        self.random_participant_id = random.choice(
            [i for i in range(2000) if i not in already_registered]
        )

        path = f"{self.random_participant_id}.png"

        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr_code.add_data(base64.b64encode(str(self.random_participant_id).encode("utf-8")))
        qr_img = qr_code.make_image(fill_color="black", back_color="white")
        qr_img.save(path)

        return path

    def check_registration(self):
        if requests.get(f"{API_URL}/user/", params={"user_id": self.random_participant_id, "api-key": self.api_key}).json()["user_attendance"] is True:
            QMessageBox.information(self, "Success!", "That user has been successfully registered!")
            self.button_box.button(QDialogButtonBox.Ok).setEnabled(True)
            return

        QMessageBox.warning(self, "Error!", "That user has not been registered yet!")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup the UI from the UI file.
        self.setupUi(self)

        # API key authentication variables.
        self.api_key: str

        # Connect API key authentication buttons.
        self.api_key_login_button.clicked.connect(self.api_key_auth)

        self.qr_code_registration_button.clicked.connect(self.new_qr_code)

    def api_key_auth(self):
        """
        Authenticate the event head through the API.
        """

        # Get API key entered by user and validate it with the API.
        api_key = self.api_key_field.text()
        request = requests.get(f"{API_URL}/api-key", params={"api-key": api_key})

        # Check if validation was successful
        if request.status_code == 200:
            # Set the instance API key variable to the entered API key.
            self.api_key = api_key
            QMessageBox.information(
                self, "Success!", f"Successfully logged in as {request.json()['user']}!"
            )

            # Disable the API key field and enable the app.
            self.api_key_field.setEnabled(False)
            self.api_key_login_button.setEnabled(False)
            self.qr_code_registration_button.setEnabled(True)

            return

        QMessageBox.warning(self, "Invalid Credentials", "Invalid API key!")

    def new_qr_code(self):
        QRCodeDialogBox(self.api_key).exec()


app = QApplication([])
app.setStyle("Fusion")

window = MainWindow()
window.show()

app.exec()
