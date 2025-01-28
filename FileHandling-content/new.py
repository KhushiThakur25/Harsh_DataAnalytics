# import phonenumbers
# from phonenumbers import geocoder
# phone_number = phonenumbers.parse("+916397280197")
# print("\nPhone Number Location")
# print(geocoder.description_for_number(phone_number,"en"))


import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_number_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        country = geocoder.description_for_number(parsed_number, 'en')
        carrier_name = carrier.name_for_number(parsed_number, 'en')

        return {
            'country': country,
            'carrier': carrier_name
        }
    except Exception as e:
        return {
            'error': str(e)
        }

# Example usage:
phone_number = "+1234567890"  # Replace with the phone number you want to trace
info = get_phone_number_info(phone_number)
print(info)