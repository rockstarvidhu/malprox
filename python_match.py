http_status = 303

match http_status:
     
    case 200 | 201:
        print("success")
    case 401:
        print("not found")
    case 500:
        print("server not found")
    case _:
        print("error")

#match statement checks one condition with several other conditions until the desired condition is met
