
import csv
from pathlib import Path

import requests

BASE_URL = "http://127.0.0.1:3000"
ENDPOINT = "/rest/products/search"

test_inputs = [
    "banana",
    "apple",
    "'",
    "')",
    "')) OR 1=1--"
]

output_file = Path("reports/input_test_results.csv")
output_file.parent.mkdir(parents=True, exist_ok=True)

results = []

print("=== Automated Web Application Input Testing ===")

for test_input in test_inputs:
    try:
        response = requests.get(
            BASE_URL + ENDPOINT,
            params={"q": test_input},
            timeout=10
        )

        status = response.status_code

        if status >= 500:
            result = "SERVER ERROR"
        elif status >= 400:
            result = "CLIENT ERROR"
        else:
            result = "REQUEST COMPLETED"

        results.append({
            "input": test_input,
            "http_status": status,
            "result": result,
            "response_length": len(response.content)
        })

        print(f"{test_input!r}: HTTP {status} - {result}")

    except requests.RequestException as error:
        results.append({
            "input": test_input,
            "http_status": "",
            "result": "REQUEST FAILED",
            "response_length": 0
        })
        print(f"Request failed: {error}")

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "input",
            "http_status",
            "result",
            "response_length"
        ]
    )
    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to: {output_file}")
