main_menu = ['Главное меню',
             'Открыть телефонную книгу',
             'Сохранить телефонную книгу',
             'Показать контакты',
             'Создать контакты',
             'Найти контакты',
             'Изменить контакты',
             'Удалить контакты',
             'Выход']

choice_main_menu = f'Выберете пункт меню ({1} - {len(main_menu) - 1}):'
choice_main_menu_error = f'Нужно ввести число от 1 до {len(main_menu) - 1}'

phone_book_opened_seccessfull = 'Телефонная книга открыта'
phone_book_saved_seccessfull = 'Телефонная книга сохранена'

empty_phone_book_error = 'Телефонная книга пуста или не открыта'

input_new_contact = ['Введите имя контакта: ',
                     'Введите номер контакта: ',
                     'Введите маркер контакта: ']
no_changes = 'Или ENTER, чтобы оставить все без изменений'

edit_contact = [f'Введите новое имя ({no_changes}): ',
                f'Введите новый телефон ({no_changes}): ',
                f'Введите новый маркер контакта ({no_changes}): ']



input_serch_word = 'Введите слово для поиска: '
input_serch_word_for_edit = 'Введите слово для поиска, который хотите изменить: '
input_search_word_for_delete = 'Введите слово для поиска, который хотите удалить: '
input_id_for_edit = 'Введите ID контакта, который хотите изменить: '
input_id_for_delete = 'Введите ID контакта, который хотите удалить: '

def new_contact_added_successfull(name: str) -> str:
    return f"Контакт'{name}' добавлен"
def find_contact_no_result(word: str) -> str:
    return f'Контакты содержащие "{word} не найдены'
def edit_contact_successfull(name) -> str:
    return f'Контакт "{name} успешно изменен'
def delete_contact_successfull(name) -> str:
    return f'Контакт "{name}" успешно удален'