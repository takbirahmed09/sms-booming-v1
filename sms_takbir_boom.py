import requests

phone = "01617718574"
url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=01617718574"

response = requests.get(url) # এখানে ডাটা লিংকের শেষেই পাঠানো হয়েছে
print(response.status_code) # ২০০ মানে সফল
