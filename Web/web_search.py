# It's a commmand line utility for run the search from the command-line.
import requests
import pyperclip


def search(query, result_number, include_link, include_title, copy_link):
    api_key = "AIzaSyC9jy1xelZMzZebRmX2L5LTeXbxhROxCxc"
    search_engine_id = "21bbb3141eea84a9a"
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"

    try:
        print("Searching across web.....")
        response = requests.get(url)
        data = response.json()
        if "items" in data:
            results = data["items"]
            if 0 < result_number <= len(results):
                result = results[result_number - 1]
                snippet = result["snippet"]
                link = result["link"]
                title = result["title"]
                print(f"Result {result_number}:")
                if include_title:
                    print(f"Title: {title}")
                print(f"Snippet: {snippet}")
                if include_link:
                    print(f"Link: {link}")
                    if copy_link:
                        pyperclip.copy(link)
                        print("Link Copied to the clipboard.")
            else:
                print(f"Error: Result number {result_number} out of range.")
        else:
            print("No results found.")
    except Exception as e:
        print("Error occurred:", e)
