import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLCDNumber
from PyQt5.QtCore import QTime, QTimer, QDateTime, QDate
from PyQt5.QtGui import QFont


class TimesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Вывод даты
        self.lbl_data = QLabel('Сегодня: ' + QDate.currentDate().toString('dd.MM.yyyy'), self)
        self.lbl_data.setFont(QFont('Times', 15))
        self.lbl_data.move(150, 25)
        # Вывод дисплеев и текстов со временем в различных поясах России, включая ваше время
        self.lcd_mine = QLCDNumber(self)
        self.lcd_mine.move(200, 50)
        self.lcd_mine.resize(100, 50)

        self.lbl_mine = QLabel('Ваше время', self)
        self.lbl_mine.move(210, 100)
        self.lbl_mine.setFont(QFont('Times', 12))

        self.lcd_kal = QLCDNumber(self)
        self.lcd_kal.resize(100, 50)
        self.lcd_kal.move(50, 125)

        self.lbl_kal = QLabel('Калининградское время', self)
        self.lbl_kal.move(25, 175)
        self.lbl_kal.setFont(QFont('Times', 10))

        self.lcd_msk = QLCDNumber(self)
        self.lcd_msk.resize(100, 50)
        self.lcd_msk.move(200, 125)

        self.lbl_msk = QLabel('Московское время', self)
        self.lbl_msk.move(195, 175)
        self.lbl_msk.setFont(QFont('Times', 10))

        self.lcd_sam = QLCDNumber(self)
        self.lcd_sam.resize(100, 50)
        self.lcd_sam.move(350, 125)

        self.lbl_sam = QLabel('Самарское время', self)
        self.lbl_sam.move(350, 175)
        self.lbl_sam.setFont(QFont('Times', 10))

        self.lcd_ekb = QLCDNumber(self)
        self.lcd_ekb.resize(100, 50)
        self.lcd_ekb.move(50, 200)

        self.lbl_ekb = QLabel('Екатеринбургское время', self)
        self.lbl_ekb.move(25, 250)
        self.lbl_ekb.setFont(QFont('Times', 10))

        self.lcd_omsk = QLCDNumber(self)
        self.lcd_omsk.resize(100, 50)
        self.lcd_omsk.move(200, 200)

        self.lbl_omsk = QLabel('Омское время', self)
        self.lbl_omsk.move(210, 250)
        self.lbl_omsk.setFont(QFont('Times', 10))

        self.lcd_kras = QLCDNumber(self)
        self.lcd_kras.resize(100, 50)
        self.lcd_kras.move(350, 200)

        self.lbl_kras = QLabel('Красноярское время', self)
        self.lbl_kras.move(340, 250)
        self.lbl_kras.setFont(QFont('Times', 10))

        self.lcd_irk = QLCDNumber(self)
        self.lcd_irk.resize(100, 50)
        self.lcd_irk.move(50, 275)

        self.lbl_irk = QLabel('Иркутское время', self)
        self.lbl_irk.move(50, 325)
        self.lbl_irk.setFont(QFont('Times', 10))

        self.lcd_yakut = QLCDNumber(self)
        self.lcd_yakut.resize(100, 50)
        self.lcd_yakut.move(200, 275)

        self.lbl_yakut = QLabel('Якутское время', self)
        self.lbl_yakut.move(205, 325)
        self.lbl_yakut.setFont(QFont('Times', 10))

        self.lcd_vldv = QLCDNumber(self)
        self.lcd_vldv.resize(100, 50)
        self.lcd_vldv.move(350, 275)

        self.lbl_vldv = QLabel('Владивостокское время', self)
        self.lbl_vldv.move(330, 325)
        self.lbl_vldv.setFont(QFont('Times', 10))

        self.lcd_mgdn = QLCDNumber(self)
        self.lcd_mgdn.resize(100, 50)
        self.lcd_mgdn.move(100, 350)

        self.lbl_mgdn = QLabel('Магаданское время', self)
        self.lbl_mgdn.move(90, 400)
        self.lbl_mgdn.setFont(QFont('Times', 10))

        self.lcd_kamch = QLCDNumber(self)
        self.lcd_kamch.resize(100, 50)
        self.lcd_kamch.move(300, 350)

        self.lbl_kamch = QLabel('Камчатское время', self)
        self.lbl_kamch.move(297, 400)
        self.lbl_kamch.setFont(QFont('Times', 10))
        # Запускаем таймер для обновления времени
        self.nTimer = QTimer()
        self.nTimer.timeout.connect(self.repeatTime)
        self.nTimer.start()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Время')

    def repeatTime(self):
        # Обновляем дату, мало ли юзер зайдет в 23:59
        self.lbl_data.setText('Сегодня: ' + QDate.currentDate().toString('dd.MM.yyyy'))
        # Вытаскиваем системное время и выводим его
        self.time_mine = QTime().currentTime().toString('hh:mm')
        self.lcd_mine.display(self.time_mine)
        # Находим разницу системного времени от UTC
        now = QDateTime.currentDateTime()
        offset = now.offsetFromUtc() // 3600
        # Находим разницу между вашим и московским временем от UTC
        offset_your_and_msk = offset - 3
        time_mine_hour = int(self.time_mine.split(':')[0])
        time_mine_min = str(int(self.time_mine.split(':')[1]))
        if len(time_mine_min) == 1:
            time_mine_min = '0' + time_mine_min
        # Проверяем не отрицательные ли часы и выводим время
        if time_mine_hour - offset_your_and_msk - 1 < 0:
            kal_hour = 24 - time_mine_hour - offset_your_and_msk - 1
        elif time_mine_hour - offset_your_and_msk - 1 > 23:
            kal_hour = time_mine_hour - offset_your_and_msk - 1 - 24
        else:
            kal_hour = time_mine_hour - offset_your_and_msk - 1
        self.lcd_kal.display(str(kal_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk < 0:
            msk_hour = 24 - time_mine_hour - offset_your_and_msk
        elif time_mine_hour - offset_your_and_msk > 23:
            msk_hour = time_mine_hour - offset_your_and_msk - 24
        else:
            msk_hour = time_mine_hour - offset_your_and_msk
        self.lcd_msk.display(str(msk_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 1 < 0:
            sam_hour = 24 - time_mine_hour - offset_your_and_msk + 1
        elif time_mine_hour - offset_your_and_msk + 1 > 23:
            sam_hour = time_mine_hour - offset_your_and_msk + 1 - 24
        else:
            sam_hour = time_mine_hour - offset_your_and_msk + 1
        self.lcd_sam.display(str(sam_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 2 < 0:
            ekb_hour = 24 - time_mine_hour - offset_your_and_msk + 2
        elif time_mine_hour - offset_your_and_msk + 2 > 23:
            ekb_hour = time_mine_hour - offset_your_and_msk + 2 - 24
        else:
            ekb_hour = time_mine_hour - offset_your_and_msk + 2
        self.lcd_ekb.display(str(ekb_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 3 < 0:
            omsk_hour = 24 - time_mine_hour - offset_your_and_msk + 3
        elif time_mine_hour - offset_your_and_msk + 3 > 23:
            omsk_hour = time_mine_hour - offset_your_and_msk + 3 - 24
        else:
            omsk_hour = time_mine_hour - offset_your_and_msk + 3
        self.lcd_omsk.display(str(omsk_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 4 < 0:
            kras_hour = 24 - time_mine_hour - offset_your_and_msk + 4
        elif time_mine_hour - offset_your_and_msk + 4 > 23:
            kras_hour = time_mine_hour - offset_your_and_msk + 4 - 24
        else:
            kras_hour = time_mine_hour - offset_your_and_msk + 4
        self.lcd_kras.display(str(kras_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 5 < 0:
            irk_hour = 24 - time_mine_hour - offset_your_and_msk + 5
        elif time_mine_hour - offset_your_and_msk + 5 > 23:
            irk_hour = time_mine_hour - offset_your_and_msk + 5 - 24
        else:
            irk_hour = time_mine_hour - offset_your_and_msk + 5
        self.lcd_irk.display(str(irk_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 6 < 0:
            yakut_hour = 24 - time_mine_hour - offset_your_and_msk + 6
        elif time_mine_hour - offset_your_and_msk + 6 > 23:
            yakut_hour = time_mine_hour - offset_your_and_msk + 6 - 24
        else:
            yakut_hour = time_mine_hour - offset_your_and_msk + 6
        self.lcd_yakut.display(str(yakut_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 7 < 0:
            vldv_hour = 24 - time_mine_hour - offset_your_and_msk + 7
        elif time_mine_hour - offset_your_and_msk + 7 > 23:
            vldv_hour = time_mine_hour - offset_your_and_msk + 7 - 24
        else:
            vldv_hour = time_mine_hour - offset_your_and_msk + 7
        self.lcd_vldv.display(str(vldv_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 8 < 0:
            mgdn_hour = 24 - time_mine_hour - offset_your_and_msk + 8
        elif time_mine_hour - offset_your_and_msk + 8 > 23:
            mgdn_hour = time_mine_hour - offset_your_and_msk + 8 - 24
        else:
            mgdn_hour = time_mine_hour - offset_your_and_msk + 8
        self.lcd_mgdn.display(str(mgdn_hour) + ':' + time_mine_min)

        if time_mine_hour - offset_your_and_msk + 9 < 0:
            kamch_hour = 24 - time_mine_hour - offset_your_and_msk + 9
        elif time_mine_hour - offset_your_and_msk + 9 > 23:
            kamch_hour = time_mine_hour - offset_your_and_msk + 9 - 24
        else:
            kamch_hour = time_mine_hour - offset_your_and_msk + 9
        self.lcd_kamch.display(str(kamch_hour) + ':' + time_mine_min)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimesWidget()
    ex.show()
    sys.exit(app.exec_())
