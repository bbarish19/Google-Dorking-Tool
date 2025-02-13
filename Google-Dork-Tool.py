import webbrowser
import re

# ASCII Art to display at the start
ASCII_ART = """8888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888P""  ""988888888888888888888888888888888
888888888888888888888P"88888P          988888"988888888888888888888888
888888888888888888888  "9888            888P"  88888888888888888888888
88888888888888888888888bo "9  d8o  o8b  P" od8888888888888888888888888
88888888888888888888888888bob 98"  "8P dod8888888888888888888888888888
88888888888888888888888888888    db    8888888888888888888888888888888
8888888888888888888888888888888      888888888888888888888888888888888
8888888888888888888888888888P"9bo  odP"9888888888888888888888888888888
8888888888888888888888888P" od88888888bo "9888888888888888888888888888
88888888888888888888888   d88888888888888b   8888888888888888888888888
888888888888888888888888oo8888888888888888oo88888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888"""

def welcome_screen():
    """Displays a welcome screen with ASCII art and some nice formatting."""
    print("\n" + "="*70)
    print(" "*0 + "                  WELCOME TO THE GOOGLE DORKING TOOL")
    print("-"*70)
    print(ASCII_ART)
    print("-"*70)
    print("  This tool lets you create custom google dorking queries with ease!")
    print(" "*0 + "                 Program created by: Benjamin Barish")
    print("="*70)

def validate_site(site_name):
    # Basic validation for a site/domain
    regex = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(regex, site_name) is not None

def validate_file_extension(file_extension):
    # Simple file extension validation (e.g., pdf, docx, jpg)
    valid_extensions = ["pdf", "xls", "docx", "jpg", "png", "txt", "html", "csv"]
    return file_extension.lower() in valid_extensions

def get_input(prompt, valid_choices=None):
    # Function to repeatedly ask the user for input until it's valid
    while True:
        user_input = input(prompt).strip().lower()
        
        if valid_choices:
            if user_input in valid_choices:
                return user_input
            else:
                print(f"Invalid choice. Please choose from {', '.join(valid_choices)}.")
        else:
            if user_input:
                return user_input
            else:
                print("Input cannot be empty. Please try again.")

def build_query():
    welcome_screen()  # Display the welcome screen with ASCII art and description
    
    # Loop to create new queries if desired
    while True:
        # Step 1: What type of search do you want to perform? (sanitize input)
        search_type = get_input("What do you want to search for? (e.g., Files, Webpages, Databases, Vunerabilities):")
        search_type = search_type.strip()  # Sanitize input (remove any extra spaces)

        # Step 2: Specify site or domain
        site = get_input("Do you want to restrict the search to a particular site or domain? (y/n):", valid_choices=['y', 'n'])
        if site == 'y':
            while True:
                site_name = input("Enter the domain or site (e.g., 'example.com'):").strip().lower()
                if validate_site(site_name):
                    query = f"site:{site_name} "
                    break
                else:
                    print("Invalid domain format. Please enter a valid domain (e.g., 'example.com').")
        else:
            query = ""
        
        # Step 3: Choose a file type if relevant
        file_type = get_input("Do you want to search for specific file types? (y/n)", valid_choices=['y', 'n'])
        if file_type == 'y':
            while True:
                file_extension = input("Enter the file type (e.g., 'pdf', 'xls', 'docx'):").strip().lower()
                if validate_file_extension(file_extension):
                    query += f"filetype:{file_extension} "
                    break
                else:
                    print("Invalid file extension. Please enter a valid file type (e.g., 'pdf', 'xls').")
        
        # Step 4: Enter the keywords
        keywords = get_input("Enter the keywords or the content you're looking for (e.g., Username, Password, Administrator):")
        query += keywords
        
        print("Generated Google dorking query:")
        print("\n" + query + "\n")

        # Step 5: Confirmation and Execution
        execute = get_input(f"Would you like to search with the following query? (y/n): {query}\n", valid_choices=['y', 'n'])
        if execute == 'y':
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
            print("Opening your search in the browser...")
        else:
            print("Query not executed.")
        
        # Ask if the user wants to create a new query
        another_query = get_input("Do you want to create another dork query? (y/n):", valid_choices=['y', 'n'])
        if another_query != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    build_query()
