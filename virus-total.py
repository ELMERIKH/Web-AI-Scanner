import sys
import virustotal_python
from base64 import urlsafe_b64encode
import hashlib
from colorama import Fore, Style

def calculate_sha256(url):
    sha256_hash = hashlib.sha256(url.encode()).hexdigest()
    return sha256_hash

def scan_url(v_url, output_file):
    vtotal_api_key = "6614755a9647849cf6148f1ecf6310a1dfb8bc22bc8d46d04e042b8d208d1264"

    # Calculate SHA-256 hash of the URL
    url_hash = calculate_sha256(v_url)

    with virustotal_python.Virustotal(vtotal_api_key) as vtotal:
        try:
            resp = vtotal.request("urls", data={"url": v_url}, method="POST")
            # Safe encode URL in base64 format
            # https://developers.virustotal.com/reference/url
            url_id = urlsafe_b64encode(v_url.encode()).decode().strip("=")
            report = vtotal.request(f"urls/{url_id}")
            v_result_url = report.data['attributes']['last_analysis_stats']
            result_message = f"URL: {v_url}\nSHA-256 Hash: {url_hash}\nAnalysis Result:\n"
            if v_result_url['malicious'] > 0:
                result_message += "Malicious: This URL is malicious\n"
            elif v_result_url['suspicious'] > 0:
                result_message += "Suspicious: This URL is suspicious\n"
            else:
                result_message += "Safe: This URL is safe\n"
            with open(output_file, 'a') as file:
                file.write("[+] Virus-total scan:\n"+result_message)
            print(f"Analysis result written to {output_file}")
        except virustotal_python.VirustotalError as err:
            print(f"Failed to send URL for analysis and get the report: {err}")

# Extract the URL and output file from command-line arguments
if len(sys.argv) != 3:
    print("Usage: python virus-total.py <url> <output_file>")
    sys.exit(1)

url_to_scan = sys.argv[1]
output_file = sys.argv[2]
scan_url(url_to_scan, output_file)