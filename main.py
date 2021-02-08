import phonenumbers
from test import number
from phonenumbers import geocoder

print(geocoder.description_for_number(phonenumbers.parse(number, 'CH'), "en"))

from phonenumbers import carrier

service_p=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_p,"en"))

