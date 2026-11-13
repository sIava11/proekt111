# -*- coding: utf-8 -*-
import json
import os

# Путь к файлу с данными
DATA_FILE = os.path.join("data", "attendance.json")

# Стартовый список студентов, если файла еще нет или он пустой
default_demo = [
    {
        "id": 1,
        "student_name": "Кушкян Александр",
        "group": "2ИП-5",
        "subject": "Информационные системы и программирование",
        "date": "2026-11-09",
        "status": "присутствует"
    },
    {
        "id": 2,
        "student_name": "Волков Вячеслав",
        "group": "2ИП-5",
        "subject": "Информационные системы и программирование",
        "date": "2026-11-09",
        "status": "присутствует"
    }
]

def load_data():
    """Читаем данные из JSON. Если файла нет или он пуст — заполняем базовыми студентами."""
    if not os.path.exists("data"):
        os.makedirs("data")
        
    if not os.path.exists(DATA_FILE):
        save_data(default_demo)
        return list(default_demo)
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list) or not data:
                save_data(default_demo)
                return list(default_demo)
            return data
    except (json.JSONDecodeError, OSError):
        save_data(default_demo)
        return list(default_demo)

def save_data(records):
    """Сохраняем список записей в JSON-файл."""
    if not os.path.exists("data"):
        os.makedirs("data")
        
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)

def show_attendance(records=None):
    """Печатаем таблицу со всеми студентами в консоль."""
    if records is None:
        records = load_data()
    
    if not records:
        print("\n[Инфо] Список посещаемости пуст.")
        return
    
    print("\n" + "=" * 105)
    print(f"{'ID':<4} | {'ФИО студента':<25} | {'Группа':<8} | {'Предмет / Спец.':<35} | {'Дата':<10} | {'Статус':<12}")
    print("=" * 105)
    for r in records:
        print(f"{r['id']:<4} | {r['student_name']:<25} | {r['group']:<8} | {r['subject']:<35} | {r['date']:<10} | {r['status']:<12}")
    print("=" * 105)

def add_record(records, student_name, group, subject, date, status):
    """Добавляем новую запись и сохраняем."""
    if not student_name.strip() or not group.strip() or not subject.strip() or not date.strip() or not status.strip():
        raise ValueError("Заполните все поля!")
    
    allowed = {"присутствует", "отсутствует", "опоздал"}
    st = status.strip().lower()
    if st not in allowed:
        raise ValueError("Статус может быть только: присутствует, отсутствует или опоздал.")

    new_id = 1 if not records else max(r["id"] for r in records) + 1

    item = {
        "id": new_id,
        "student_name": student_name.strip(),
        "group": group.strip(),
        "subject": subject.strip(),
        "date": date.strip(),
        "status": st
    }
    
    records.append(item)
    save_data(records)
    return item

def search_records(records, query):
    """Ищем по фамилии, группе или предмету."""
    q = query.strip().lower()
    if not q:
        return []
    
    res = []
    for r in records:
        if q in r["student_name"].lower() or q in r["group"].lower() or q in r["subject"].lower():
            res.append(r)
    return res

def update_record(records, record_id, student_name=None, group=None, subject=None, date=None, status=None):
    """Редактируем поля по ID."""
    found = None
    for r in records:
        if r["id"] == record_id:
            found = r
            break
            
    if not found:
        raise ValueError(f"Запись с ID {record_id} не найдена.")
        
    if student_name and student_name.strip():
        found["student_name"] = student_name.strip()
    if group and group.strip():
        found["group"] = group.strip()
    if subject and subject.strip():
        found["subject"] = subject.strip()
    if date and date.strip():
        found["date"] = date.strip()
    if status and status.strip():
        allowed = {"присутствует", "отсутствует", "опоздал"}
        st = status.strip().lower()
        if st not in allowed:
            raise ValueError("Неверный статус.")
        found["status"] = st
        
    save_data(records)
    return found

def delete_record(records, record_id):
    """Удаляем запись по ID."""
    found = None
    for r in records:
        if r["id"] == record_id:
            found = r
            break
            
    if not found:
        raise ValueError(f"Запись с ID {record_id} не найдена.")
        
    records.remove(found)
    save_data(records)
    return found