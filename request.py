import requests
import json

with open("urls.json") as f:
    urls = json.load(f)

url_code = [{"url":u} for u in urls]
up_count = 0
down_count = 0


for items in url_code:
    target_url = items
    try:
        response = requests.get(target_url["url"], timeout=5)  
        items['status'] = response.status_code   
        items['elapsed'] = response.elapsed.total_seconds()    
        print(f"{items['url']} -> {response.status_code}, {items['elapsed']}")
        if items['status'] < 400:
            up_count += 1    
        else:
            down_count += 1
    except requests.exceptions.RequestException:
        items['elapsed'] = None
        print(f"{items['url']} -> DOWN, {items['elapsed']}")
        items['status'] = "DOWN"
        down_count += 1



with open("url_report.json", "w") as f:
    json.dump(url_code, f, indent=4)

print(f"Total sites up {up_count}, Total sites down {down_count}")




     


