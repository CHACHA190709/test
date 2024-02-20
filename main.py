from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QCheckBox, QPushButton, QVBoxLayout
import string
import random

app = QApplication([])

window = QWidget()
window.setWindowTitle('Генератор паролей')
window.show()
window.resize(400, 200)

layout = QVBoxLayout()

password_label = QLabel('Сгенерированный пароль:')
password_display = QLineEdit()
password_display.setReadOnly(True)

lenght_label = QLabel('Длина пароля:')
lenght_input = QLineEdit()

lowercase_chekbox = QCheckBox('Использовать строчные буквы')
uppercase_chekbox = QCheckBox('Использовать заглавные буквы')
numbers_chekbox = QCheckBox('Использовать цифры')
symbols_chekbox = QCheckBox('Использовать символы')

generate_button = QPushButton('Сгенерировать')

layout.addWidget(password_label)
layout.addWidget(password_display)
layout.addWidget(lenght_label)
layout.addWidget(lenght_input)
layout.addWidget(lowercase_chekbox)
layout.addWidget(uppercase_chekbox)
layout.addWidget(numbers_chekbox)
layout.addWidget(symbols_chekbox)
layout.addWidget(generate_button)


window.setLayout(layout)

# =================================

def generate_password():
    try:
        lenght = int(lenght_input.text())
    except:
        password_display.setText('Введи длину пароля числом !!!')
        return None

    symbols = ''

    if lowercase_chekbox.isChecked():
        symbols += string.ascii_lowercase
    if uppercase_chekbox.isChecked():
        symbols += string.ascii_uppercase
    if numbers_chekbox.isChecked():
        symbols += string.digits
    if symbols_chekbox.isChecked():
        symbols += string.punctuation

    if len(symbols) == 0:
        password_display.setText('Выберите хотя бы одну опцию')
        return None

    password = ''
    for i in range(lenght):
        password += random.choice(symbols)
    password_display.setText(password)

generate_button.clicked.connect(generate_password)

app.exec()
