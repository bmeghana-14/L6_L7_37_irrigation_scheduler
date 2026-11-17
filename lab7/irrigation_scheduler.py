import math


def parse_zone(text):
    """Parse 'zone:area' and return (title-cased zone, area).

    Invalid input is represented by ("", 0.0).
    """
    if not isinstance(text, str):
        return "", 0.0
    parts = text.split(":")
    if len(parts) != 2:
        return "", 0.0
    name, area_text = parts[0].strip(), parts[1].strip()
    if not name or not area_text:
        return "", 0.0
    try:
        area = float(area_text)
    except (TypeError, ValueError, OverflowError):
        return "", 0.0
    if not math.isfinite(area) or area < 0:
        return "", 0.0
    return name.title(), area


def moisture_average(readings_csv):
    """Return the integer average of comma-separated moisture percentages.

    Invalid input is represented by 0.
    """
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        return 0
    try:
        parts = readings_csv.split(",")
        if any(not part.strip() for part in parts):
            return 0
        values = [int(part.strip()) for part in parts]
    except (TypeError, ValueError, OverflowError):
        return 0
    if any(value < 0 or value > 100 for value in values):
        return 0
    return sum(values) // len(values)


def water_needed(text):
    """Calculate max(area * 5 - rainfall, 0).

    Invalid input is represented by 0.0.
    """
    if not isinstance(text, str):
        return 0.0
    parts = text.split("|")
    if len(parts) != 2:
        return 0.0
    try:
        area = float(parts[0].strip())
        rain = float(parts[1].strip())
    except (TypeError, ValueError, OverflowError):
        return 0.0
    if not math.isfinite(area) or not math.isfinite(rain) or area < 0 or rain < 0:
        return 0.0
    return max(area * 5 - rain, 0.0)


def main():
    print("==== Running parse_zone ====")
    user_input = input("Enter zone:area in m2 (e.g. north:120): ")
    print("Zone and Area:", parse_zone(user_input))

    print("\n==== Running moisture_average ====")
    user_input = input("Enter moisture readings as CSV (e.g. 40,35,50): ")
    print("Average Moisture:", moisture_average(user_input))

    print("\n==== Running water_needed ====")
    user_input = input("Enter area|rainfall (e.g. 120|8): ")
    print("Water Needed:", water_needed(user_input))


if __name__ == "__main__":
    main()
