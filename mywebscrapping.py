import requests
from bs4 import BeautifulSoup
from flask import Flask, request, redirect, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    link_url = ""  # Declare link_url here

    if request.method == 'POST':
        link_url = request.form['link_url']
#----------------------------------------------------------------------------------------------------------------------------#
        #KhushiKaran13579 code start

        try:
            response = requests.get(link_url)
            if response.status_code == 200:
                htmlContent = response.text
                soup = BeautifulSoup(htmlContent, 'html.parser')
                title = soup.title
                paras = soup.find_all('p')
                all_links = set()
                for link in soup.find_all('a'):
                    if link.get('href') != '#':
                        link_text = link.get('href')
                        all_links.add(link_text)

                navbar_content = soup.find(id='nav-content')
                elem = soup.select('.modal-footer')
                
                #KhushiKaran13579 code ended
#---------------------------------------------------------------------------------------------------------------------
                
                return render_template('index.html', title=title, paras=paras, all_links=all_links, navbar_content=navbar_content, elem=elem)
            else:
                return f"Failed to fetch the URL. Status code: {response.status_code}"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('index.html', link_url=link_url)  # Pass link_url to the template

if __name__ == '__main__':
    app.run(debug=True)
    




