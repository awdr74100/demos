import requests

payload = {
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATE": "/wEPDwUKLTc5ODg3MzA5Ng9kFgICAw9kFhICBQ8QDxYGHg5EYXRhVmFsdWVGaWVsZAULc2VtZXN0ZXJfbm8eDURhdGFUZXh0RmllbGQFDXNlbWVzdGVyX25hbWUeC18hRGF0YUJvdW5kZ2QQFSMP6KuL6YG45pOH5a245pyfFjEwOOWtuOW5tOW6puesrDHlrbjmnJ8SMTA35a245bm05bqm5pqR5pyfFjEwN+WtuOW5tOW6puesrDLlrbjmnJ8WMTA35a245bm05bqm56ysMeWtuOacnxIxMDblrbjlubTluqbmmpHmnJ8WMTA25a245bm05bqm56ysMuWtuOacnxYxMDblrbjlubTluqbnrKwx5a245pyfEjEwNeWtuOW5tOW6puaakeacnxYxMDXlrbjlubTluqbnrKwy5a245pyfFjEwNeWtuOW5tOW6puesrDHlrbjmnJ8SMTA05a245bm05bqm5pqR5pyfFjEwNOWtuOW5tOW6puesrDLlrbjmnJ8WMTA05a245bm05bqm56ysMeWtuOacnxIxMDPlrbjlubTluqbmmpHmnJ8WMTAz5a245bm05bqm56ysMuWtuOacnxYxMDPlrbjlubTluqbnrKwx5a245pyfEjEwMuWtuOW5tOW6puaakeacnxYxMDLlrbjlubTluqbnrKwy5a245pyfFjEwMuWtuOW5tOW6puesrDHlrbjmnJ8SMTAx5a245bm05bqm5pqR5pyfFjEwMeWtuOW5tOW6puesrDLlrbjmnJ8WMTAx5a245bm05bqm56ysMeWtuOacnxIxMDDlrbjlubTluqbmmpHmnJ8WMTAw5a245bm05bqm56ysMuWtuOacnxYxMDDlrbjlubTluqbnrKwx5a245pyfETk55a245bm05bqm5pqR5pyfFTk55a245bm05bqm56ysMuWtuOacnxU5OeWtuOW5tOW6puesrDHlrbjmnJ8ROTjlrbjlubTluqbmmpHmnJ8VOTjlrbjlubTluqbnrKwy5a245pyfFTk45a245bm05bqm56ysMeWtuOacnxE5N+WtuOW5tOW6puaakeacnxU5N+WtuOW5tOW6puesrDLlrbjmnJ8VOTflrbjlubTluqbnrKwx5a245pyfFSMEMDAwMAUxMDgwMQUxMDcwMwUxMDcwMgUxMDcwMQUxMDYwMwUxMDYwMgUx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",
    "__VIEWSTATEGENERATOR": "E6FA358A",
    "__EVENTVALIDATION": "/wEWdwKpoe6rBQKO/LeLCAKk0vqMCAK2to7+AQLBiM+4CgLAiM+4CgLDiM+4CgK69+wVAr337BUCvPfsFQKX3oqCBgKW3oqCBgKZ3oqCBgLwxKj/CwLzxKj/CwLyxKj/CwLts7bUAQLss7bUAQLvs7bUAQLGmtTCBwLJmtTCBwLImtTCBwKjgfK/DQKigfK/DQKlgfK/DQKc6J+UAwKf6J+UAwKe6J+UAwK/0pr9DQK/0vbaBgK/0uKnDwK/0ob9DQK/0vLaBgK/0u6nDwK/0sL+DQK/0r7aBgK/0qqnDwLa/s6tCwLczsakDgKFhI7lDAKvqsPiDAKV6+QIApXr6AgClevsCAKV69AIApXr1AgClevYCAKV69wIApXrwAgCleuECwKV64gLApXrqBUCleusFQKV65AVApXrlBUCleuYFQKV65wVApXrgBUClevEFQKV68gVApXrzBUCleuwFQKV67QVApXruBUCleu8FQKV6+QVApXr6BUClevsFQKV69AVApXr1BUClevYFQKV69wVApXrwBUCleuEFAKV64gUApXrjBQCiuvoCAKK6+wIAorr0AgCiuvUCAKK69gIAorr3AgCiuvACAKK64QLAorriAsCi+vkCAKL6+gIAovr7AgCi+vQCAKL69QIAovr2AgCi+vcCAKL68AIAovrhAsCi+uICwKkrfv9AwKhrfv9AwKkrefGCgKhrefGCgKkrdOrAQKhrdOrAQKkrb+PCAKhrb+PCAKPrf+IAQLDrPv9AwLDrOfGCgLrlvv9AwLrlufGCgLrltOrAQLrlr+PCAK4lv+IAQK3qvv9AwK3qufGCgK3qtOrAQK3qr+PCALsqv+IAQKMpsrVBQKQnf7tBQL3kPrJBVXZdQQGhhD2rxT+i+A05gPAbgmg",
    "dddlSem": "10801",
    "txtTeaName": "",
    "ddlDept": "0G",
    "ddlClass": "4G031",
    "btnCourByClass": "2. 依班級查詢",    
    "txtSub_name": ""
}

res = requests.post("https://webap3.stust.edu.tw/courinfo/default.aspx",data=payload)

print(res.text)