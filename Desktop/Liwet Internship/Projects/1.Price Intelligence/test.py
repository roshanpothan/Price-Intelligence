from flask import Flask, request, jsonify
import requests
keyword = 'oranges'
keyword = keyword.replace(' ','+')
app = Flask(__name__)
@app.route('/process_data', methods=['GET'])
def process_data():
    keyword = request.args.get('keyword','oranges')
    keyword = keyword.replace(' ','+')

cookie='_fbp=fb.1.1677429315931.1313864373; _pin_unauth=dWlkPU1ETmhOV1l3TUdRdE9HVmlNUzAwTURVNUxXSmtZamN0TXpNNVl6SmtObU5rWkROaQ; ajs_anonymous_id=84c5f7a7-f9d2-4bbe-97fa-5a49e09ab80a; _pin_unauth=dWlkPU1ETmhOV1l3TUdRdE9HVmlNUzAwTURVNUxXSmtZamN0TXpNNVl6SmtObU5rWkROaQ; ajs_anonymous_id=84c5f7a7-f9d2-4bbe-97fa-5a49e09ab80a; __stripe_mid=fd0e7b64-53a7-4e25-b07f-6388af276178ebcd3a; _derived_epik=dj0yJnU9RkJaRU0wci1MOWlwdXRwclhLNVpSaS1WUFJKZDAyWGEmbj1MWjljczA1VXhsdFJ5U2RSMlFaSzl3Jm09MSZ0PUFBQUFBR1J3Yl9ZJnJtPTEmcnQ9QUFBQUFHUndiX1kmc3A9NQ; _gcl_au=1.1.1406692167.1686887871; wfm.tracking.sessionStart=1686887870959; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; __cf_bm=LkIwVb6RZe1faWS9u_nOyVTqrIFQeg69VmqfUlZwDKY-1686887871-0-AYWARownm2AAlk0sAtnvGES9DYJWBQbZ/JQCzLXjS1qwD3Mw2qLaALyjH9TZJ45X4dgmlOlowHWd10Tj7LODYtI=; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY3ODEyMTc0NzM0NTE4MTMxMjgwMTU3ODMwMzUyMzY4MDY1Mjg0NVIPCLyz0PToMBgBKgRJTkQx8AG25eiSjDE=; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; wfmStoreId=16; at_check=true; gpv_pn=Wegmans%20Food%20Markets%3A%20Grocery%20%26%20Meal%20Delivery%20or%20Curbside; s_loginSuccess=0; s_cc=true; wfm.modals.wfmCovidTooltip=1; wfm.tracking.s10=1; wfm.tracking.x2p=1; _derived_epik=dj0yJnU9ZEpOaDU1QWNGMkNPNW5rN3QwQzdXMUFtZzVnd0I0a1Qmbj1XcnZvaU4yQ08ycUR1dFZIZzJhc2VnJm09MSZ0PUFBQUFBR1NMM2dBJnJtPTEmcnQ9QUFBQUFHU0wzZ0Emc3A9NQ; dotcomSearchId=00c39920-91c4-4d97-9ffc-a74e0a4aa305; lux_uid=168688799428813814; _uetsid=f711b9300bf911ee81365bf759874949; _uetvid=7f3b48a0b78c11ed8587a33d8b5d2694; session-prd-weg=.eJwdjstygjAAAP8lZ8eRhw84qsiEQphqMMCFQYmQ8LIEtEmn_16mh73sZfcHZI-BigrYj7wRdAGyJx3avKPdCOxxmGYjqBCs77Kxr2kHbEClV93cOwuZByMFNcQ8azlL7a5f5Yy6683r1ljP9AA3kJcGwiceuifu4z1PsDMiN1mhi1alx4b5GK5SDFXSQj3lkUISCthdVRp7j5x8spAHRqAiE2FHDy5vlpDzmJP1fyvWmxry51SQb-Ef5qnWmijRXkUcsLA7y4JEArZNVcwfAU5MxEsTqdIIutVyax4d52PXYqsiR-nv-xq6X1d3d6rHPn4XNWFS4QRvhCzBAkyCDhkrgG1sjfVurW203z8eDGoX.F21vug.afrCAfAhjB9HBH4998K50HqyThg; _dd_s=rum=1&id=d53d5fff-dba6-4c17-b790-8851c4edfc96&created=1686887995161&expire=1686888895161; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19525%7CMCMID%7C78121747345181312801578303523680652845%7CMCAAMLH-1687492795%7C12%7CMCAAMB-1687492795%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1686895195s%7CNONE%7CvVersion%7C5.5.0; at_check=true; mbox=session#4e9a2a1ebccd489b91eb1dcb5dd96993#1686889856'
URL='https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=false&allow_autocorrect=true&limit=60&offset=0&search_is_autocomplete=false&search_provider=ic&search_term='+keyword+'&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false'

HEADERS = {   

  'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",  
  'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
  'Cookie': cookie 
}
response = requests.get(URL,headers=HEADERS)
data=response.json()
items=data['items']
# result=[]
for item in items:
    # result.append({
    #     'name' : item['name'],
    #     'base_price' : item['base_price'],
    #     'base_quantity' : item['base_quantity'] 
    #     })
#     return jsonify(result)
# if __name__ == '__main__':
#    app.run()
 print(f"name:{item['name']}")
 print(f"base_price:{item['base_price']}")
 print(f"base_quantity:{item['base_quantity']}")
 print(' ')
#  print(data.keys())
# # item_list=[]
# # for item_number in range(len(data['items'])):
# #     item_name = data['items'][item_number]['name']
#     base_price = data['items'][item_number]['base_price']
#     item_dictt ={
#         "item_name" :item_name,
#         "base_price" :base_price 
#     }
#     item_list.append(item_dictt)
#     print(item_list)
#     less_than_5  = filter(lambda x: x['base_price'] < 5, item_list)
# for item in less_than_5:
#     print(f"{item['item_name']}: {item['base_price']}")




   
    