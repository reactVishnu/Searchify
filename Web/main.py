import sys
from web_search import search


def print_usage():
    print(
        "Usage: python script_name.py <query> [--no=N] [--link=true/false] [--title=true/false] [--copy=true/false]"
    )


def print_help():
    print("Search Script Help:")
    print("  -h, --help          Display this help message")
    print("  <query>             The search query")
    print("Options:")
    print("  --no=N              Specify the result number to display (default: 1)")
    print("  --link=true/false   Include link in the search result (default: false)")
    print("  --title=true/false  Include title in the search result (default: false)")
    print("  --copy=true/false   Copy link to clipboard (default: false)")


# The Main Function
if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print_help()
        sys.exit(0)
    elif len(sys.argv) < 2:
        print(
            "Usage: python script_name.py <query> [--no=N] [--link=true/false] [--title=true/false]"
        )
        sys.exit(1)

    query = ""
    result_number = 1  # Default result number to display
    include_link = False  # Default option to include link
    include_title = False  # Default option to include title
    copy_link = False


    for arg in sys.argv[1:]:
        if arg.startswith("--no="):
            try:
                result_number = int(arg.split("=")[1])
            except ValueError:
                print("Invalid result number. Please provide an integer value.")
                sys.exit(1)
        elif arg.startswith("--link="):
            include_link_str = arg.split("=")[1].lower()
            if include_link_str in ["true", "false"]:
                include_link = include_link_str == "true"
            else:
                print("Invalid value for --link option. Please provide 'true' or 'false'.")
                sys.exit(1)
        elif arg.startswith("--title="):
            include_title_str = arg.split("=")[1].lower()
            if include_title_str in ["true", "false"]:
                include_title = include_title_str == "true"
            else:
                print("Invalid value for --title option. Please provide 'true' or 'false'.")
                sys.exit(1)
        elif arg.startswith("--copy="):
            copy_link_str = arg.split("=")[1].lower()
            if copy_link_str in ["true", "false"]:
                copy_link = copy_link_str == "true"
            else:
                print("Invalid value for --copy option. Please provide 'true' or 'false'.")
                sys.exit(1)
        else:
            query += arg + " "

    query = query.strip()
    search(query, result_number, include_link, include_title, copy_link)
