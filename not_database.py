import csv


def user_creation():
    username = input("Type in a username: ")
    password = input("Set a password: ")
    first_name = input("First name: ").lower()
    last_name = input("Last name: ").lower()
    dog_count = int(input("How many dogs in the home? "))
    boat_count = int(input("How many boats are at the house? "))

    profile = "{},{},{},{},{},{}".format(
        username, password, first_name, last_name, dog_count, boat_count)

    with open("data_not.csv", "a") as infile:
        infile.write(profile)

    return profile


def verify_login():
    while True:
        login_name = input("Username: ")
        # login_password = input("Password: ")

        with open("data_not.csv") as outfile:
            user_data = csv.DictReader(outfile, fieldnames=["username", "password"])
            for row in user_data:
                if row["username"] == login_name:
                    print("name good.")
                    return False
                else:
                    print("es no bueno")


    # return login_status


def modify_user():
    pass


def logout():
    pass


# user_inputs()
verify_login()
