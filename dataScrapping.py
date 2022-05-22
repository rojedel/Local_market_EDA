from bs4 import BeautifulSoup
import requests
import datetime as dt
from csv import writer



with open('heb-groceries-mex5212022.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ["Product_Id", "title", "price", "brand", "department", "store", "date"]
    thewriter.writerow(header)

    page = 1
    while page != 106:
        abarrotes_url = f"https://www.heb.com.mx/super/abarrotes?p={page}"
        abarrotes_page = requests.get(abarrotes_url)
        abarrotes_soup = BeautifulSoup(abarrotes_page.content, 'html.parser')
        abarrotes_lists = abarrotes_soup.find_all('div', class_="product details product-item-details")


        for list in abarrotes_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            abarrotes_data =[product_id, title, price, brand, "Abarrotes", "HEB", date]
            thewriter.writerow(abarrotes_data)
        page = page + 1

    page = 1
    while page != 17:
        frutas_verduras_url = f"https://www.heb.com.mx/super/frutas-y-verduras?p={page}"
        frutas_verduras_page = requests.get(frutas_verduras_url)
        frutas_verduras_soup = BeautifulSoup(frutas_verduras_page.content, 'html.parser')
        frutas_verduras_lists = frutas_verduras_soup.find_all('div', class_="product details product-item-details")

        for list in frutas_verduras_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            frutas_verduras_data =[product_id, title, price, brand, "Frutas-Verduras", "HEB", date]
            thewriter.writerow(frutas_verduras_data)
        page = page + 1

    page = 1
    while page != 30:
        lacteos_url = f"https://www.heb.com.mx/super/lacteos?p={page}"
        lacteos_page = requests.get(lacteos_url)
        lacteos_soup = BeautifulSoup(lacteos_page.content, 'html.parser')
        lacteos_lists = lacteos_soup.find_all('div', class_="product details product-item-details")

        for list in lacteos_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            lacteos_data =[product_id, title, price, brand, "Lacteos", "HEB", date]
            thewriter.writerow(lacteos_data)
        page = page + 1

    page = 1
    while page != 12:
        carnes_pescados_url = f"https://www.heb.com.mx/super/carnes-y-pescados?p={page}"
        carnes_pescados_page = requests.get(carnes_pescados_url)
        carnes_pescados_soup = BeautifulSoup(carnes_pescados_page.content, 'html.parser')
        carnes_pescados_lists = carnes_pescados_soup.find_all('div', class_="product details product-item-details")

        for list in carnes_pescados_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            carnes_pescados_data =[product_id, title, price, brand, "Carnes y Pescado", date]
            thewriter.writerow(carnes_pescados_data)
        page = page + 1

    while page != 16:
        congelados_url = f"https://www.heb.com.mx/super/congelados?p={page}"
        congelados_page = requests.get(congelados_url)
        congelados_soup = BeautifulSoup(congelados_page.content, 'html.parser')
        congelados_lists = congelados_soup.find_all('div', class_="product details product-item-details")

        for list in congelados_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            congelados_data =[product_id, title, price, brand, "Congelados", "HEB", date]
            thewriter.writerow(congelados_data)
        page = page + 1

    page = 1
    while page != 21:
        salchichoneria_url = f"https://www.heb.com.mx/super/salchichoneria?p={page}"
        salchichoneria_page = requests.get(salchichoneria_url)
        salchichoneria_soup = BeautifulSoup(salchichoneria_page.content, 'html.parser')
        salchichoneria_lists = salchichoneria_soup.find_all('div', class_="product details product-item-details")

        for list in salchichoneria_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            salchichoneria_data =[product_id, title, price, brand, "Salchichoneria", "HEB", date]
            thewriter.writerow(salchichoneria_data)
        page = page + 1

    page = 1
    while page != 79:
        bebidas_botanas_url = f"https://www.heb.com.mx/super/bebidas-botanas-y-dulces?p={page}"
        bebidas_botanas_page = requests.get(bebidas_botanas_url)
        bebidas_botanas_soup = BeautifulSoup(bebidas_botanas_page.content, 'html.parser')
        bebidas_botanas_lists = bebidas_botanas_soup.find_all('div', class_="product details product-item-details")

        for list in bebidas_botanas_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            bebidas_botanas_data =[product_id, title, price, brand, "Bebidas y Botanas", "HEB", date]
            thewriter.writerow(bebidas_botanas_data)
        page = page + 1

    page = 1
    while page != 19:
        panaderia_tortillas_url = f"https://www.heb.com.mx/super/panaderia-y-tortillas?p={page}"
        panaderia_tortillas_page = requests.get(panaderia_tortillas_url)
        panaderia_tortillas_soup = BeautifulSoup(panaderia_tortillas_page.content, 'html.parser')
        panaderia_tortillas_lists = panaderia_tortillas_soup.find_all('div', class_="product details product-item-details")

        for list in panaderia_tortillas_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            panaderia_tortillas_data =[product_id, title, price, brand, "Panaderia y Tortillas", "HEB", date]
            thewriter.writerow(panaderia_tortillas_data)
        page = page + 1

    page = 1
    while page != 16:
        reposteria_url = f"https://www.heb.com.mx/super/horneado-y-reposteria?p={page}"
        reposteria_page = requests.get(reposteria_url)
        reposteria_soup = BeautifulSoup(reposteria_page.content, 'html.parser')
        reposteria_lists = reposteria_soup.find_all('div', class_="product details product-item-details")

        for list in reposteria_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            reposteria_data =[product_id, title, price, brand, "Reposteria y horneado", "HEB", date]
            thewriter.writerow(reposteria_data)
        page = page + 1

    page = 1
    while page != 17:
        dulceria_url = f"https://www.heb.com.mx/super/dulceria?=p{page}"
        dulceria_page = requests.get(dulceria_url)
        dulceria_soup = BeautifulSoup(dulceria_page.content, 'html.parser')
        dulceria_lists = dulceria_soup.find_all('div', class_="product details product-item-details")

        for list in dulceria_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            dulceria_data =[product_id, title, price, brand, "Dulceria", "HEB", date]
            thewriter.writerow(dulceria_data)
        page = page + 1

    page = 1
    while page != 29:
        limpieza_url = f"https://www.heb.com.mx/super/limpieza-lavanderia-y-desechables?p={page}"
        limpieza_page = requests.get(limpieza_url)
        limpieza_soup = BeautifulSoup(limpieza_page.content, 'html.parser')
        limpieza_lists = limpieza_soup.find_all('div', class_="product details product-item-details")

        for list in limpieza_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            limpieza_data =[product_id, title, price, brand, "Limpieza", "HEB", date]
            thewriter.writerow(limpieza_data)
        page = page + 1

    page = 1
    while page != 13:
        internacional_url = f"https://www.heb.com.mx/super/sabores-del-mundo?p={page}"
        internacional_page = requests.get(internacional_url)
        internacional_soup = BeautifulSoup(internacional_page.content, 'html.parser')
        internacional_lists = internacional_soup.find_all('div', class_="product details product-item-details")

        for list in internacional_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            internacional_data = [product_id, title, price, brand, "Internacional", "HEB", date]
            thewriter.writerow(internacional_data)
        page = page + 1

    page = 1
    while page != 33:
        saludable_url = f"https://www.heb.com.mx/super/vive-saludable?p={page}"
        saludable_page = requests.get(saludable_url)
        saludable_soup = BeautifulSoup(saludable_page.content, 'html.parser')
        saludable_lists = saludable_soup.find_all('div', class_="product details product-item-details")

        for list in saludable_lists:
            product_id = list.find('a', class_="product-item-link")
            product_id = str(product_id)
            product_id = product_id[46:53]
            title = list.find('a', class_="product-item-link").text
            price = list.find('span', class_="price").text
            brand = list.find('div', class_= "category-brand").text
            today = dt.datetime.now()
            date = today.strftime("%m/%d/%Y")
            saludable_data =[product_id, title, price, brand, "Saludable", "HEB", date]
            thewriter.writerow(saludable_data)
        page = page + 1











