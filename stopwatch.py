import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QPushButton, QListWidget
from PyQt5.QtCore import QTimer


class StopwatchWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Кнопка старта секундомера
        self.btn_start = QPushButton('Старт', self)
        self.btn_start.move(225, 50)
        self.btn_start.resize(50, 50)
        self.btn_start.clicked.connect(self.start)
        # Кнопка паузы
        self.btn_pause = QPushButton('Пауза', self)
        self.btn_pause.move(225, 50)
        self.btn_pause.resize(50, 50)
        self.btn_pause.setVisible(False)
        self.btn_pause.clicked.connect(self.pause)
        # Кнопка для продолжения секундомера
        self.btn_continue = QPushButton('Продолжить', self)
        self.btn_continue.move(200, 50)
        self.btn_continue.resize(100, 50)
        self.btn_continue.setVisible(False)
        self.btn_continue.clicked.connect(self.timer_continue)
        # Кнопка сохранения результата секундомера
        self.btn_split = QPushButton('Split', self)
        self.btn_split.move(150, 50)
        self.btn_split.resize(50, 50)
        self.btn_split.setVisible(False)
        self.btn_split.clicked.connect(self.spliting)
        # Сброс секундомера и его значений
        self.btn_drop = QPushButton('Сброс', self)
        self.btn_drop.move(300, 50)
        self.btn_drop.resize(50, 50)
        self.btn_drop.setVisible(False)
        self.btn_drop.clicked.connect(self.drop)
        # Дисплей для вывода времени
        self.dsp = QLCDNumber(self)
        self.dsp.move(150, 0)
        self.dsp.resize(200, 50)
        self.dsp.setDigitCount(13)
        self.dsp.display('00:00:00.000')
        # Список со значениями секундомера
        self.lst_times = QListWidget(self)
        self.lst_times.move(125, 100)
        self.lst_times.resize(250, 300)
        # Таймер
        self.nTimer = QTimer()
        self.nTimer.timeout.connect(self.repeatTime)

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Секундомер')

    def start(self):
        # Инициализируем при старте первое значение в списке
        self.num = 1
        # Устанавливаем всё значение времени на ноль
        self.time_in_ms = 0
        self.time_in_s = 0
        self.time_in_m = 0
        self.time_in_h = 0
        # Махинация с показом кнопок
        self.btn_drop.setVisible(True)
        self.btn_split.setVisible(True)
        self.btn_pause.setVisible(True)
        # Запускаем таймер на 1 мс
        self.nTimer.start(1)

    def repeatTime(self):
        # При каждом тике таймера кол-во мс в секундомере увеличивается на 1, остальные значения правильно форматируются
        self.time_in_ms += 1
        if self.time_in_ms == 1000:
            self.time_in_s += 1
            self.time_in_ms = 0
        if self.time_in_s == 60:
            self.time_in_m += 1
            self.time_in_s = 0
        if self.time_in_m == 60:
            self.time_in_h += 1
            self.time_in_m = 0
        # Переводим их в строку
        ms = str(self.time_in_ms)
        s = str(self.time_in_s)
        m = str(self.time_in_m)
        h = str(self.time_in_h)
        # Форматируем значения к виду hh:mm:ss.mss
        if len(s) == 1:
            s = '0' + s
        if len(m) == 1:
            m = '0' + m
        if len(h) == 1:
            h = '0' + h
        if len(ms) == 1:
            ms = '00' + ms
        if len(ms) == 2:
            ms = '0' + ms
        # Сохраняем в едином виде и показываем в дисплее
        self.time = h + ":" + m + ':' + s + '.' + ms
        self.dsp.display(self.time)

    def drop(self):
        # Останавливаем таймер и сбрасываем время на дисплее
        self.nTimer.stop()
        self.dsp.display('00:00:00.000')
        # Махинации с показом кнопок
        self.btn_pause.setVisible(False)
        self.btn_split.setVisible(False)
        self.btn_drop.setVisible(False)
        self.btn_start.setVisible(True)
        self.btn_continue.setVisible(False)
        # Сбрасываем список значений и устанавливаем, что следующее значение будет первым
        self.lst_times.clear()
        self.num = 1

    def pause(self):
        # Сохраняем на чем остановился таймер
        self.inter = self.nTimer.remainingTime()
        self.nTimer.stop()
        # Махинация с показом кнопок
        self.btn_continue.setVisible(True)
        self.btn_pause.setVisible(False)

    def timer_continue(self):
        # Запускаем с того места, на котором остановили
        self.nTimer.start(self.inter)
        # Махинации с покахом кнопок
        self.btn_pause.setVisible(True)
        self.btn_continue.setVisible(False)

    def spliting(self):
        # Сохраняем данное значение времени в списке
        self.lst_times.addItem(str(self.num) + '. ' + self.time)
        # Делаем следующее значение на один больше, чем предыдущее
        self.num += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StopwatchWidget()
    ex.show()
    sys.exit(app.exec_())
