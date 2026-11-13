# -*- coding: utf-8 -*-
from attendance import (
    load_data, show_attendance, add_record, 
    search_records, update_record, delete_record
)

def main():
    records = load_data()
    
    while True:
        print("\n--- МЕНЮ УЧЕТА ПОСЕЩАЕМОСТИ (2ИП-5) ---")
        print("1. Посмотреть весь список")
        print("2. Добавить студента / запись")
        print("3. Найти запись")
        print("4. Изменить запись")
        print("5. Удалить запись")
        print("6. Выйти")
        
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == "1":
            show_attendance(records)
            
        elif choice == "2":
            print("\n--- Добавление новой записи ---")
            name = input("ФИО: ")
            group = input("Группа (например, 2ИП-5): ")
            subject = input("Предмет / Специальность: ")
            date = input("Дата (гггг-мм-дд): ")
            status = input("Статус (присутствует / отсутствует / опоздал): ")
            
            try:
                add_record(records, name, group, subject, date, status)
                print("[+] Запись добавлена!")
            except ValueError as err:
                print(f"[!] Ошибка: {err}")
                
        elif choice == "3":
            print("\n--- Поиск ---")
            query = input("Введите текст для поиска: ")
            res = search_records(records, query)
            if res:
                show_attendance(res)
            else:
                print("[-] Ничего не найдено.")
                
        elif choice == "4":
            print("\n--- Редактирование ---")
            try:
                rec_id = int(input("Введите ID записи: "))
                print("(Если не хотите менять поле — просто жмите Enter)")
                name = input("Новое ФИО: ")
                group = input("Новая группа: ")
                subject = input("Новый предмет: ")
                date = input("Новая дата: ")
                status = input("Новый статус: ")
                
                update_record(
                    records, rec_id,
                    student_name=name if name else None,
                    group=group if group else None,
                    subject=subject if subject else None,
                    date=date if date else None,
                    status=status if status else None
                )
                print("[+] Запись обновлена!")
            except ValueError as err:
                print(f"[!] Ошибка: {err}")
                
        elif choice == "5":
            print("\n--- Удаление ---")
            try:
                rec_id = int(input("Введите ID записи для удаления: "))
                delete_record(records, rec_id)
                print("[+] Запись удалена!")
            except ValueError as err:
                print(f"[!] Ошибка: {err}")
                
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("[!] Неверный ввод, введите цифру от 1 до 6.")

if __name__ == "__main__":
    main()