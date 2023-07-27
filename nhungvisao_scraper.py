import requests
import json
import csv

def scrape_data_from_api():
    cookies = {
        '_ga': 'GA1.1.1937375067.1690250574',
        '_fbp': 'fb.1.1690250574814.816236946',
        '_ga_NJF8DBC7E8': 'GS1.1.1690250574.1.1.1690252740.0.0.0',
    }

    headers = {
        'authority': 'nhungvisao.com',
        '__requestverificationtoken': 'aZqg4BLgHwPo7HqbAxgNSwxn79_id8vgl3pjweRl2Rz6h9oGQda03p6mx7_-_Z8CtrboK7atViGthy7PMyp4-oLXHOER5N2eHSaVw8BjOX41:JutvM0ZhFlSSbXBsu1et8vcC03XboM8msMNNRZxKMzwh5eL1_qznLteOYkQRHalQFlQ7XgLLn8DuBa0OqInVGoaKuNFPiPvOsKCYmHQ0t9M1',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_ga=GA1.1.1937375067.1690250574; _fbp=fb.1.1690250574814.816236946; _ga_NJF8DBC7E8=GS1.1.1690250574.1.1.1690252740.0.0.0',
        'origin': 'https://nhungvisao.com',
        'referer': 'https://nhungvisao.com/products?search=page2',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.183',
    }

    json_data = {
        'search': '',
        'age': ';18+',
        'bookCoverTypeId': 0,
        'bookColorId': 0,
        'metarial': 0,
        'isLimited': 0,
        'languague': 0,
        'bookType': 0,
        'sortBy': 1,
        'hashtag': '',
        'pageIndex': 0,
        'pageSize': 20,
    }

    with open('list_book_18+.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Mã sách', 'Tên sách', 'Giá bìa', 'Giá chiết khấu']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            response = requests.post('https://nhungvisao.com/products/Search', cookies=cookies, headers=headers, json=json_data)
            data = response.json()
            result = data.get('result')  # Get the 'result' field from the response

            if not result:  # If the 'result' field is empty or null, break the loop
                break

            data_list = json.loads(result)
            
            if not data_list:  # If the list of data is empty, break the loop
                break

            # Process the data here
            for item in data_list:
                product_id = item['Id']
                product_name = item['ProductName']
                org_price = item['OrgPriceStrVn']
                discount_price = item['BasePriceStrVn']

                print(f"Mã sách: {product_id}, Tên sách: {product_name}, Giá bìa: {org_price}, Giá chiết khấu: {discount_price}")
                writer.writerow({'Mã sách': product_id, 'Tên sách': product_name, 'Giá bìa': org_price, 'Giá chiết khấu': discount_price})

            # Update your JSON data if necessary before making the next API request
            # For example, you can use the 'skip' parameter to paginate through the data
            # json_data['skip'] += 10  # Assuming 'skip' is a parameter to skip results
            json_data['pageIndex'] += 1

# Call the function to start scraping
scrape_data_from_api()