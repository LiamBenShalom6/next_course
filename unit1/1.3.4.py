def get_real_password(string):
    return str([chr((ord(x) - 2 - 97) % 26 + 97) if x != " " else x for x in string])

def main():
    c = 'a'
    print("The ASCII value of '" + c + "' is", ord(c))
    map(print, get_real_password("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))
    print(get_real_password("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))


if __name__ == '__main__':
    main()