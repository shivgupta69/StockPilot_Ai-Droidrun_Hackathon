import json

def analyze_stock(data):
    score = 0

    if data.get("roe", 0) >= 20:
        score += 1
    if data.get("pe", 100) <= 30:
        score += 1
    if data.get("price", 0) >= 0.9 * data.get("high_52w", 0):
        score += 1

    if score >= 3:
        return "STRONG FUNDAMENTALS"
    elif score == 2:
        return "MODERATE FUNDAMENTALS"
    else:
        return "WEAK FUNDAMENTALS"


if __name__ == "__main__":
    with open("stock_data.json") as f:
        data = json.load(f)

    verdict = analyze_stock(data)

    print("📊 Stock Analysis Result")
    print("-----------------------")
    print("Data:", data)
    print("Verdict:", verdict)
