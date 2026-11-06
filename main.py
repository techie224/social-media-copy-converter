import utils
import platforms
import repurposer
import file_handler

def main():
    
    print("Welcome to Content Repurposer!")

    # Get user input
    original_post = utils.get_og_post()
    selected_platforms = platforms.select_platforms()
    
    # Make API call
    repurposed_content = repurposer.repurpose_content(original_post, selected_platforms)
    
    # Print and save
    utils.print_content(repurposed_content)
    file_handler.save_content(original_post, repurposed_content)
    
if __name__ == "__main__":
    main()