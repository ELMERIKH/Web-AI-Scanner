from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_website', methods=['POST'])
def test_website():
    website_url = request.form['website_url']

    # Call your tool with the website URL
    # Replace the following line with your actual tool code
    tool_output = my_tool_function(website_url)

    return render_template('result.html', tool_output=tool_output)

def my_tool_function(website_url):
    # Replace this function with your actual tool code
    # For now, just returning a dummy output
    return f"Testing website: {website_url}. Tool output: This is a dummy output."

if __name__ == '__main__':
    app.run(debug=True)
