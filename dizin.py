
import requests
import time

def scan(wordlist,target,time_second):
    
    try:
        with open(wordlist,"r") as file:
            worldlist_word=file.read().splitlines()

    except Exception as e:
        print(f"Wordlist açılırken hata olustu Kodu:{e}")

    test="not_real"
    test_url=f"{target}/{test}"
    test_response=requests.get(test_url,timeout=5,allow_redirects=True)
    test_redirect=test_response.content


    find_direct=[]
    for word in worldlist_word:
        check=f"{target}/{word}"
        

        try:
            response=requests.get(check,timeout=5,allow_redirects=True)
            redirect_location=response.content
            if response.status_code in [200,301,302,403]:
                if redirect_location and redirect_location==test_redirect:
                    time.sleep(time_second)
                    continue
                else:
                    print(f"{response.status_code} -> {check}")
                    find_direct.append(f"{response.status_code} -> {check}")
                    time.sleep(time_second)
        except Exception as e:
            print(f"Hata {e}")

    if find_direct:
        print("Bulunan Dizinler")
        for i in find_direct:
            print(f"Bulunan dizi {i}")
        with open("result.txt","a+") as file:
            for i in find_direct:
                file.write(i+"\n")
                
                
                

                
    else:
        print("Hiçbir Dizin bulunamadı")
wordlist=input("Wordlist Giriniz: ")
target=input("Hedef Url Giriniz: ")
time_second=int(input("Kaç Sanıye beklensin: "))


scan(wordlist,target,time_second)
