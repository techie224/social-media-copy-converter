from utils import format_error_message

def select_platforms(): # Returns selected platforms based on user input
    
    selected_platforms = []
    print()
    # Go through all platforms and add selected ones into a list
    for platform in platforms:
        if input(f"Would you like to convert it for {platform.upper()}? (type 'x' for yes, hit enter for no) ") == "x":
            selected_platforms.append(platform)
        
    # Run again if no platforms were selected
    while not selected_platforms:
        format_error_message("No platforms selected. Please try again.")
        return select_platforms()
    
    return selected_platforms

platform_prompts = {
  
  "instagram": '''
You are a social media expert. Your task is to convert the given content into a single Instagram post.

Requirements:
- Keep the style, tone, and personality of the original content so it sounds like the same person wrote it, but adjust the expression to fit platform conventions.
- Preserve the exact message and intention of the original post (whether it's lead generation, branding, education, or storytelling).
- Structure the post in Instagram’s native style:
  • Start with a strong hook in the first 1–2 lines.
  • Use short paragraphs for readability, do not use line breaks after every sentence!
  • Optionally include emojis that fit naturally with the style and audience (do not overuse).
  • End with a clear call-to-action relevant to the post (e.g. “Save this for later 🔖” / “Share this with a friend” / “What do you think? 👇”).
- Keep it within Instagram caption length (max 2,200 characters, ideally under 500 for engagement).
- Add 5–10 relevant hashtags at the end that match the topic and audience.
- Output ONLY the Instagram text, nothing else (no alternatives, no explanations).
- **Output plain text only - no markdown formatting (no **, no ##, no ---, no bullets with *).**
- The output should be ready to copy-paste directly into Instagram.

Content:
{original_post}
''',

"twitter": '''
You are a social media expert. Your task is to convert the given content into a single Twitter/X post.

Requirements:
- Keep the style, tone, and personality of the original content so it sounds like the same person wrote it, but adjust the expression to fit platform conventions.
- Preserve the core message and intention of the original post.
- Format as ONE single tweet:
  • Keep it under 280 characters (strict limit).
  • Start with a strong hook or bold statement.
  • Use clear, conversational language.
  • Optionally use 1–2 relevant emojis if natural.
  • Make it punchy and engaging.
- Hashtags: 0–2 max, only if they naturally fit.
- Output ONLY the tweet text, nothing else (no alternatives, no explanations).
- **Output plain text only - no markdown formatting (no **, no ##, no ---, no bullets with *).**
- The output should be ready to copy-paste directly into Twitter/X.

Content:
{original_post}
''',

"linkedin": '''
You are a social media expert. Your task is to convert the given content into a single LinkedIn post.

Requirements:
- Keep the style, tone, and personality of the original content so it sounds like the same person wrote it, but adjust the expression to fit platform conventions.
- Preserve the exact message and intention of the original post (whether it's lead generation, branding, education, or storytelling).
- Format the content for LinkedIn’s native style:
  • Start with a bold statement or thought-provoking question.
  • Use short paragraphs with whitespace for readability (1–3 sentences per paragraph).
  • Add bullet points or numbered lists if explaining steps or lessons.
  • End with a reflective or engaging call-to-action (e.g., “What’s your take?” / “Have you experienced this?”).
- Keep it under 1,200 characters for readability (max 3,000).
- Do not overuse emojis (1–2 max, only if they naturally fit a professional tone).
- Hashtags: add 3–5 industry-relevant hashtags at the end.
- Output ONLY the LinkedIn text, nothing else (no alternatives, no explanations).
- **Output plain text only - no markdown formatting (no **, no ##, no ---, no bullets with *).**
- The output should be ready to copy-paste directly into LinkedIn.

Content:
{original_post}
'''
}

platforms = list(platform_prompts.keys())