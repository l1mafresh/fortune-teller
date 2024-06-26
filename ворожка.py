import sys, os, random
from PyQt6 import QtWidgets, QtCore, QtGui

answers = [
    "Так", "Ні", "Можливо", "Скоріше так", "Ближче до ні",
    "Безумовно так", "Безумовно ні", "Не знаю", "Запитай пізніше",
    "Запитай когось іншого", "Тільки якщо будеш старатися",
    "Якщо будеш йти до цього - так", "Запитай щось важливіше"
]

previous_request = ""

def generate_answer():
    global previous_request
    tx = request_text.toPlainText()
    if not tx.endswith("?"):
        answer_label.setStyleSheet("color: grey;")
        answer_label.setText("Некоректний запит")
    elif tx == previous_request:
        answer_label.setStyleSheet("color: grey;")
        answer_label.setText("Я вже відповідав на це питання")
    else:
        answer_label.setStyleSheet("")
        answer_label.setText(random.choice(answers))
        previous_request = tx

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.setWindowTitle("Ворожка")
win.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")))
win.resize(320, 240)
win.setMinimumSize(320, 240)

vert_lay = QtWidgets.QVBoxLayout(win)

font = QtGui.QFont()
font.setPointSize(12)
font.setBold(True)

answer_label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignmentFlag.AlignCenter, font=font)
vert_lay.addWidget(answer_label)

request_text = QtWidgets.QTextEdit(placeholderText="Введіть своє питання тут...", font=font)
vert_lay.addWidget(request_text)

ask_btn = QtWidgets.QPushButton("Ворожити", font=font)
ask_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #5500ff, stop:1 #00aa00); color: white")
ask_btn.clicked.connect(generate_answer)
vert_lay.addWidget(ask_btn)

win.show()
sys.exit(app.exec())
