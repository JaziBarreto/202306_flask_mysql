from flask import Flask, render_template, request, redirect
# importar la clase de friend.py
from friends import Friend

app = Flask(__name__)

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
# Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Friend.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)