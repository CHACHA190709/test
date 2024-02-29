from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QLabel, QComboBox, QPushButton
import requests

app = QApplication([])

window = QWidget()
window.setWindowTitle('Конвентор валют')
window.resize(200, 150)

window.show()

API_KEY = '10d8ea0dcb93b0c4606ea544c15fa034'


layout = QVBoxLayout()

valt = QLabel('В какую валюту сконвертировать?')
valt_input = QLineEdit()
valt_input.setPlaceholderText('Введите сумму')
valt_disp = QLineEdit()
valt_disp.setReadOnly(True)
valt_disp.setPlaceholderText('Курс')
box = QComboBox()
box.addItems(['USD','EUR','RUB'])
box2 = QComboBox()
box2.addItems(['RUB','EUR','USD'])
valt_button = QPushButton('Конвертировать')



layout.addWidget(valt_input)
layout.addWidget(valt_disp)
layout.addWidget(valt)
layout.addWidget(box)
layout.addWidget(box2)
layout.addWidget(valt_button)


window.setLayout(layout)

def convert():
    curs_from = box.currentText()
    curs_to = box2.currentText()
    try:
        res = requests.get(f"https://currate.ru/api/?get=rates&pairs={curs_from}{curs_to}&key={API_KEY}")
        data = res.json()
        course = data['data'][curs_from + curs_to]
        result = float(valt_input.text()) * float(course)
        valt_disp.setText(str(round(result, 2)))
    except:
        pass
        valt_disp.setText('Ошибка')


valt_button.clicked.connect(convert)

app.exec()

