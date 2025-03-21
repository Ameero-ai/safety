import os
import json

def check_vulnerabilities():
    # Run safety check
    os.system('pip install safety')
    result = os.popen('safety check --json').read()
    vulnerabilities = json.loads(result)

    if vulnerabilities:
        print("Vulnerabilities found:")
        for vulnerability in vulnerabilities:
            print(f"- {vulnerability['package_name']} ({vulnerability['affected_versions']}): {vulnerability['vulnerability']}")
    else:
        print("No vulnerabilities found.")


if __name__ == "__main__":
    check_vulnerabilities()