"""Layihənin bütün konfiqurasiya dəyərləri bir yerdə."""
import os

# --- SQL Server ---
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_NAME = os.getenv("DB_NAME", "UniversityDB")
# Boş saxlasanız Windows Authentication istifadə olunur
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# --- Score qaydaları ---
MIN_SCORE = 0
MAX_SCORE = 100

# --- Grade sərhədləri (magic number yoxdur) ---
GRADE_A_MIN_SCORE = 90
GRADE_B_MIN_SCORE = 80
GRADE_C_MIN_SCORE = 70
GRADE_D_MIN_SCORE = 60
