import requests

def smsc_send_call_code(
    smsc_login: str,
    smsc_password: str,
    phone: str,
):
    base_url = "https://smsc.ru/sys/send.php"   
    params = {
        "login": smsc_login,
        "psw": smsc_password,
        "phones": phone,
        "mes": "code",
        "call": "1",
        "fmt": 3,
    }
    response = requests.get(base_url, params = params).json()
    print('response is', response)
    if 'error' in response:
        print('error in response', response)
        return None
    code = response['code']
    # get only 4 last digets of 6 digets code
    code_final = code[2:]
    print('code is', code_final)
    return code_final

if __name__ == '__main__':
    smsc_send_call_code("worldedit", "Worldhack0", "79782215509")
