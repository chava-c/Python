from flask import Flask
import os,requests

app = Flask(__name__)
  
@app.route('/', methods =['GET'])
def home():
    construct_url = "https://api.openweathermap.org/data/2.5/weather?q=Guadalajara&appid=a19913b0ea32583092ca45f0af7e0e1e&units=metric"
    response = requests.get(construct_url)

    list_of_data = response.json()
    
    html_data = f"""
    <table border="1">
    <tr>
        <td>City</td>
        <td>Country</td>
        <td>Temp</td>
        <td>Pressure</td>
        <td>Humidity</td>
    </tr>
    <tr>
        <td>Guadalajara</td>
        <td>{str(list_of_data['sys']['country'])}</td>
        <td>{str(list_of_data['main']['temp']) + '°C'}</td>
        <td>{str(list_of_data['main']['pressure'])}</td>
        <td>{str(list_of_data['main']['humidity'])}</td>
    </tr>

</table>
    """
    return html_data

if __name__ == "__main__":
    app.run(port = 8000,debug=True)
