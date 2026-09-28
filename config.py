"""Application configuration."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "library.db"
FINE_PER_DAY = 5.0
LOAN_DAYS = 14
