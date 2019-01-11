import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLCDNumber, QTimeEdit, QPushButton, QFileDialog, QRadioButton
from PyQt5.QtCore import QTime, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtGui import QFont


class AlarmWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Флаг, чтобы функция вызова будильника не вызвыалась с каждым тиком
        self.flag_get_up = True
        # Нулевое время для сброса часов
        self.zero_time = QTime(0, 0)
        # Пустая ссылка
        self.url = QUrl()
        # Инициализируем плеер и плейлист, который после зацикливаем
        self.playlist = QMediaPlaylist(self)
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player = QMediaPlayer()
        # Кнопка для выбора файла с музыкой
        self.btn_getfile = QPushButton('Выбрать файл', self)
        self.btn_getfile.setFont(QFont('Times', 10))
        self.btn_getfile.move(142.5, 25)
        self.btn_getfile.resize(215, 50)
        self.btn_getfile.setVisible(False)
        self.btn_getfile.clicked.connect(self.getfile)
        # Радио-кнопка для включения будильника
        self.radio_btn1 = QRadioButton('вкл', self)
        self.radio_btn1.move(0, 15)
        self.radio_btn1.setFont(QFont('Times', 10))
        self.radio_btn1.toggled.connect(self.on_off)
        # Радио-кнопка для выключения будильника
        self.radio_btn2 = QRadioButton('выкл', self)
        self.radio_btn2.move(0, 40)
        self.radio_btn2.setChecked(True)
        self.radio_btn2.setFont(QFont('Times', 10))
        self.radio_btn2.toggled.connect(self.on_off)
        # Значение будильника
        self.timer_edit = QTimeEdit(self)
        self.timer_edit.setDisplayFormat('hh:mm')
        self.timer_edit.move(200, 110)
        self.timer_edit.resize(100, 50)
        self.timer_edit.setFont(QFont('Times', 18, QFont.Bold))
        self.timer_edit.setVisible(False)
        # Бирка
        self.lbl = QLabel('Будильник:', self)
        self.lbl.move(0, 0)
        self.lbl.setFont(QFont('Times', 10))
        # Подсказка для кнопки выбора мелодии
        self.lbl2 = QLabel('Выберите мелодию для будильника:', self)
        self.lbl2.move(142.5, 0)
        self.lbl2.setVisible(False)
        self.lbl2.setFont(QFont('Times', 10))
        # Бирка
        self.lbl3 = QLabel('Будильник установлен на:', self)
        self.lbl3.move(175, 185)
        self.lbl3.setFont(QFont('Times', 10))
        self.lbl3.setVisible(False)
        # Бирка
        self.lbl4 = QLabel('Установите время будильника:', self)
        self.lbl4.move(150, 85)
        self.lbl4.setFont(QFont('Times', 10))
        self.lbl4.setVisible(False)
        # Кнопка выключения будильника, когда он сработает
        self.btn = QPushButton('Выключить\nбудильник', self)
        self.btn.clicked.connect(self.awake)
        self.btn.resize(100, 100)
        self.btn.move(200, 200)
        self.btn.setFont(QFont('Times', 11, QFont.ExtraBold))
        self.btn.setVisible(False)
        # Дисплей для вывода значения будильника
        self.dis2 = QLCDNumber(self)
        self.dis2.move(200, 210)
        self.dis2.resize(100, 50)
        self.dis2.setVisible(False)
        # Дисплей с текущим временем
        self.dis1 = QLCDNumber(self)
        self.dis1.move(375, 25)
        self.dis1.resize(100, 50)
        # Бирка
        self.lbl5 = QLabel('Сейчас:', self)
        self.lbl5.move(375, 0)
        self.lbl5.setFont(QFont('Times', 10))
        # Таймер
        self.nTimer = QTimer()
        self.nTimer.timeout.connect(self.repeatTime)
        self.nTimer.start()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Будильник')

    def repeatTime(self):
        # Вытаскиваем системное время и преобразуем в строку
        self.time = QTime().currentTime()
        time_text = self.time.toString('hh:mm')
        # Вытаскиваем выставленное значение будильника и преобразуем в строку
        timer = self.timer_edit.time()
        timer_text = timer.toString('hh:mm')
        # Выводим значения будильника на дисплей
        self.dis2.display(timer_text)
        # Выводим текущее время
        self.dis1.display(time_text)
        # Проверяем условия срабатывания будильника
        if timer_text == time_text and self.flag_get_up and self.radio_btn1.isChecked():
            self.flag_get_up = False
            self.get_up()
        else:
            self.flag_get_up = True

    def awake(self):
        # Устанавливаем нулевое значение времени будильника
        self.timer_edit.setTime(self.zero_time)
        # Махинация с показом виджетов
        self.lbl.setVisible(True)
        self.lbl2.setVisible(True)
        self.lbl3.setVisible(True)
        self.lbl4.setVisible(True)
        self.radio_btn1.setVisible(True)
        self.radio_btn2.setVisible(True)
        self.btn_getfile.setVisible(True)
        self.dis2.setVisible(True)
        self.timer_edit.setVisible(True)
        self.btn.setVisible(False)
        # Останавливаем музыку
        self.player.stop()

    def get_up(self):
        # Махинации с показом виджетов
        self.lbl.setVisible(False)
        self.lbl2.setVisible(False)
        self.lbl3.setVisible(False)
        self.lbl4.setVisible(False)
        self.radio_btn1.setVisible(False)
        self.radio_btn2.setVisible(False)
        self.btn_getfile.setVisible(False)
        self.dis2.setVisible(False)
        self.timer_edit.setVisible(False)
        self.btn.setVisible(True)
        # Включаем музыку
        self.player.play()

    def getfile(self):
        # Достаем файл с мелодией и сохраняем её путь
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home', 'Audio Files (*mp3 *wav)')
        self.url = QUrl.fromLocalFile(fname[0])
        # Устанавливаем музыку в плеер
        self.content = QMediaContent(self.url)
        self.playlist.clear()
        self.playlist.addMedia(self.content)
        self.player.setPlaylist(self.playlist)

    def on_off(self):
        # Включаем/выключаем будильник
        if self.radio_btn1.isChecked():
            self.btn_getfile.setVisible(True)
            self.timer_edit.setVisible(True)
            self.dis2.setVisible(True)
            self.lbl2.setVisible(True)
            self.lbl3.setVisible(True)
            self.lbl4.setVisible(True)
        else:
            self.btn_getfile.setVisible(False)
            self.timer_edit.setVisible(False)
            self.dis2.setVisible(False)
            self.lbl2.setVisible(False)
            self.lbl3.setVisible(False)
            self.lbl4.setVisible(False)
            self.timer_edit.setTime(self.zero_time)
            self.btn.setVisible(False)
            self.player.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlarmWidget()
    ex.show()
    sys.exit(app.exec_())
