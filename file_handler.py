import os
from datetime import datetime
from utils import format_error_message

def save_content(original_post, repurposed_content):
    
    timestamp = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    folder = f"outputs/{timestamp}"
    os.makedirs(folder)

    with open(f"{folder}/input.txt", "w", encoding="UTF-8") as file:
        file.write(original_post)

    for platform, content in repurposed_content.items():
        try:
            filename = f"{folder}/{platform.lower()}.txt"
            with open(filename, "w", encoding="UTF-8") as file:
                file.write(content)
            print(f"✅ Post saved to: {filename}")
        except Exception as e:
            format_error_message(f"Failed to save {platform.upper()} content. Exception: {e}")