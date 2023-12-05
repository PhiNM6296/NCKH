import requests

url= "https://www.hnx.vn/cophieu-etfs/chi-tiet-chung-khoan-ny-AAV.html?_des_tab=2"
#url2= "https://github.com/psf/requests/issues/6537"
r = requests.get(url2,verify=True)

print(r.status_code)