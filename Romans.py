if __name__ == "__main__":
    N = float(input())
    engmile = 5280
    romanmile = 4854

    translate = N*(engmile/romanmile)*1000
    print(round(translate))
