from AddressToCoordinate import *
from optimizeRoad import *

address = 'דיזנגוף 48 נתניה'
address2 = "ניסים אלוני 16 תל אביב"
address3 = "השיקמים 5 אור עקיבא"
address4 = "הר שלמה 3 אור עקיבא"
address5 = "גדליהו 5 חיפה"
address6 = "הגפן 17 קרית אתא"
list_of_addresses = [ address2, address3, address4, address5, address6]

print(optimizeRoad(list_of_addresses, address, address))

