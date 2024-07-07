from flask import Flask, request, render_template

app = Flask(__name__)

# Define your Python function here
"""def process_inputs(lis):
    # Do something with the input values
    # Call your Python function here
    t1 = lis[0]
    t2 = lis[1]
    t3 = lis[2]
    t4 = lis[3]
    t5 = lis[5]
    o1 = lis[6]
    o2 = lis[7]
    o3 = lis[8]
    o4 = lis[9]
    o5 = lis[10]
    gr1 = lis[11]
    #result = my_function(t1, t2, t3, t4, t5, o1, o2, o3, o4, o5, gr1)
    return "Done"
"""
@app.route('/')
def home():
    return render_template('wordlesolve.html')
lis = []
@app.route('/url1', methods=['POST', 'GET'])
def process_form1():
    if request.method == 'POST':
        t1 = request.form.get('t1')
        t2 = request.form.get('t2')
        t3 = request.form.get('t3')
        t4 = request.form.get('t4')
        t5 = request.form.get('t5')
        lis += [t1, t2, t3, t4, t5]
        return f"<h1>{t1}<h1>"
    else:
        return 'Invalid request'
"""@app.route('/url2', methods=['GET', 'POST'])
def process_form2(lis):
    if request.method == 'POST':
        o1 = request.form.get('o1')
        o2 = request.form.get('o2')
        o3 = request.form.get('o3')
        o4 = request.form.get('o4')
        o5 = request.form.get('o5')
        lis += [o1, o2, o3, o4, o5]
        return
        
    else:
        return 'Invalid request'

@app.route('/url3', methods=['GET', 'POST'])
def process_form3(lis):
    if request.method == 'POST':
        gr1 = request.form.get('gr1')
        gr1 = gr1.split()
        lis += [gr1]

    else:
        return 'Invalid request'
def run():
    result = process_inputs(lis)
    return render_template('output.html', result=result)
"""
if __name__ == '__main__':
    app.run()



