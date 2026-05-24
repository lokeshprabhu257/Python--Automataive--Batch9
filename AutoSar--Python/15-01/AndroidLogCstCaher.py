import os
from collections import Counter

# ================================
# Android Logcat Crash Analyzer
# Automotive Infotainment Edition
# ================================

LOG_FILE = "android_logcat.txt"


# -------------------------------
# 1. Data Collection Layer
# -------------------------------
def read_logcat_file():
    if not os.path.exists(LOG_FILE):
        print(" Error: Android logcat file not found!")
        return []

    with open(LOG_FILE, "r") as file:
        return file.readlines()


# -------------------------------
# 2. Crash Detection Layer
# -------------------------------
def extract_crash_reasons(log_lines):
    crash_reasons = []

    for line in log_lines:
        if "Exception" in line or "Error" in line:
            crash_reasons.append(line.strip())

    return crash_reasons


# -------------------------------
# 3. Crash Frequency Analysis
# -------------------------------
def analyze_crashes(crash_list):
    crash_counter = Counter(crash_list)
    return crash_counter


# -------------------------------
# 4. Display Report Layer
# -------------------------------
def display_results(crash_data):
    print("\n📊 ANDROID APP CRASH REPORT")
    print("----------------------------------")

    if not crash_data:
        print("✅ No crashes detected.")
        return

    for crash, count in crash_data.most_common():
        print(f"{crash}  →  {count} time(s)")

    print("----------------------------------")
    print("⚠️ Most Frequent Crash:")
    print(crash_data.most_common(1)[0][0])


# -------------------------------
# Main Infotainment Diagnostic
# -------------------------------
def main():
    print("🚗 Android Infotainment Crash Analyzer Started...\n")

    log_data = read_logcat_file()
    crashes = extract_crash_reasons(log_data)
    crash_stats = analyze_crashes(crashes)
    display_results(crash_stats)


if __name__ == "__main__":
    main()