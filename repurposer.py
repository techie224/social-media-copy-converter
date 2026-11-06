import os
import platforms
from anthropic import Anthropic, APIError, APIConnectionError, RateLimitError, AuthenticationError
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)

def repurpose_content(original_post, selected_platforms): # Returns repurposed content as a dictionary {"platform":repurposed_content}
    
    repurposed_content = {}
    
    # Go through all the selected platforms
    for platform in selected_platforms:
        
        # Get current platform's prompt
        try:
            print(f"\nConverting to {platform.capitalize()}...")
            prompt_template = platforms.platform_prompts[platform.lower()]
        except Exception as e:
            raise Exception(f"Something went wrong. Please check your platforms.py file. Exception: {e}")
        
        # Call Anthropic's API and with the completed prompt
        try:
            message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt_template.format(original_post=original_post)}]
            )
            message_text = message.content[0].text

            repurposed_content[platform] = message_text
            
    
        except AuthenticationError:
            raise Exception("Invalid API key. Please check your .env file.")

        except RateLimitError:
            raise Exception("Rate limit reached. Please wait a few minutes and try again.")

        except APIConnectionError:
            raise Exception("Cannot connect to the API. Check your internet connection.")

        except APIError as e:
            raise Exception(f"API error occurred: {str(e)}")

        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")
    
    return repurposed_content