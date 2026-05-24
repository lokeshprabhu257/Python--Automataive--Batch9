import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from main import (
    FakeCar,
    decode_speed,
    encode_speed,
    run_validation_sequence,
    send_speed,
    receive_speed,
    validate_speed_value,
)


def test_validate_speed_value_bounds():
    assert validate_speed_value(0) is True
    assert validate_speed_value(200) is True
    assert validate_speed_value(-1) is False
    assert validate_speed_value(201) is False


def test_encode_decode_roundtrip():
    data = encode_speed(123)
    assert decode_speed(data) == 123


def test_fake_bus_send_receive():
    bus = FakeCar()
    send_speed(bus, 88)
    received = receive_speed(bus)
    assert received == 88


def test_run_validation_sequence_results():
    bus = FakeCar()
    results = run_validation_sequence(bus, [0, 50, 201])
    assert [r["status"] for r in results] == ["PASS", "PASS", "FAIL"]
