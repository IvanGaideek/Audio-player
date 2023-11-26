import os
import sqlite3
from datetime import datetime


from create_album_ui import CUi_Form
from open_album_ui import OUi_Form
from PyQt5.QtWidgets import QWidget, QTableWidget, QFileDialog, QTableWidgetItem


class CUalbum(QWidget, CUi_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # загрузка интерфейса
        self.setGeometry(450, 250, 450, 520)
        self.setFixedSize(530, 450)
        self.create_table()
        self.open_file.clicked.connect(lambda: f_open(self))
        self.add_music.clicked.connect(self.add_table_music)
        self.dir = ''
        self.file_name = ''
        self.delete_2.clicked.connect(self.delete_selected_row)
        self.create_album.clicked.connect(self.createAlbum)

    def create_table(self):
        self.tableWidget.setColumnCount(2)  # Устанавливаем число колонок
        self.tableWidget.setHorizontalHeaderLabels(['Название трека', 'Путь к нему'])
        # Задаем размеры колонок
        self.tableWidget.setColumnWidth(0, 253)
        self.tableWidget.setColumnWidth(1, 253)
        # Запрещаем редактирование ячеек
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def add_table_music(self):
        if len(self.title_music.text().strip()) == 0 or len(self.way_file.text().strip()) == 0:
            self.result.setText('Выберите файл.')
        elif not os.path.isfile(self.way_file.text()) and \
                not (self.way_file.text().endswith('.mp3') or
                     self.way_file.text().endswith('.wav')):  # проверяет верность пути к файлу
            self.result.setText('По такому пути файла не существует.')
        else:
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)  # добавление строчки
            self.tableWidget.setItem(row_count, 0, QTableWidgetItem(self.title_music.text().strip()))
            self.tableWidget.setItem(row_count, 1, QTableWidgetItem(self.way_file.text().strip()))
            self.result.setText('Трек успешно добавился.')

    def delete_selected_row(self):
        selected_row = self.tableWidget.currentRow()  # получение индекса строки которой мы хотим удалить
        if selected_row >= 0:
            self.title_music.setText('')
            self.tableWidget.removeRow(selected_row)  # удаление строки
            self.result.setText('Трек удалена.')
        else:
            self.result.setText('Выберете ячейку строки которой вы хотите удалить.')

    def createAlbum(self):
        songs = self.receiving_data_table
        if len(self.title_album.text().strip()) == 0:
            self.result.setText('Назовите альбом.')
        elif not songs:
            self.result.setText('Плейлист пустой.')
        else:
            # Подключение к базе данных
            conn = sqlite3.connect('albums.db')
            cursor = conn.cursor()
            # Поиск плейлиста с указанным названием
            query = "SELECT * FROM Playlists WHERE playlist_name = ?"
            cursor.execute(query, (self.title_album.text().strip(),))
            result = cursor.fetchone()
            # Закрытие подключения к базе данных
            cursor.close()
            conn.close()
            # Проверка результата запроса
            if result:
                self.result.setText('Такой плейлист(альбом) уже существует.')
            else:
                # Получение текущей даты и времени
                now = datetime.now()
                created_date = now.strftime("%Y-%m-%d %H:%M")
                conn = sqlite3.connect('albums.db')
                cursor = conn.cursor()
                # Вставка нового плейлиста в таблицу "Playlists"
                query = "INSERT INTO Playlists (playlist_name, created_date) VALUES (?, ?)"
                cursor.execute(query, (self.title_album.text().strip(), created_date))
                playlist_id = cursor.lastrowid
                # Вставка песен в таблицу "Songs" и связывание с плейлистом
                for song_name, song_path in songs:
                    query = "INSERT INTO Songs (song_name, song_path, playlist_id) VALUES (?, ?, ?)"
                    cursor.execute(query, (song_name, song_path, playlist_id))
                # Сохранение изменений и закрытие подключения к базе данных
                conn.commit()
                cursor.close()
                conn.close()
                self.result.setText('Плейлист(альбом) успешно создался.')
                self.title_album.setText('')
                self.create_table()

    @property
    def receiving_data_table(self):
        '''Получаем список кортежей (значение из 1 столбца, значение из 2 столбца)'''
        tuples_list = []
        for row in range(self.tableWidget.rowCount()):
            item1 = self.tableWidget.item(row, 0)
            item2 = self.tableWidget.item(row, 1)
            if item1 is not None and item2 is not None:
                tuple_value = (item1.text(), item2.text())
                tuples_list.append(tuple_value)
        return tuples_list

    def clear_table(self):
        self.table_widget.clearContents()  # Очищаем содержимое ячеек
        self.table_widget.setRowCount(0)  # Устанавливаем количество строк равное нулю


