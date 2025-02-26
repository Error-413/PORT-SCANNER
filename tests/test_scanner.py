import pytest
from app.scanner import scan_port

def test_scan_port():
    """Test de la fonction scan_port sur localhost avec un port fermé"""
    target = "127.0.0.1"
    closed_port = 9999  # Assure-toi que ce port est fermé
    assert scan_port(target, closed_port) is None

