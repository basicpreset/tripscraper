import getphone
import getbusiness
import getaddress
import xlwt
from xlwt import Workbook

website_base_url = 'https://www.tripadvisor.co.hu'

wb = Workbook()
sheet1 = wb.add_sheet('Elérhetőségek') 

name_pos = 1
phone_pos = 1
business_pos = 1

sheet1.write(0,0, 'Név')
sheet1.write(0,1, "Cím")
sheet1.write(0,2, "Telefonszám")

with open('./restaurants_raw.txt') as f:
    restaurant_list_raw = f.read().splitlines()
    restaurant_list_clean = list(dict.fromkeys(restaurant_list_raw))
    f.close()
    print(len(restaurant_list_clean))
    for element in restaurant_list_clean:
        clean_file = open("restaurants_clean_v1.2.txt", "a")
        businessURL = website_base_url + element
        businessName = getbusiness.getBusiness(businessURL)
        businessPhone = getphone.getPhone(businessURL)
        businessAddress = getaddress.get(businessURL)
        if businessName is not None and businessPhone is not None and businessAddress is not None:
            sheet1.write(name_pos,0, businessName)
            name_pos += 1
            sheet1.write(business_pos,1, businessAddress)
            business_pos += 1
            sheet1.write(phone_pos,2, businessPhone)
            phone_pos += 1
            clean_file.write(businessName + ', ' + businessPhone + '\n')
        wb.save('Magyarorszagi Ettermek v1.2.xls') 
        clean_file.close()
        print('Added entry: ' + businessName)