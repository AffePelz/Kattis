inp = int(input())

if __name__ == "__main__":
    l = []
    keys = "keys"
    phone = "phone"
    wallet = "wallet"
    for i in range(inp):
        k = input()
        l.append(k)
    if keys not in l:
        print(keys)
    if phone not in l:
        print(phone)
    if wallet not in l:
        print(wallet)
    if keys in l and wallet in l and phone in l:
        print("ready")
