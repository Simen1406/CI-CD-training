import os
import pytest
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
BACKEND_DIR = PROJECT_ROOT / "backend"
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(BACKEND_DIR))


@pytest.fixture(autouse=True)
def use_test_db(tmp_path):
    """each tests will use a separate test database file"""
    test_db = tmp_path / "test_database.db"
    os.environ["DB_PATH"] = str(test_db)

    from backend.db.db import init_db
    init_db()

    yield

    os.environ.pop("DB_PATH", None)

    os.environ.pop("DB_PATH", None)
