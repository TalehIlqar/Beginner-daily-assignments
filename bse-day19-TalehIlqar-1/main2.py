import requests

x = input("input gotur: ")
# facebook.com/

try:
    response = requests.get(f"https://{x}")
    print ('Status code [200]')

except:
    print ('Status code [404]')

# import requests
# from requests.exceptions import MissingSchema, ConnectionError
# while True:
#     url = input()
#     try:
#         response = requests.get(url)
#     except MissingSchema:
#         print("Protokol elave edin. (ex: https://facebook.com)")
#     except ConnectionError:
#         print("Bağlantı qurulmadı. Domaini doğru yazın. (ex: https://facebook.com)")
#     else:
#         if response.status_code == 404:
#             print("Sehife tapılmadı")
#         else:
#             print("Bağlantı quruldu")
#         break
