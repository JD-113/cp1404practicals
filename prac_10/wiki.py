import wikipedia
from wikipedia import PageError, DisambiguationError

user_search = input("Enter page title: ")
while user_search != "":
    try:
        user_page = wikipedia.page(user_search)
        print(user_page)
        print(f'{wikipedia.summary(user_page)}')
        print(f'{user_page.url}')

    except PageError:
        print(f"Page id '{user_search}' does not match any pages. Try another id!")
    except DisambiguationError:
        print(f'We need a more specific title. Try one of the following, or a new search: ',
              wikipedia.page(user_search, auto_suggest=True))
    user_search = input("Enter page title: ")
print("Thank you.")