class OUalbum(QWidget, OUi_Form):
    def __init__(self, window):
        super().__init__()
        self.setupUi(self)  # загрузка интерфейса
        self.setWindowTitle('Открытие и редактирование альбома')
        self.setGeometry(450, 250, 450, 520)
        self.setFixedSize(530, 450)
        self.create_album.setText('Открыть альбом')
        self.create_table()
        self.dir = ''
        self.file_name = ''
        self.open_file.clicked.connect(lambda: f_open(self))
        self.search_playlists()
        self.title_album.textChanged.connect(self.search_playlists)  # подключение поиска по вводу названия плейлиста
        self.add_music.clicked.connect(self.add_playlist_music)
        self.delete_2.clicked.connect(self.delete_selected_row)
        self.create_album.clicked.connect(self.open_playlist)
        self.window = window

    def add_playlist_music(self):
        '''Добавляет в выбранный плейлист песню.'''
        song_path = self.way_file.text().strip()  # Путь к песне
        song_name = self.title_music.text().strip()  # Название песни
        if len(song_name.strip()) == 0 or len(song_path.strip()) == 0:
            self.result.setText('Выберите файл.')
        elif not os.path.isfile(self.way_file.text()) and \
                not (song_path.endswith('.mp3') or
                     song_path.endswith('.wav')):  # проверяет верность пути к файлу
            self.result.setText('По такому пути файла не существует.')
        else:
            playlist_name = self.title_album.text().strip()
            if self.processing_database(playlist_name, song_path, song_name):
                pass
            elif self.tableWidget.currentRow() >= 0:
                selected_item = self.tableWidget.currentItem()  # Получение выбранного элемента
                selected_row = selected_item.row()  # Получение индекса выбранной строки
                playlist_name = self.tableWidget.item(selected_row,
                                            0).text().strip()  # Получение значения из первого столбца выбранной строки
                self.processing_database(playlist_name, song_path, song_name)
            else:
                self.result.setText('Напишите название плейлиста или выберете его в таблицы.')

    def processing_database(self, playlist_name, song_path, song_name):
        # Соединение с базой данных
        conn = sqlite3.connect('albums.db')
        c = conn.cursor()
        # Получение идентификатора выбранного плейлиста по его названию
        c.execute("SELECT playlist_id FROM Playlists WHERE playlist_name = ?", (playlist_name,))
        result = c.fetchone()
        if result:
            playlist_id = result[0]
            # Выполнение SQL-запроса для добавления песни в базу данных
            c.execute("INSERT INTO Songs (song_path, song_name, playlist_id) VALUES (?, ?, ?)",
                      (song_path, song_name, playlist_id))
            # Сохранение изменений и закрытие соединения
            conn.commit()
            conn.close()
            self.result.setText('Трек успешно добавлен.')
            return True
        else:
            return False

    def create_table(self):
        self.tableWidget.setColumnCount(2)  # Устанавливаем число колонок
        self.tableWidget.setHorizontalHeaderLabels(['Название альбома', 'Дата создания'])
        # Задаем размеры колонок
        self.tableWidget.setColumnWidth(0, 253)
        self.tableWidget.setColumnWidth(1, 253)
        # Запрещаем редактирование ячеек
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def search_playlists(self):
        # Получение введенного пользователем названия плейлиста
        playlist_name = self.title_album.text()
        # Соединение с базой данных
        conn = sqlite3.connect('albums.db')
        c = conn.cursor()
        # Выполнение SQL-запроса для поиска плейлистов
        c.execute("SELECT playlist_name, created_date FROM Playlists WHERE playlist_name LIKE ?",
                  ('%' + playlist_name + '%',))
        playlists = c.fetchall()
        # Очистка таблицы перед обновлением результатов
        self.tableWidget.clearContents()
        # Обновление таблицы с результатами поиска
        self.tableWidget.setRowCount(len(playlists))
        for i, playlist in enumerate(playlists):
            for j, data in enumerate(playlist):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(i, j, item)
        # Закрытие соединения с базой данных
        conn.close()

    def delete_song_in_playlist(self, playlist):
        conn = sqlite3.connect('albums.db')
        cursor = conn.cursor()
        song_name = self.title_music.text().strip()
        # Получить идентификатор плейлиста по его имени
        cursor.execute("SELECT playlist_id FROM Playlists WHERE playlist_name = ?", (playlist,))
        playlist_id = cursor.fetchone()[0]  # Извлекаем первый столбец результата запроса
        # Проверить наличие песни в таблице Songs для заданного плейлиста
        cursor.execute("SELECT * FROM Songs WHERE song_name = ? AND playlist_id = ?", (song_name, playlist_id))
        result = cursor.fetchone()
        if result:
            # Удалить песню из таблицы Songs, сопоставив по названию песни и идентификатору плейлиста
            cursor.execute("DELETE FROM Songs WHERE song_name = ? AND playlist_id = ?", (song_name, playlist_id))
            conn.commit()  # Зафиксировать изменения в базе данных
            if song_name in self.window.album_songs:
                self.open_playlist()
            self.result.setText('Трек из плейлиста удалён.')
        else:
            self.result.setText('Такого трека нет в этом альбом!.')
        conn.close()

    def delete_selected_row(self):
        selected_row = self.tableWidget.currentRow()  # получение индекса строки, которую мы хотим удалить
        if selected_row >= 0:
            selected_item = self.tableWidget.currentItem()  # Получение выбранного элемента
            selected_row = selected_item.row()  # Получение индекса выбранной строки
            playlist_name = self.tableWidget.item(selected_row,
                                                  0).text().strip()  # Получение значения из первого столбца выбранной строки
            if self.check_song.isChecked():
                self.delete_song_in_playlist(playlist_name)
            elif True:
                # Соединение с базой данных
                conn = sqlite3.connect('albums.db')
                c = conn.cursor()
                # Получение идентификатора выбранного плейлиста по его названию
                c.execute("SELECT playlist_id FROM Playlists WHERE playlist_name = ?", (playlist_name,))
                result = c.fetchone()
                if result:
                    playlist_id = result[0]
                    # Удаление плейлиста из таблицы Playlists
                    c.execute("DELETE FROM Playlists WHERE playlist_id = ?", (playlist_id,))
                    # Удаление треков, связанных с плейлистом, из таблицы Songs
                    c.execute("DELETE FROM Songs WHERE playlist_id = ?", (playlist_id,))
                    # Сохранение изменений и закрытие соединения
                    conn.commit()
                    conn.close()
                    self.tableWidget.removeRow(selected_row)  # удаление строки
                    self.result.setText('Плейлист удален.')
                else:
                    self.result.setText('Выберете ячейку строки, которую вы хотите удалить.')
        else:
            self.result.setText('Выберете ячейку строки.')

    def open_playlist(self):
        '''Выводит в главный список треков выбранный плейлист.'''
        playlist_name = self.title_album.text().strip()
        if not playlist_name and self.tableWidget.currentRow() >= 0:
            selected_item = self.tableWidget.item(self.tableWidget.currentRow(),
                                                  0)  # Получение значения из первого столбца выбранной строки
            playlist_name = selected_item.text().strip()  # Получение текста из выбранной ячейки
        if playlist_name:
            # Соединение с базой данных
            conn = sqlite3.connect('albums.db')
            c = conn.cursor()
            # Получение идентификатора плейлиста по имени
            c.execute("SELECT playlist_id FROM Playlists WHERE playlist_name=?", (playlist_name,))
            result = c.fetchone()
            if result is not None:
                playlist_id = result[0]
                # Получение треков плейлиста по идентификатору
                c.execute("SELECT song_name, song_id FROM Songs WHERE playlist_id=?", (playlist_id,))
                playlist_songs = c.fetchall()
                # Очистка главного списка треков
                self.window.listMusics.clear()
                self.window.flag_radio = False
                # Добавление треков в главный список
                self.window.album_songs = dict(playlist_songs)  # словарь название трека - индекс в БД
                for song_name, song_index in playlist_songs:
                    self.window.listMusics.addItem(song_name)
                self.result.setText('Треки плейлиста успешно загружены.')
                self.window.title_playlist.setText(f'Альбом: {playlist_name}')
                self.window.play_music.setEnabled(False)  # блокирование кнопок
                self.window.last.setEnabled(False)  # блокирование кнопок
                self.window.next.setEnabled(False)
            else:
                self.result.setText('Плейлист с таким названием не найден.')
            # Закрытие соединения с базой данных
            conn.commit()
            conn.close()
        else:
            self.result.setText('Напишите название плейлиста или выберете его в таблице.')


def f_open(self):
    '''Выбор файла(трека) в проводнике.'''
    self.way_file.setText('')
    dir = QFileDialog.getOpenFileName(self, 'Аудио файлы', '',
                                      'Аудио файлы (*.wav *.mp3)')[0]  # создание диалогового окна для выбора файлов
    if dir:
        file_name = os.path.split(dir)[1]  # получаем название файла с расширением
        if len(self.title_music.text().strip()) == 0:  # если не заполнита строка названия трека
            self.title_music.setText(file_name)  # вставляется название файла
    self.way_file.setText(dir)
