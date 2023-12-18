from flask import Flask, render_template, request, jsonify
import gemini as g

model=g.model()
chat=model.start_chat(history=[])
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/fromuser', methods=['post'])
def gettextfromuser():    
    prompt = request.json['usertext']
    response = chat.send_message(prompt)
    res = response.text
    return(jsonify(res))

if __name__ == '__main__':
    app.run(debug=True)
