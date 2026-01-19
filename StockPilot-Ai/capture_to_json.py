import json
import re

def extract_number(text):
    text = text.replace(",", "")
    match = re.search(r"[0-9.]+", text)
    return float(match.group()) if match else None

def capture_to_json(screen_text):
    data = {}

    for line in screen_text.split("\n"):
        if "Market Cap" in line:
            data["market_cap"] = extract_number(line)
        elif "P/E" in line:
            data["pe"] = extract_number(line)
        elif "ROE" in line:
            data["roe"] = extract_number(line)
        elif "52 Week High" in line:
            data["high_52w"] = extract_number(line)
        elif "52 Week Low" in line:
            data["low_52w"] = extract_number(line)
        elif "Current Price" in line:
            data["price"] = extract_number(line)

    with open("stock_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Data saved to stock_data.json")


if __name__ == "__main__":
    # TEMPORARY: sample text from DroidRun vision
    screen_text = """
    Market Cap ₹6,50,000 Cr
    Current Price ₹1600
    P/E 28.3
    ROE 24.1 %
    52 Week High 1700
    52 Week Low 1200
    """

    capture_to_json(screen_text)
