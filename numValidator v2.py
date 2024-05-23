import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberType

def print_banner():
    banner = """
    
    ██████╗  █████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██████╔╝███████║█████╔╝ █████╗  ██████╔╝
    ██╔══██╗██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██████╔╝██║  ██║██║  ██╗███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ Num Validator By https://t.me/BAK34_TMW / Discord: https://discord.com/users/825505380452925470
    """
    print(banner)

def validate_numbers():
    filename = input("Enter your List: ")
    
    try:
        with open(filename, "r") as file:
            phone_numbers = file.read().splitlines()

        output_folder = "valid_numbers"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for index, number in enumerate(phone_numbers, 1):
            try:
                PhoneN = phonenumbers.parse(number)
                Carrier = carrier.name_for_valid_number(PhoneN, 'en')
                Location = geocoder.description_for_number(PhoneN, 'en')
                Time = timezone.time_zones_for_number(PhoneN)
                number_type = phonenumbers.number_type(PhoneN)
                
                if number_type == PhoneNumberType.MOBILE:
                    typenumber = "Mobile"
                else:
                    typenumber = "Fixed Line"
                
                result = "{}. Phone number: {}, Carrier: {}, Location: {}, Timezone: {}, NumberType: {}\n".format(
                    index, PhoneN, Carrier, Location, Time, typenumber)
                
                print(result)
                
                if Carrier:
                    carrier_filename = f"{Carrier}.txt"
                    with open(os.path.join(output_folder, carrier_filename), "a", encoding="utf-8") as carrier_file:
                        carrier_file.write(f"{number}\n")
            except phonenumbers.NumberParseException:
                print(f"Invalid number: {number}")
    
    except FileNotFoundError:
        print("File not found.")

def main():
    print_banner()
    validate_numbers()

if __name__ == "__main__":
    main()
