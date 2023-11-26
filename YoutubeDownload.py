from pytube import YouTube, Stream
import os
from yt_ui import Ui_YtForm
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import QObject
import threading
import moviepy.editor as mp  # для преобразования расширения из mp4 в mp3


class MusicYtApp(QWidget, Ui_YtForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # загрузка интерфейса
        self.setGeometry(480, 260, 450, 500)
        self.btn_select.clicked.connect(self.select)  # для выбора куда сохранять
        self.btn_download.clicked.connect(self.download)  # подготовка к загрузки звука

    def select(self):
        self.file = QFileDialog.getExistingDirectory(self, "Куда желаете сохранить?")
        if self.file != "":
            self.line_save.setText(self.file)  # путь сохранения записываем
        else:
            pass

    def download(self):
        self.title = self.line_title.text()
        self.url = self.line_url.text()
        self.path = self.line_save.text()
        self.pr = Process(self.label, self.title,
                          self.url, self.path)  # создание класса для внутренних процессов скачивания
        threading.Thread(target=self.pr.download).start()  # поток скачивания звука, его запуск
        self.pr.k_progress.connect(
            self.progress)  # соединение с сигналом для того чтобы progressBar поставил своё максимальное значение

    def progress(self, size):
        self.progressBar.setValue(int(size))  # изменение ProgressBar


class Process(QObject):
    k_progress = QtCore.pyqtSignal(int)  # выдает целочисленный аргумент

    def __init__(self, label, title=None, url=None, path=None):
        super().__init__()
        self.label = label
        self.label.setText('')
        self.title = title
        self.url = url
        self.path = path

    def download(self):
        self.label.setText('Обработка...')
        try:
            yt = YouTube(self.url, use_oauth=True, on_progress_callback=self.change_progress)
            audio = yt.streams.filter(progressive=True,
                                      file_extension='mp4').order_by('resolution').desc().first()
            audio.download(output_path=self.path)
            mp4_filename = os.path.join(self.path, audio.default_filename)
            if self.title.strip():
                mp3_filename = os.path.join(self.path, self.title.strip() + ".mp3")  # преобразование в расширение .mp3
            else:
                mp3_filename = os.path.join(self.path, mp4_filename[:-4] + ".mp3")  # преобразование в расширение .mp3
            mp.AudioFileClip(mp4_filename).write_audiofile(mp3_filename)  # файл переименуется
            os.remove(mp4_filename)  # удаление оригинала
            self.label.setText('Успешно установилось.')
        except Exception as error:
            print(error)
            self.label.setText('Подождите. Возможно что-то пошло не так, но это не точно.')  # вывод ошибки

    def progress(self, percent):
        '''Используется для обработки хода загрузки музыки.'''
        if percent['status'] == 'downloading':  # проверка статуса загрузки
            result = round(percent['downloaded_bytes'] /
                           percent['total_bytes']
                           * 100, 1)  # вычисление процентов на основе загруженных байтов
            self.k_progress.emit(result)

    def change_progress(self, stream: Stream, chunk, bytes):
        '''Вычисления для ProgressBar из потока байт.'''
        size = stream.filesize  # размер файла
        self.label.setText('Началась установка.')
        bytes_res = size - bytes
        # вычисление на основе процентов на основе полученных байтов и общего объёма файла
        percent = round(100.0 * bytes_res / float(size), 1)
        self.k_progress.emit(int(percent))
