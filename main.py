import datetime
import json

notes_list = []


def test_notes(date_str):
    note1 = dict()
    note1["id"] = str(len(notes_list) + 1)
    note1["title"] = "title_note" + str(len(notes_list) + 1)
    note1["msg"] = "text_note" + str(len(notes_list) + 1)
    #note1['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #note1['date'] = '2021-02-12 21:41:42'
    note1['date'] = date_str
    notes_list.append(note1)


def print_notes(notes: list):
    for note in notes:
        for key, value in note.items():
            print(key + ": " + str(value), end='  ')
        print()


def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    new_note = dict()
    new_note["id"] = str(find_max_id() + 1) #str(len(notes_list) + 1)
    new_note["title"] = title
    new_note["msg"] = body
    new_note["date"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notes_list.append(new_note)


def save_notes():
    with open('notes_list.txt', 'a', encoding='utf-8') as file:
        res = file.write(str(notes_list))
        file.write('\n')
    return res


def save_notes_json():
    with open('notes_list_json.json', 'w') as file_json:
        json.dump(notes_list, file_json)


def load_notes():
    with open('notes.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def load_notes_json():
    with open('notes_list_json.json', 'r') as file_json:
        data = json.load(file_json)
        return data


def find_note_date():
    date_note = input('Введите дату записи в виде "гггг-мм-дд": ')
    new_notes_date = []
    for note in notes_list:
        temp = str(note["date"])
        date_yyyy_mm_dd = temp.split()
        if date_yyyy_mm_dd[0] == date_note:
            new_notes_date.append(note)
    if len(new_notes_date) > 0:
        print("Найденные заметки по дате " + date_note + ": ")
        print_notes(new_notes_date)
    else:
        print("Не нашел заметку по дате...")
    return new_notes_date


def find_note_id():
    id_note = input("Введите id записи: ")
    new_note_id = []
    for note in notes_list:
        temp = note["id"]
        if id_note == temp:
            new_note_id.append(note)
    if len(new_note_id) > 0:
        print("Найденная заметка по id " + id_note + ": ")
        print_notes(new_note_id)
    else:
        print("Не нашел заметку по id...")
    return new_note_id


def change_note(chng_note: dict):
    temp_list = list()

    temp_list.append(chng_note)
    print("Старая запись: ")
    print_notes(temp_list)
    title = input("Введите новый заголовок заметки: ")
    body = input("Введите новое тело заметки: ")
    for note in notes_list:
        if chng_note["id"] == note["id"]:
            note["title"] = title
            note["msg"] = body
            note["date"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def delete_note(note: dict):
    for del_note in notes_list:
        if del_note["id"] == note["id"]:
            try:
                notes_list.remove(del_note)
                print("Запись: id: " + note["id"] + "  title: " + note["title"] + "  msg: " +
                      note["msg"] + "  date: " + note["date"] + " успешно удалена.")
                print("Новый список заметок:")
                print_notes(notes_list)
            except Exception:
                print("Запись не удалось удалить.")


def find_max_id():
    max_id = 0
    for note in notes_list:
        temp = int(note["id"])
        if temp > max_id:
            max_id = temp
    return max_id


def menu():
    print()
    print('Команды работы с записной книжкой: ')
    print('                                     1 - Показать все записи.\n'
          '                                     2 - Добавить запись.\n'
          '                                     3 - Поиск записи по дате.\n'
          '                                     4 - Поиск записи по id.\n'                            
          '                                     5 - Изменить запись.\n'
          '                                     6 - Удалить запись.\n'
          '                                     7 - Сохранить записи в файл.\n'
          '                                     8 - Загрузить записи из файла.\n'
          '                                     9 - Выход из записной книги.')


def start():
    # две тестовых записи при первой загрузке блокнота
    test_notes('2021-02-12 21:41:42')
    test_notes('2020-02-22 13:23:15')
    while True:
        menu()
        answer = input('Введите номер команды: ')
        if answer == "1":
            print_notes(notes_list)
        if answer == "2":
            add_note()
        if answer == "3":
            find_note_date()
        if answer == "4":
            find_note_id()
        if answer == "5":
            if len(find_note_date()) > 0:
                change_note(*find_note_id())
        if answer == "6":
            if len(find_note_date()) > 0:
                delete_note(*find_note_id())
        if answer == "7":
            try:
                save_notes_json()
                print("Записи успешно сохранены...")
            except FileNotFoundError:
                print("Записи не удалось сохранить...")
        if answer == "8":
            try:
                temp = load_notes_json()
                print("Загруженные записи:")
                print_notes(temp)
            except FileNotFoundError:
                print("Записи не удалось загрузить...")
        if answer == "9":
            break


start()
