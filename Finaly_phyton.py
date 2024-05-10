import json
import datetime

class Note:
    def __init__(self, note_id, title, message, creation_date):
        self.note_id = note_id
        self.title = title
        self.message = message
        self.creation_date = creation_date

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump([note.__dict__ for note in notes], file)

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            data = json.load(file)
            notes = [Note(note['note_id'], note['title'], note['message'], note['creation_date']) for note in data]
        return notes
    except FileNotFoundError:
        return []

def add_note(notes, title, message):
    note_id = len(notes) + 1
    creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append(Note(note_id, title, message, creation_date))
    save_notes(notes)

def list_notes(notes):
    for note in notes:
        print(f"ID: {note.note_id} | Title: {note.title} | Date: {note.creation_date}")

def edit_note(notes, note_id, new_title, new_message):
    for note in notes:
        if note.note_id == note_id:
            note.title = new_title
            note.message = new_message
            note.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            break

def delete_note(notes, note_id):
    notes = [note for note in notes if note.note_id != note_id]
    save_notes(notes)

def filter_notes_by_date(notes, date):
    filtered_notes = [note for note in notes if date in note.creation_date]
    return filtered_notes

if __name__ == "__main__":
    notes = load_notes()

    while True:
        command = input("Введите команду (add/list/edit/delete/filter/exit): ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(notes, title, message)
            print("Заметка успешно сохранена.")
        elif command == "list":
            list_notes(notes)
        elif command == "edit":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            new_title = input("Введите новый заголовок: ")
            new_message = input("Введите новое сообщение: ")
            edit_note(notes, note_id, new_title, new_message)
            print("Заметка успешно отредактирована.")
        elif command == "delete":
            note_id = int(input("Введите ID заметки, которую хотите удалить: "))
            delete_note(notes, note_id)
            print("Заметка успешно удалена.")
        elif command == "filter":
            date = input("Введите дату для фильтрации (гггг-мм-дд): ")
            filtered_notes = filter_notes_by_date(notes, date)
            list_notes(filtered_notes)
        elif command == "exit":
            break
        else:
            print("Неверная команда. Попробуйте снова.")
