import requests
import sys

def send_request(value):
    url = "http://localhost:7081/infer"
    data = [{"format": "wav", "sampling_rate": 22050, "text_flag": 0, "value": value}]

    response = requests.post(url, json=data)
    result = response.json()
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <value>")
        sys.exit(1)

    value = sys.argv[1]
    result = send_request(value)
    print(result)
