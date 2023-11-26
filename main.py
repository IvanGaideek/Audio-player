import sys
import os
import information
import Album
import sqlite3

from music_ui import Ui_MainWindow
from PyQt5.QtCore import QUrl, QTimer
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QStyle
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from YoutubeDownload import MusicYtApp
from URadio import ChangeRadio


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # загрузка главного интерфейса
        self.dir = ''  # путь на ресурс музыки
        self.flag_play = False  # разрешение на проигрывание следующего трека после предыдущего автоматически
        self.flag_radio = False
        self.album_songs = dict()
        self.initUI()

    def initUI(self):
        '''Метод, где приклепляются функции к элементам интерфейса.'''
        self.listMusics.itemDoubleClicked.connect(self.record)
        # установка иконки(иконка из библиотеки PyQt5)
        self.play_music.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_music.clicked.connect(self.stop_or_play)
        self.last.clicked.connect(self.last_music)
        self.next.clicked.connect(self.next_music)

        actions = [self.action, self.action_YouTube, self.action_6, self.action_5, self.action_4, self.action_2,
                   self.action_3]
        for act in actions:
            act.triggered.connect(self.menuAction)  # подключает функцию к действию

        self.musics_slider.setRange(0, 0)  # фиксирует слайдер пока не была включена музыка
        self.last.setEnabled(False)  # блокирование кнопок
        self.next.setEnabled(False)

    def stop_or_play(self):
        '''Определяет какой метод запустить.'''
        try:
            if self.flag_play:  # проверка играет ли музыка
                self.stop()
            elif self.media_player.state() == QMediaPlayer.PlayingState:  # проверка играет ли музыка
                self.stop()
            else:
                self.play()
        except AttributeError:
            pass

    def stop(self):
        self.flag_play = False
        position = self.media_player.position() - 10  # текущая позиция воспроизведения
        self.media_player.stop()
        self.play_music.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.media_player.setPosition(position)  # установка положение воспроизведения в сохраненное положение
        self.musics_slider.setValue(position)  # установка ползунка в положение остановки
        if not self.flag_radio:
            self.management_slider.update_time()  # установка времени в положение остановки

    def record(self):
        self.item = self.listMusics.currentItem()  # выбранный трек в списке
        self.playMusic()

    def play_radio(self):
        self.play()

    def playMusic(self):
        self.statusbar.showMessage('')
        if self.flag_radio:
            self.play_radio()
            self.title_music.setText('Радио:' + self.item.text())
            self.musics_slider.setRange(0, 0)  # фиксирует слайдер
            self.time.setText('00:00')
            self.play_music.setEnabled(True)
            try:
                self.timer.stop()  # отключает таймер
            except AttributeError:
                pass
        else:
            if self.album_songs:
                if not os.path.isfile(self.get_song_path(self.album_songs[self.item.text()])):
                    # проверка есть ли по такому пути файл
                    self.listMusics.takeItem(self.listMusics.row(self.item))
                    self.statusbar.showMessage('Файл не найден! Он будет удалён.')
                    self.delete_song(self.album_songs[self.item.text()], self.item.text())
                else:
                    content = QMediaContent(QUrl.fromLocalFile(
                        self.get_song_path(self.album_songs[self.item.text()])))  # загружает музыку
                    self.title_music.setText(self.item.text().split('.')[0])
                    self.enabling_play(content)
                    self.statusbar.showMessage('')
            elif self.item:
                file_name = os.path.join(self.dir, self.item.text())
                content = QMediaContent(QUrl.fromLocalFile(file_name))  # загружает музыку
                self.title_music.setText(self.item.text().split('.')[0])
                self.enabling_play(content)
            self.last.setEnabled(True)  # разблокирование кнопок
            self.next.setEnabled(True)
            self.play_music.setEnabled(True)

    def enabling_play(self, content):
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(content)
        self.media_player.stateChanged.connect(
            self.state_change_music)  # сигнал состояния музыки(закончила играть, не закончила играть)
        self.management_slider = MySlider(self)  # класс управления ползунком и временем
        self.media_player.positionChanged.connect(
            self.management_slider.update_slider)  # сигнал изменения позиции проигрывания
        self.media_player.durationChanged.connect(
            self.management_slider.update_duration)  # сигнал изменения длительности
        self.play()

    def delete_song(self, song_id, song_name):
        '''Удаляет трек из плейлиста.'''
        conn = sqlite3.connect('albums.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Songs WHERE song_id = ? AND song_name = ?", (song_id, song_name))
        conn.commit()
        conn.close()

    def play(self):
        try:
            if self.flag_radio:
                self.media_content = QMediaContent(QUrl(self.url_radio[self.item.text()]))
                self.media_player = QMediaPlayer()
                self.media_player.setMedia(self.media_content)
            self.flag_play = True
            self.media_player.play()
            self.play_music.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.statusbar.showMessage('')
        except Exception:
            self.statusbar.showMessage('Невозможно проигрывание.')

    def state_change_music(self, state):
        '''Регистрирует когда трек закончил проигрывать'''
        if not state and self.flag_play:
            self.next_music()

    def next_music(self):
        try:
            if self.item:
                length = self.listMusics.count()
                if self.listMusics.row(self.item) + 1 < length:
                    next_item = self.listMusics.row(self.item) + 1  # номер объект находящийся ниже по списку
                else:
                    next_item = 0
                self.item = self.listMusics.item(next_item)  # вытаскиваем объект по индексу
                self.playMusic()
        except AttributeError:
            print('не выбран был ни один трек')

    def last_music(self):
        try:
            if self.item:
                if self.listMusics.row(self.item):
                    previous_item = self.listMusics.row(self.item) - 1  # номер объект находящийся выше по списку
                else:
                    previous_item = self.listMusics.count() - 1
                self.item = self.listMusics.item(previous_item)
                self.playMusic()
        except AttributeError:
            print('не выбран был ни один трек')

    def get_song_path(self, song_id):
        # Соединение с базой данных
        conn = sqlite3.connect('albums.db')
        c = conn.cursor()
        # Выполнение SQL-запроса для извлечения пути трека из базы данных
        c.execute("SELECT song_path FROM Songs WHERE song_id=?", (song_id,))
        result = c.fetchone()
        # Проверка, был ли получен результат
        if result is not None:
            song_path = result[0]
        else:
            song_path = None
        # Закрытие соединения с базой данных
        conn.close()
        return song_path

    @QtCore.pyqtSlot()
    def menuAction(self):
        action = self.sender()
        MyAction(action, self)  # создание класса для выполнения действия относящегося к нажатому элементу меню


class MyAction:
    def __init__(self, action, window):
        self.window = window
        if action.text() == 'открыть':
            self.load(window)
        elif action.text() == 'скачать с YouTube':
            self.window.obj = MusicYtApp()
            self.launch()
        elif action.text() == 'Добавить поток':
            self.window.obj = ChangeRadio()
            self.launch()
        elif action.text() == 'Открыть имеющиеся потоки':
            self.open()
        elif action.text() == 'Описания пользования':
            self.window.obj = information.Widget()
            self.launch()
        elif action.text() == 'Создать':
            self.window.obj = Album.CUalbum()
            self.launch()
        elif action.text() == 'Открыть':
            self.window.obj = Album.OUalbum(window)
            self.launch()

    def load(self, window):
        window.listMusics.clear()
        dir = QFileDialog.getExistingDirectory(window,
                                               'Выбор папки с треками')  # создание диалогового окна для выбора файлов
        if dir:
            for file_name in os.listdir(dir):
                if file_name.endswith('.mp3') or file_name.endswith('.wav'):  # проверка расширения файла
                    window.listMusics.addItem(file_name)  # добавление пункта в списке
            window.flag_radio = False
            window.dir = dir
        window.album_songs = dict()
        window.play_music.setEnabled(False)  # блокирование кнопок
        window.title_playlist.setText('Альбом: ...')

    def launch(self):
        '''Запускает приложение'''
        self.window.obj.show()

    def open(self):
        self.window.listMusics.clear()
        self.window.url_radio = {}
        for rtitle, url in ChangeRadio.radio_return():  # перебор списка из radio_url.csv
            self.window.listMusics.addItem(rtitle)
            self.window.url_radio[rtitle] = url
        self.window.flag_radio = True
        self.window.title_playlist.setText('Альбом: потоки радио')
        self.window.last.setEnabled(False)  # блокирование кнопок
        self.window.next.setEnabled(False)
        self.window.play_music.setEnabled(False)


class MySlider:
    def __init__(self, window):
        self.wind = window
        # Подключение сигнала sliderMoved слайдера к методу set_position
        self.wind.musics_slider.sliderMoved.connect(self.set_position)
        self.wind.timer = QTimer()  # Создание экземпляра QTimer для обновления времени
        self.wind.timer.setInterval(1000)  # Обновление времени каждые 1000 миллисекунд
        self.wind.timer.timeout.connect(self.update_time)  # Подключение сигнала timeout таймера к методу
        self.wind.timer.start()

    def update_slider(self, position):
        '''Установка значения слайдера в соответствии с позицией проигрывания'''
        if self.wind.flag_play:
            self.wind.musics_slider.setValue(position)

    def update_duration(self, duration):
        '''Установка максимального значения слайдера в соответствии с длительностью проигрывания'''
        self.wind.musics_slider.setMaximum(duration)

    def set_position(self, position):
        '''Установка позиции проигрывания для media_player '''
        self.wind.media_player.setPosition(position)

    def update_time(self):
        minutes = '0' + str(self.wind.media_player.position() // 60000)
        second = '0' + str((self.wind.media_player.position() % 60000) // 1000)  # Преобразование позиции в секунды
        self.wind.time.setText(f"{minutes[-2:]}:{second[-2:]}")


def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
