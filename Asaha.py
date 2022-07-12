import phonenumbers 
from phonenumbers import timezone,geocoder,carrier


number = input("Enter Your Phone Number: ")

> External Libraries

phone = phonenumbers.parse(number)

Scratches and Consoles

time = timezone.time_zones_for_number (phone)

sim_details = carrier.name_for_number (phone, "en")

register geocoder.description_for_number (phone, "en")


print (number)
print (phone)



print(time)

13

print (sim details)

14

print (register)
