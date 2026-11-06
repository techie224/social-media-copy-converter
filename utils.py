import os

def get_og_post(): # Returns text to be converted
    
    print("How would you like to input your content?")
    print("\t[1] Paste directly")
    print("\t[2] Provide a .txt file path")
    
    choice = input("\nEnter 1 or 2: ").strip()
    
    if choice == "1":
        while True:
        
            original_post = input("Paste the content you would like to convert below (as one line):\n\n")

            if valid_input(original_post): return original_post
                
            
    elif choice == "2":
        while True:
            path = input("Provide the path to your .txt file:\n\n").strip().strip('"')

            if not path.endswith(".txt"):
                format_error_message("Incorrect format. Please make sure your file is a .txt.")

            elif not os.path.exists(path):
                format_error_message("File not found. Please make sure the path you provided is correct.")

            else:
                try:
                    with open(path, "r", encoding="UTF-8") as file:
                        original_post = file.read()

                    if valid_input(original_post): return original_post
                    
                except Exception as e:
                    format_error_message(f"Could not read file: {e}")


    else:
        format_error_message("Invalid choice. Please enter 1 or 2.")
        return get_og_post()
    
        
def print_content(repurposed_content):
    
    for platform, content in repurposed_content.items():
        print("\n" + "="*60)
        print(f"{platform.upper()} VERSION")
        print("="*60 + "\n")
        print(content + "\n")
        
def valid_input(input):
    
    if not input.strip() or len(input) < 10:
        format_error_message("No viable input given. Please try again.")
        return False
    elif len(input) > 5000:
        format_error_message("Input too long. Please keep it under 5000 characters.")
        return False
    else:
        return True

def format_error_message(error_message):
    
    print("\n" + "="*60 + "\n")
    print("ERROR: " + error_message)
    print("\n" + "="*60 + "\n")