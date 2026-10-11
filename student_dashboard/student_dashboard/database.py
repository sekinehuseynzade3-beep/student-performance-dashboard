"""Database layer: yalnız SQL Server ilə əlaqəli funksiyalar."""
from contextlib import contextmanager
from dataclasses import dataclass

import pyodbc

import config


@dataclass(frozen=True)
class Student:
    name: str
    score: int


def _build_connection_string() -> str:
    base = (
        f"DRIVER={{{config.DB_DRIVER}}};"
        f"SERVER={config.DB_SERVER};"
        f"DATABASE={config.DB_NAME};"
        "TrustServerCertificate=yes;"
    )
    if config.DB_USER:
        return base + f"UID={config.DB_USER};PWD={config.DB_PASSWORD};"
    return base + "Trusted_Connection=yes;"


def create_connection() -> pyodbc.Connection:
    return pyodbc.connect(_build_connection_string())


@contextmanager
def _connection():
    connection = create_connection()
    try:
        yield connection
    finally:
        connection.close()


def add_student(name: str, score: int) -> None:
    with _connection() as connection:
        connection.cursor().execute(
            "INSERT INTO Students (Name, Score) VALUES (?, ?)", name, score
        )
        connection.commit()


def get_students() -> list[Student]:
    with _connection() as connection:
        rows = connection.cursor().execute(
            "SELECT Name, Score FROM Students ORDER BY StudentID"
        ).fetchall()
    return [Student(name=row.Name, score=row.Score) for row in rows]


def get_student(name: str) -> list[Student]:
    """Ada görə (qismən uyğunluq ilə) axtarış."""
    with _connection() as connection:
        rows = connection.cursor().execute(
            "SELECT Name, Score FROM Students WHERE Name LIKE ? ORDER BY StudentID",
            f"%{name}%",
        ).fetchall()
    return [Student(name=row.Name, score=row.Score) for row in rows]
