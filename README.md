# Web Scraping and File Download Flask Application

This Flask application allows you to enter a URL, fetch its HTML content, parse it using BeautifulSoup, and then download the HTML content as a file. Additionally, it extracts specific information from the HTML, such as the page title, paragraphs, and links.
## Images

## Layout
 ![Screenshot (22)](https://github.com/Sarvesh223/web_scrapper/assets/92908500/c5470907-e60f-460c-90a9-e2ef741cf88e)
## Scrape Data
 ![Screenshot (23)](https://github.com/Sarvesh223/web_scrapper/assets/92908500/c1b2fe3b-32ac-4faf-a6fa-92f67ac9220f)
 ![Screenshot (24)](https://github.com/Sarvesh223/web_scrapper/assets/92908500/1fe1933c-1fd4-4f3b-ae7e-3ab853615a4d)

## Prerequisites
Before running the application, make sure you have the following prerequisites installed:
- Python 3.x
- Flask
- Requests
- BeautifulSoup
You can install the required Python packages using `pip`:
``bash
pip install flask requests beautifulsoup4


# Usage
## Clone this repository to your local machine:
 git clone https://github.com/Sarvesh223/web_scrapper.git

## Navigate to the project directory:
 cd your-repo
## Run the Flask application:
 python app.py

Open your web browser and go to http://localhost:5000/ to access the application.
# How it Works
- The application provides a web interface where you can enter a URL.
- After entering the URL and submitting the form, the application does the following:
- It sends an HTTP GET request to the provided URL using the requests library.
- If the request is successful (status code 200), it parses the HTML content of the page using BeautifulSoup.
- It extracts the page title, paragraphs (<p> tags), and links (<a> tags) from the HTML content.
- The downloaded HTML content is saved to a file in the downloads folder.
- The user is provided with a download link to fetch the saved HTML file.
- If there is an error in the process (e.g., failed request or parsing error), an error message is displayed.

# Project Structure
- app.py: The main Flask application.
- templates/index.html: HTML template for the web interface.

# License
This project is licensed under the MIT License. Feel free to use and modify it for your own purposes.

# Acknowledgments
- This project was inspired by the need to easily fetch  HTML content from a URL.
- Special thanks to the Flask, Requests, and BeautifulSoup communities for their excellent libraries.
vbnet









