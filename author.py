
applications = []


def add_application(name, author, version, publishing_year, price):
    applications.append({
        "name": name,
        "author": author,
        "version": version,
        "publishing_year": publishing_year,
        "price": price
    })

# Function to display all details of applications by a given author
def display_applications_by_author(author):
    for app in applications:
        if app["author"] == author:
            print("Name:", app["name"])
            print("Author:", app["author"])
            print("Version:", app["version"])
            print("Publishing Year:", app["publishing_year"])
            print("Price:", app["price"])
            print()

def sort_applications_by_price():
    sorted_apps = sorted(applications, key=lambda x: x["price"])
    for app in sorted_apps:
        print("Name:", app["name"])
        print("Author:", app["author"])
        print("Version:", app["version"])
        print("Publishing Year:", app["publishing_year"])
        print("Price:", app["price"])
        print()


def display_applications_by_publisher_and_year(publisher, year):
    for app in applications:
        if app["author"] == publisher and app["publishing_year"] == year:
            print("Name:", app["name"])
            print("Author:", app["author"])
            print("Version:", app["version"])
            print("Publishing Year:", app["publishing_year"])
            print("Price:", app["price"])
            print()


def sort_applications_by_author_and_publishing_year():
    sorted_apps = sorted(applications, key=lambda x: (x["author"], x["publishing_year"]))
    for app in sorted_apps:
        print("Name:", app["name"])
        print("Author:", app["author"])
        print("Version:", app["version"])
        print("Publishing Year:", app["publishing_year"])
        print("Price:", app["price"])
        print()


add_application("App1", "Author1", "1.0", 2020, 50.00)
add_application("App2", "Author2", "2.0", 2021, 30.00)
add_application("App3", "Author1", "1.5", 2019, 40.00)
add_application("App4", "Author3", "3.0", 2022, 60.00)



