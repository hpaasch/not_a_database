import csv


def activity():
    action = input("(C)reate new user? (Q)uit? ").lower()  # add modify later.
    # if choose M, then present login row without username and allow changes. do a series?
    if action == "c":
        user_profile()
    else:
        login()


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
                        activity()
                        return row
            else:
                print("Login failed. Try again.")


def unique_name_check(username):
    with open("data_not.csv") as outfile:
        user_data = csv.DictReader(outfile,
                                   fieldnames=["username", "password", "full_name", "dog_count"])
        for row in user_data:
            if row["username"].lower() == username.lower():
                print("That username is taken. Try another.")
                user_profile()


def user_profile():
    username = input("Type in a new username: ")
    unique_name_check(username)
    password = input("Set a password: ")
    full_name = input("Full name: ")
    dog_count = int(input("How many dogs in the home? "))

    profile = "{},{},{},{}\n".format(
        username, password, full_name, dog_count)

    with open("data_not.csv", "a") as infile:
        infile.write(profile)

    activity()
    return profile


def modify_user():
    pass


login()
