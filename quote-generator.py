import requests
import textwrap

def get_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        quote = data['content']
        author = data['author']
        return quote, author
    except requests.exceptions.RequestException as e:
        return "Failed to fetch quote.", str(e)

def display_quote():
    quote, author = get_quote()
    print("\n" + "-"*60)
    print("\n".join(textwrap.wrap(quote, width=60)))
    print(f"\n— {author}")
    print("-"*60)

if __name__ == "__main__":
    display_quote()

