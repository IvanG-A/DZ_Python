import pytest
from sqlalchemy.orm import Session
from db import engine
from models import Base, Student


# Создаём таблицы перед тестами
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# fixture для сессии БД
@pytest.fixture
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


# fixture для создания тестового студента
@pytest.fixture
def create_test_student(db_session: Session):
    student = Student(first_name="Test", last_name="User", email="test@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    yield student

    # Очистка после теста
    db_session.delete(student)
    db_session.commit()


# ---------- ТЕСТ 1: ДОБАВЛЕНИЕ СТУДЕНТА ----------
def test_create_student(db_session: Session):
    """Позитивный тест: создание нового студента"""
    student = Student(
        first_name="Иван", last_name="Петров", email="ivan.petrov@example.com"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    assert student.id is not None
    assert student.first_name == "Иван"
    assert student.last_name == "Петров"
    assert student.email == "ivan.petrov@example.com"
    assert student.is_active is True

    db_session.delete(student)
    db_session.commit()


# ---------- ТЕСТ 2: ОБНОВЛЕНИЕ СТУДЕНТА ----------
def test_update_student(db_session: Session, create_test_student: Student):
    """Позитивный тест: обновление данных студента"""
    student = create_test_student

    # Обновляем данные
    student.first_name = "Updated"
    student.last_name = "Name"
    student.email = "updated@example.com"
    db_session.commit()
    db_session.refresh(student)

    assert student.first_name == "Updated"
    assert student.last_name == "Name"
    assert student.email == "updated@example.com"


# ---------- ТЕСТ 3: УДАЛЕНИЕ СТУДЕНТА ----------
def test_delete_student(db_session: Session):
    """Позитивный тест: удаление студента"""
    # Создаём студента специально для удаления
    student = Student(
        first_name="ToDelete", last_name="User", email="delete@example.com"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student_id = student.id

    # Удаляем
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что студент удален
    deleted_student = db_session.get(Student, student_id)
    assert deleted_student is None
