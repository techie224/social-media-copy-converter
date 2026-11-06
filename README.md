<h1 align="center">
  <br>
  <img width="200" alt="Logo" src="images/logo_circle_with_border.png"> <!--CHANGE PATH WHEN RENAMING FOLDERS/FILES-->
  <br>
  Social Media Copy Converter
  <br>
</h1>

<h3 align="center">An AI-powered CLI tool that converts social media copy to Instagram, Twitter/X, and LinkedIn formats.</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-v3.14+-555555?labelColor=3776AB&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Claude-Sonnet%204.5-555555?labelColor=D97752&logo=anthropic&logoColor=white" alt="Model">
  <img src="https://img.shields.io/badge/API-Integration-555555?labelColor=2E7D32&logo=mulesoft&logoColor=white" alt="API Integration">
 <img src="https://img.shields.io/badge/Prompt-Engineering-555555?labelColor=D4A017" alt="Prompt Engineering">
</p>

## Demo screenshot
![Demo screenshot](images\demo_screenshot.png)

## Tech Stack

- **Python 3.11** - Core programming language
- **Anthropic Claude API** - AI content generation (Sonnet 4.5)
- **python-dotenv** - Environment variable management
- **VS Code** - Development environment

## Setup

### 1. Install required software
Make sure you have [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) ([version 3.14](https://www.python.org/downloads/latest/python3.14/) or newer) installed on your computer.

### 2. Set up your API key

1. Get your API key from the [Anthropic Console](https://console.anthropic.com)
2. Create a .env file in the project root
3. Fill out your .env file as shown in the [example](.env.example)

### 3. Run the following commands
From your command line
```bash
# Clone this repository
git clone https://github.com/techie224/social-media-copy-converter.git
cd social-media-copy-converter

# Create a virtual environment (recommended)
py -m venv venv
venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# All set! - Run the tool
py main.py
```


## Usage

1. Run the program: `py main.py`
2. Paste your original content when prompted
3. Select which platforms to convert for (Instagram, Twitter, LinkedIn)
4. View the converted content in your terminal
5. Find saved outputs in the `outputs/` folder with timestamps

## What I Learned

- **API Integration**: Working with Anthropic's Claude API, handling authentication and rate limits
- **Error Handling**: Implementing robust exception handling for network and API failures
- **Project Structure**: Organizing code into modular files for maintainability
- **User Experience**: Adding input validation and clear error messages for better UX

## Future Improvements

- Support for more platforms (TikTok, Facebook, Threads)
- Batch processing for multiple posts at once
- Analytics on character counts and optimization suggestions️
- Customizable tone/style preferences