# Summarize daily rainfall and calculate a moving average.
# Practice: lists, statistics, sliding windows, streaks, and text charts.
import math
from statistics import fmean


def validate_readings(readings):
    if not readings or len(readings) > 366:
        raise ValueError("Enter from 1 to 366 daily readings.")
    if any(not math.isfinite(value) or not 0 <= value <= 1000000 for value in readings):
        raise ValueError("Readings must be finite and from 0 to 1000000 mm.")


def summarize_rainfall(readings):
    validate_readings(readings)
    longest_dry = current_dry = 0
    for value in readings:
        current_dry = current_dry + 1 if value == 0 else 0
        longest_dry = max(longest_dry, current_dry)
    peak = max(readings)
    return {"total": math.fsum(readings), "average": fmean(readings),
            "wet_days": sum(value > 0 for value in readings),
            "peak": peak, "peak_day": readings.index(peak) + 1, "longest_dry": longest_dry}


def moving_averages(readings, window):
    validate_readings(readings)
    if type(window) is not int or not 1 <= window <= len(readings):
        raise ValueError("Window must be a whole number from 1 to the number of readings.")
    return [fmean(readings[start:start + window]) for start in range(len(readings) - window + 1)]


def main():
    print("Rainfall Analyzer - comma-separated daily measurements in millimetres.")
    while True:
        text = input("Readings (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            readings = [float(part) for part in text.split(",")]
            window = int(input("Moving-average window in days: "))
            summary = summarize_rainfall(readings)
            averages = moving_averages(readings, window)
            for day, value in enumerate(readings, 1):
                width = round(value / summary["peak"] * 30) if summary["peak"] else 0
                print(f"Day {day}: {value:g} mm {'#' * width}")
            print(f"Total: {summary['total']:g} mm | Average: {summary['average']:.2f} mm")
            print(f"Wet days: {summary['wet_days']} | Longest dry streak: {summary['longest_dry']}")
            print(f"Peak: {summary['peak']:g} mm on day {summary['peak_day']} (first if tied)")
            for day, average in enumerate(averages, window):
                print(f"Window ending day {day}: {average:.2f} mm")
        except (ValueError, OverflowError) as error:
            print(f"Invalid rainfall input: {error}")


if __name__ == "__main__":
    main()
