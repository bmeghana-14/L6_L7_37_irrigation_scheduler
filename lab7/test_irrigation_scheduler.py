from hypothesis import given, strategies as st

from irrigation_scheduler import parse_zone, moisture_average, water_needed


@given(st.text() | st.none())
def test_parse_zone_no_crash(value):
    result = parse_zone(value)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], float)


@given(st.text() | st.none())
def test_moisture_average_no_crash(value):
    result = moisture_average(value)
    assert isinstance(result, int)
    assert 0 <= result <= 100


@given(st.text() | st.none())
def test_water_needed_no_crash(value):
    result = water_needed(value)
    assert isinstance(result, float)
    assert result >= 0


@given(
    st.text(min_size=1).filter(
        lambda value: ":" not in value and value.strip() != ""
    ),
    st.floats(
        min_value=0,
        max_value=1_000_000,
        allow_nan=False,
        allow_infinity=False,
    ),
)
def test_parse_zone_valid_inputs(name, area):
    result = parse_zone(f"{name}:{area}")
    assert result[0] == name.strip().title()
    assert result[1] == area


@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=50))
def test_moisture_average_valid_inputs(readings):
    csv = ",".join(str(value) for value in readings)
    assert moisture_average(csv) == sum(readings) // len(readings)


@given(
    st.floats(
        min_value=0,
        max_value=1_000_000,
        allow_nan=False,
        allow_infinity=False,
    ),
    st.floats(
        min_value=0,
        max_value=1_000_000,
        allow_nan=False,
        allow_infinity=False,
    ),
)
def test_water_needed_valid_inputs(area, rainfall):
    assert water_needed(f"{area}|{rainfall}") == max(area * 5 - rainfall, 0.0)
