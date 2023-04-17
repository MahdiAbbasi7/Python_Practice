def isValid(ip):
    ip = ip.split(".")

    for i in ip:
        if i == "":
            return False
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        return True

def convertor(string):

    if len(string) > 12:
        return []
    newip = string
    lst = []

    for i in range(1, len(string) - 2):
        for j in range(i + 1, len(string) - 1):
            for k in range(j + 1, len(string)):
                newip = newip[:k] + "." + newip[k:]
                newip = newip[:j] + "." + newip[j:]
                newip = newip[:i] + "." + newip[i:]

                if isValid(newip):
                    lst.append(newip)
                    newip = string
    for ip in lst:
        print(ip)


string = input("")
convertor(string)