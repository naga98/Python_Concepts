from collections import Counter
from pathlib import Path


LOG_FILE = Path(__file__).with_name("application.log")
ERROR_FILE = Path(__file__).with_name("errors.txt")
WARNING_FILE = Path(__file__).with_name("warnings.txt")


def read_log():
    """Read the entire log file and return non-empty entries."""
    with LOG_FILE.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def count_levels(entries):
    counts = Counter()
    for entry in entries:
        level = entry.split(" - ", 1)[0]
        counts[level] += 1
    return counts


def save_matching_entries(entries, level, output_file):
    matching = [entry for entry in entries if entry.startswith(f"{level} - ")]
    output_file.write_text("\n".join(matching) + "\n", encoding="utf-8")
    return len(matching)


def pandas_frequency_analysis(entries):
    try:
        import pandas as pd
    except ImportError:
        return None
    dataframe = pd.DataFrame({"entry": entries})
    dataframe["level"] = dataframe["entry"].str.split(" - ", n=1).str[0]
    return dataframe["level"].value_counts()


def main():
    entries = read_log()
    counts = count_levels(entries)
    error_count = save_matching_entries(entries, "ERROR", ERROR_FILE)
    warning_count = save_matching_entries(entries, "WARNING", WARNING_FILE)

    print(f"Total log entries: {len(entries)}")
    print(f"INFO occurrences: {counts['INFO']}")
    print(f"WARNING occurrences: {counts['WARNING']}")
    print(f"ERROR occurrences: {counts['ERROR']}")
    print(f"Saved {error_count} entries to {ERROR_FILE.name}")
    print(f"Saved {warning_count} entries to {WARNING_FILE.name}")

    frequency = pandas_frequency_analysis(entries)
    if frequency is not None:
        print("\nPandas frequency analysis:")
        print(frequency.to_string())
    else:
        print("\nPandas is not installed; frequency analysis skipped.")


if __name__ == "__main__":
    main()