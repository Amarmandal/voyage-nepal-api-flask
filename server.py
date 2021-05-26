from flask import Flask, request
import flask
app = Flask(__name__)

@app.route('/')
def index():
  return flask.jsonify({ "success": "This is a success Message"})
  
@app.route('/recommends', methods=['POST'])
def say_hello():
  if request.method == 'POST':
      user_data = request.get_json();

      place_name = user_data['placename']
      user_age = user_data['age']
      user_coordinates_x = user_data['x']
      user_coordinates_y = user_data['y']

      return flask.jsonify({ "userData":  {
         "NearYou": [],
         "special_recommendation": []
      }})

if __name__ == '__main__':
    app.run(host="localhost", port=8181, debug=True)