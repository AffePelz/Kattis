if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        K = input().split()
        name = K[0]
        PS_studies = K[1]
        Separate_PS_studies = PS_studies.split("/")
        birth = K[2]
        Separate_birth = birth.split("/")
        NumberOfCourses = int(K[3])

        if int(Separate_PS_studies[0]) >= 2010:
            print(name, "eligible")
        elif int(Separate_birth[0]) >= 1991:
            print(name, "eligible")
        elif (int(Separate_PS_studies[0]) < 2010 or int(Separate_birth[0]) < 1991) and NumberOfCourses >= 41:
            print(name, "ineligible")
        elif int(Separate_PS_studies[0]) < 2010 or int(Separate_birth[0]) < 1991 or NumberOfCourses < 41:
            print(name, "coach petitions")
