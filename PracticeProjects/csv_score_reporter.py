# Read student scores from CSV and report averages, leaders, and pass counts.
# Practice: csv.DictReader, file handling, statistics, sets, and aggregation.
import csv
import math
from pathlib import Path
from statistics import fmean


def load_scores(path):
    records = []
    seen_names = set()
    with Path(path).open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, strict=True)
        if reader.fieldnames != ["name", "score"]:
            raise ValueError("CSV header must be exactly: name,score")
        for row in reader:
            line_number = reader.line_num
            if None in row or row["score"] is None:
                raise ValueError(f"Line {line_number}: expected two columns.")
            name = row["name"].strip()
            if not name:
                raise ValueError(f"Line {line_number}: name cannot be empty.")
            if name.casefold() in seen_names:
                raise ValueError(f"Line {line_number}: duplicate student name.")
            try:
                score = float(row["score"])
            except ValueError as error:
                raise ValueError(f"Line {line_number}: score must be numeric.") from error
            if not math.isfinite(score) or not 0 <= score <= 100:
                raise ValueError(f"Line {line_number}: score must be from 0 to 100.")
            records.append({"name": name, "score": score})
            seen_names.add(name.casefold())
    if not records:
        raise ValueError("CSV must contain at least one student.")
    return records


def summarize_scores(records, pass_mark=50):
    if not records:
        raise ValueError("No student scores to summarize.")
    if not math.isfinite(pass_mark) or not 0 <= pass_mark <= 100:
        raise ValueError("Pass mark must be from 0 to 100.")
    scores = [record["score"] for record in records]
    highest = max(scores)
    return {
        "count": len(records),
        "average": fmean(scores),
        "lowest": min(scores),
        "highest": highest,
        "leaders": [record["name"] for record in records if record["score"] == highest],
        "passed": sum(score >= pass_mark for score in scores),
    }


def main():
    print("CSV Score Reporter - reads a CSV with columns name,score.")
    print('Example rows: Amina,80 and "Otieno, Sam",65. Files are not changed.')
    while True:
        path = input("CSV path (q to quit): ").strip()
        if path.lower() == "q":
            break
        try:
            text = input("Pass mark (blank for 50): ").strip()
            pass_mark = float(text) if text else 50
            summary = summarize_scores(load_scores(path), pass_mark)
            print(f"Students: {summary['count']} | Average: {summary['average']:.2f}")
            print(f"Lowest: {summary['lowest']:g} | Highest: {summary['highest']:g}")
            print(f"Top students: {', '.join(summary['leaders'])}")
            print(f"Passed: {summary['passed']} | Failed: {summary['count'] - summary['passed']}")
        except (OSError, UnicodeError, ValueError, csv.Error) as error:
            print(f"Cannot create report: {error}")


if __name__ == "__main__":
    main()
