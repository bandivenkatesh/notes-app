"""Utility functions for database operations."""
import json
import os
from typing import List, Dict, Any

def ensure_data_dir():
    """Ensure data directory exists."""
    from config import DATA_DIR
    os.makedirs(DATA_DIR, exist_ok=True)

def load_json(filepath: str) -> List[Dict]:
    """Load data from JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_json(filepath: str, data: List[Dict]) -> bool:
    """Save data to JSON file."""
    try:
        ensure_data_dir()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving to {filepath}: {e}")
        return False
