import csv


def login():
    print("This data is top secret, even by Gen. Petraeus standards. Login to continue.")
    while True:
        login_name = input("Username: ")
        login_password = input("Password: ")

        with open("data_not.csv") as outfile:
            user_data = csv.DictReader(outfile,
                                       fieldnames=["username", "password", "full_name", "dog_count"])
            for row in user_data:
                if row["username"] == login_name:
                    if row["password"] == login_password:
                        print("Login successful.")
                        print(row)  # make this pretty
                        return row
            else:
                print("Login failed. Try again.")


def activity():
    action = input("(C)reate new user? (Q)uit? ").lower()  # add modify later
    if action == "c":
        user_creation()
    else:
        login()


def user_creation():
    while True:
        username = input("Type in a new username: ")
        with open("data_not.csv") as outfile:
            user_data = csv.DictReader(outfile,
                                       fieldnames=["username", "password", "full_name", "dog_count"])
            for row in user_data:
                if row["username"].lower() == username.lower():
                    print("That username is taken. Try another.")
            else:
                return username
    password = input("Set a password: ")
    full_name = input("Full name: ")
    dog_count = int(input("How many dogs in the home? "))

    profile = "{},{},{},{}".format(
        username, password, full_name, dog_count)

    with open("data_not.csv", "a") as infile:
        infile.write(profile)

    print(profile)
    return profile


def modify_user():
    pass


# login()
user_creation()
# login()
# activity()


