from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout
import string
import random

app = QApplication([])

window = QWidget()
window.setWindowTitle('Генератор паролей')
window.show()
window.resize(400,300)

layout = QVBoxLayout()

pass_label = QLabel('Cгенирированный пароль:')
pass_disp = QLineEdit()
pass_disp.setReadOnly(True)
pass_size = QLabel('Длина пароля:')
pass_size_disp = QLineEdit()

strock = QCheckBox('Использывать строчные буквы')
zaglav = QCheckBox('Использывать заглавные буквы')
number = QCheckBox('Использывать цифры')
simvol = QCheckBox('Использывать символы')

gen_button = QPushButton('Сгенерировать')



layout.addWidget(pass_label)
layout.addWidget(pass_disp)
layout.addWidget(pass_size)
layout.addWidget(pass_size_disp)
layout.addWidget(strock)
layout.addWidget(zaglav)
layout.addWidget(number)
layout.addWidget(simvol)
layout.addWidget(gen_button)



window.setLayout(layout)

#--------------------------------------------------

def generate_password():
    try:
        lenght = int(pass_size_disp.text())
    except:
        pass_disp.setText('Введи длину пароля числом!')
        return None
    
    symbols = ''
    if strock.isChecked():
        symbols += string.ascii_lowercase
    if zaglav.isChecked():
        symbols += string.ascii_uppercase
    if number.isChecked():
        symbols += string.digits
    if simvol.isChecked():
        symbols += string.punctuation
    
    if len(symbols) == 0:
        pass_disp.setText('Выберите хотябы одну функцию')
        return None
    
    password = ''
    for i in range(lenght):
        password += random.choice(symbols)
    pass_disp.setText(password )


    

    
gen_button.clicked.connect(generate_password)
    


app.exec()