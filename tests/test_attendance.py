# -*- coding: utf-8 -*-
import pytest
from attendance import add_record, search_records, update_record, delete_record

def test_add_record_success():
    """Тест успешного добавления записи"""
    records = []
    res = add_record(records, "Тестов Тест", "2ИП-5", "Информационные системы", "2026-11-09", "присутствует")
    assert len(records) == 1
    assert res["id"] == 1
    assert res["student_name"] == "Тестов Тест"

def test_add_record_invalid_status():
    """Тест на ошибку при неверном статусе"""
    records = []
    with pytest.raises(ValueError):
        add_record(records, "Тест", "2ИП-5", "Информационные системы", "2026-11-09", "гуляет")

def test_search_records():
    """Тест поиска записей"""
    records = [
        {"id": 1, "student_name": "Иванов Иван", "group": "2ИП-5", "subject": "Математика", "date": "2026-11-09", "status": "присутствует"},
        {"id": 2, "student_name": "Петров Петр", "group": "2ИП-5", "subject": "Физика", "date": "2026-11-09", "status": "отсутствует"}
    ]
    found = search_records(records, "Иванов")
    assert len(found) == 1
    assert found[0]["student_name"] == "Иванов Иван"

def test_update_record():
    """Тест изменения данных"""
    records = [
        {"id": 1, "student_name": "Старый Студент", "group": "2ИП-5", "subject": "Физика", "date": "2026-11-09", "status": "присутствует"}
    ]
    updated = update_record(records, 1, student_name="Новый Студент", status="опоздал")
    assert updated["student_name"] == "Новый Студент"
    assert updated["status"] == "опоздал"

def test_delete_record():
    """Тест удаления записи"""
    records = [
        {"id": 1, "student_name": "Удаляемый", "group": "2ИП-5", "subject": "Информационные системы", "date": "2026-11-09", "status": "присутствует"}
    ]
    delete_record(records, 1)
    assert len(records) == 0