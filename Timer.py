import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLCDNumber, QTimeEdit, QPushButton, QFileDialog
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtGui import QFont


class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Инициализируем плеер и плейлист, на котором поставим цикличное воспроизведение
        self.playlist = QMediaPlaylist(self)
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player = QMediaPlayer()
        # Создадим пустую ссылку, чтобы программа не крашилась, если пользователь не выберет мелодию
        self.url = QUrl()
        # Подскажем для чего кнопка
        self.lbl = QLabel('Выберите мелодию для таймера:', self)
        self.lbl.move(165, 100)
        # Кнопка для выбора файла с мелодией
        self.btn_getfile = QPushButton('Выбрать файл', self)
        self.btn_getfile.move(200, 125)
        self.btn_getfile.resize(100, 50)
        self.btn_getfile.clicked.connect(self.getfile)
        # Кнопка старта таймера
        self.btn_start = QPushButton('Старт', self)
        self.btn_start.move(225, 225)
        self.btn_start.resize(50, 50)
        self.btn_start.clicked.connect(self.start_timer)
        # Кнопка остановки таймера до того, как он закончит отсчет
        self.btn_stop = QPushButton('Стоп', self)
        self.btn_stop.move(250, 225)
        self.btn_stop.resize(50, 50)
        self.btn_stop.clicked.connect(self.stop_timer)
        self.btn_stop.setVisible(False)
        # Кнопка паузы таймера
        self.btn_pause = QPushButton('Пауза', self)
        self.btn_pause.move(200, 225)
        self.btn_pause.resize(50, 50)
        self.btn_pause.clicked.connect(self.pause_timer)
        self.btn_pause.setVisible(False)
        # Кнопка для продолжения отсчета таймера
        self.btn_continue = QPushButton('Дальше', self)
        self.btn_continue.move(200, 225)
        self.btn_continue.resize(50, 50)
        self.btn_continue.clicked.connect(self.continue_timer)
        self.btn_continue.setVisible(False)
        # Кнопка для выключения таймера, когда он закончит отсчет
        self.btn_off = QPushButton('Выкл', self)
        self.btn_off.move(225, 225)
        self.btn_off.resize(50, 50)
        self.btn_off.clicked.connect(self.timer_off)
        self.btn_off.setVisible(False)
        # Спрашивваем значение таймера
        self.get_timer = QTimeEdit(self)
        self.get_timer.move(185, 175)
        self.get_timer.resize(130, 50)
        self.get_timer.setFont(QFont('Times', 15, QFont.Bold))
        self.get_timer.setDisplayFormat('HH:mm:ss')
        # Дисплей для вывода таймера
        self.dsp = QLCDNumber(self)
        self.dsp.resize(200, 50)
        self.dsp.move(150, 175)
        self.dsp.setVisible(False)
        self.dsp.setDigitCount(8)
        # Таймер
        self.nTimer = QTimer()
        self.nTimer.timeout.connect(self.timer)

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Таймер')

    def start_timer(self):
        # Добавляем мелодию в плеер
        self.content = QMediaContent(self.url)
        self.playlist.addMedia(self.content)
        self.player.setPlaylist(self.playlist)
        # Выводим начальное значение времени на дисплей
        self.dsp.display(self.get_timer.time().toString('hh:mm:ss'))
        # Переводим время в секунды
        timer = self.get_timer.time()
        timer_text = timer.toString('hh:mm:ss')
        timer_int = list(map(lambda x: int(x), timer_text.split(':')))
        self.timer_in_sec = timer_int[0]*3600 + timer_int[1]*60 + timer_int[2]
        # Проверяем не установили ли нулевое значение
        if self.timer_in_sec == 0:
            self.timer_timeout()
        else:
            # Запускаем таймер
            self.nTimer.start(1000)
            # Махинации с показом кнопок
            self.btn_start.setVisible(False)
            self.btn_pause.setVisible(True)
            self.btn_stop.setVisible(True)
            self.dsp.setVisible(True)
            self.get_timer.setVisible(False)
            self.lbl.setVisible(False)
            self.btn_getfile.setVisible(False)

    def timer(self):
        # Функция обновления таймера и дисплея со временем
        # Делаем обратный отсчет, отнимая каждую секунду единицу из начального значения
        self.timer_in_sec -= 1
        # Переводим целочисленные значения в строку
        timer_text = list(map(lambda x: str(x), [self.timer_in_sec // 3600,
                                                 (self.timer_in_sec % 3600) // 60,
                                                 (self.timer_in_sec % 3600) % 60]))
        # Если один символ, то к нему добавляется ноль
        if len(timer_text[0]) == 1:
            timer_text[0] = '0' + timer_text[0]
        if len(timer_text[1]) == 1:
            timer_text[1] = '0' + timer_text[1]
        if len(timer_text[2]) == 1:
            timer_text[2] = '0' + timer_text[2]
        # Объединяем список в формат hh:mm:ss
        timer_text = ':'.join(timer_text)
        # Выводим текст со временем на дисплей
        self.dsp.display(timer_text)
        # Если таймер дошел до нуля:
        if self.timer_in_sec == 0:
            self.timer_timeout()
        else:
            # Обновляем таймер
            self.nTimer.start(1000)

    def stop_timer(self):
        # Останавливаем таймер
        self.nTimer.stop()
        # Махинации с кнопками
        self.btn_start.setVisible(True)
        self.btn_stop.setVisible(False)
        self.btn_pause.setVisible(False)
        self.dsp.setVisible(False)
        self.btn_continue.setVisible(False)
        self.get_timer.setVisible(True)
        self.btn_getfile.setVisible(True)
        self.lbl.setVisible(True)

    def continue_timer(self):
        # Продолжаем таймер с того места, где остановились
        self.nTimer.start(self.inter)
        # Махинации с показом кнопок
        self.btn_continue.setVisible(False)
        self.btn_pause.setVisible(True)

    def pause_timer(self):
        # Ловим оставшееся время таймера
        self.inter = self.nTimer.remainingTime()
        # Останавливаем таймер и делаем махинации с показом кнопок
        self.nTimer.stop()
        self.btn_pause.setVisible(False)
        self.btn_continue.setVisible(True)

    def timer_off(self):
        # Махинации с кнопками
        self.btn_start.setVisible(True)
        self.dsp.setVisible(False)
        self.get_timer.setVisible(True)
        self.btn_off.setVisible(False)
        self.btn_getfile.setVisible(True)
        self.lbl.setVisible(True)
        # Останавливаем мелодию
        self.player.stop()

    def timer_timeout(self):
        # Останавливаем таймер
        self.nTimer.stop()
        # Махинации с кнопками
        self.get_timer.setVisible(False)
        self.btn_stop.setVisible(False)
        self.btn_pause.setVisible(False)
        self.btn_continue.setVisible(False)
        self.btn_off.setVisible(True)
        self.dsp.setVisible(True)
        self.lbl.setVisible(False)
        self.btn_getfile.setVisible(False)
        # Запускаем функцию воспроизведения мелодии
        self.playmus()

    def playmus(self):
        # Воспроизводим мелодию
        self.player.play()

    def getfile(self):
        # Достаем файл с мелодией и сохраняем её путь
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home', 'Audio Files (*mp3 *wav)')
        self.url = QUrl.fromLocalFile(fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerWidget()
    ex.show()
    sys.exit(app.exec_())
