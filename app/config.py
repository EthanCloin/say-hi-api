from pathlib import Path

base_path = Path(__file__).resolve().parent

DATABASE = base_path / "hellos.db"
SECRET_KEY = "dev"
