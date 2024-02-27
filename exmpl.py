from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout, QComboBox

app = QApplication([])

window = QWidget()
window.setWindowTitle('Конвертер')
window.show()

label = QLabel('Из какой валюты перевод?')
curr_from_box = QComboBox()
curr_from_box.addItems(['USD', 'EUR', 'RUB'])
curr_from = QLineEdit()
curr_from.setPlaceholderText('Введите сумму')

curr_to_box = QComboBox('В какой валюту перевести?')
curr_to_box.addItems(['EUR', 'USD', 'RUB'])
curr_to = QLineEdit()
curr_to.setReadOnly(True)

convert_button = QPushButton('Конвертировать')


layout = QVBoxLayout()

layout.addWidget(label)
layout.addWidget(curr_from_box)
layout.addWidget(curr_from)
layout.addWidget(curr_to_box)
layout.addWidget(curr_to)
layout.addWidget(convert_button)


window.setLayout(layout)



app.exec()