from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout, QComboBox
import requests

app = QApplication([])
API_KEY = '10d8ea0dcb93b0c4606ea544c15fa034'

window = QWidget()
window.setWindowTitle('Конвертер')
window.resize(400, 200)
window.show()

label_from = QLabel('Из какой валюты перевод?')
curr_from_box = QComboBox()
curr_from_box.addItems(['USD', 'EUR', 'RUB'])
curr_from = QLineEdit()
curr_from.setPlaceholderText('Введите сумму')

label_to = QLabel('В какую валюту перевод?')
curr_to_box = QComboBox()
curr_to_box.addItems(['EUR', 'USD', 'RUB'])
curr_to = QLineEdit()
curr_to.setReadOnly(True)

convert_button = QPushButton('Конвертировать')


layout = QVBoxLayout()

layout.addWidget(label_from)
layout.addWidget(curr_from_box)
layout.addWidget(curr_from)

layout.addWidget(label_to)
layout.addWidget(curr_to_box)
layout.addWidget(curr_to)

layout.addWidget(convert_button)

window.setLayout(layout)

def convert():
    current_from = curr_from_box.currentText()
    current_to = curr_to_box.currentText()
    try:
        res = requests.get(f"https://currate.ru/api/?get=rates&pairs={current_from}{current_to}&key={API_KEY}")
        data = res.json()
        course = data['data'][current_from + current_to]
        result = float(curr_from.text()) * float(course)
        curr_to.setText(str(round(result, 2)))
    except:
        curr_to.setText('Ошибка')

convert_button.clicked.connect(convert)

app.exec()