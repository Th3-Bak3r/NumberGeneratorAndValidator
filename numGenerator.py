import requests
import json

API_KEY = "61eff0ad2dc64c3388d1cdecc0bb0898"

def print_banner():
    banner = """
    
    ██████╗  █████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██████╔╝███████║█████╔╝ █████╗  ██████╔╝
    ██╔══██╗██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██████╔╝██║  ██║██║  ██╗███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ Num Generator By https://t.me/BAK34_TMW / Discord: https://discord.com/users/825505380452925470
    """
    print(banner)

def generate_numbers():
    country_code = input("Enter country code (e.g., US): ")
    num_count = int(input("Enter the number of numbers to generate: "))

    headers = {
        "X-Api-Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "CountryCode": country_code,
        "Quantity": num_count
    }

    response = requests.get("https://randommer.io/api/Phone/Generate", params=params, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            filename = f"{country_code}_generated_numbers.txt"
            with open(filename, "w") as file:
                for number in data:
                    file.write(number + "\n")
                    print(number)
            print(f"Generated numbers saved to {filename}")
        except json.decoder.JSONDecodeError:
            print("Failed to decode JSON response:", response.text)
    else:
        print("Failed to retrieve data from API:", response.text)

def main():
    print_banner()
    print("Generate random phone numbers.")
    generate_numbers()

if __name__ == "__main__":
    main()
