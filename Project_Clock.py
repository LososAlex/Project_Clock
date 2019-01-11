import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget, QHBoxLayout
from times import TimesWidget
from stopwatch import StopwatchWidget
from alarm import AlarmWidget
from Timer import TimerWidget


class Project_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Делаем макет для виджетов
        layer = QVBoxLayout(self)
        # Стакуем виджеты
        self.stack = QStackedWidget()
        self.stack.addWidget(TimesWidget())
        self.stack.addWidget(AlarmWidget())
        self.stack.addWidget(StopwatchWidget())
        self.stack.addWidget(TimerWidget())
        # Кнопка для показа виджета времени
        self.btn_times = QPushButton('Время', self)
        self.btn_times.move(0, 0)
        self.btn_times.resize(100, 25)
        self.btn_times.clicked.connect(self.times_on)
        # Кнопка для показа виджета будильника
        self.btn_alarm = QPushButton('Будильник', self)
        self.btn_alarm.move(100, 0)
        self.btn_alarm.resize(100, 25)
        self.btn_alarm.clicked.connect(self.alarm_on)
        # Кнопка для показа виджета секундомера
        self.btn_stopwatch = QPushButton('Секундомер', self)
        self.btn_stopwatch.move(200, 0)
        self.btn_stopwatch.resize(100, 25)
        self.btn_stopwatch.clicked.connect(self.stopwatch_on)
        # Кнопка для показа виджета таймера
        self.btn_timer = QPushButton('Таймер', self)
        self.btn_timer.move(300, 0)
        self.btn_timer.resize(100, 25)
        self.btn_timer.clicked.connect(self.timer_on)
        # Макет для кнопок
        btnLayout = QHBoxLayout()
        # Добавление кнопок в мает
        btnLayout.addWidget(self.btn_times)
        btnLayout.addWidget(self.btn_alarm)
        btnLayout.addWidget(self.btn_stopwatch)
        btnLayout.addWidget(self.btn_timer)
        # Добавление макета кнопок и стака с виджетами в основной макет
        layer.addWidget(self.stack)
        layer.addLayout(btnLayout)

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Часы')

    def times_on(self):
        self.stack.setCurrentIndex(0)

    def alarm_on(self):
        self.stack.setCurrentIndex(1)

    def stopwatch_on(self):
        self.stack.setCurrentIndex(2)

    def timer_on(self):
        self.stack.setCurrentIndex(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project_Clock()
    ex.show()
    sys.exit(app.exec_())
