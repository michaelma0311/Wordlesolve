#Michael Ma Wordle Solver
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

#Linking the flask function routes to index.html, actual python code starts on line 55
@app.route('/')
def home():
    return render_template('wordlesolve.html')
lis = []
@app.route('/url1', methods=['POST', 'GET'])
def process_form1():
    global lis
    if request.method == 'POST':
        t1 = request.form.get('t1')
        t2 = request.form.get('t2')
        t3 = request.form.get('t3')
        t4 = request.form.get('t4')
        t5 = request.form.get('t5')
        lis += [t1, t2, t3, t4, t5]
        return "<h1>Sucess, please go back to the previous page by hitting the back arrow key to continue</h1>"
    else:
        return 'Invalid request'
@app.route('/url2', methods=['GET', 'POST'])
def process_form2():
    global lis
    if request.method == 'POST':
        o1 = request.form.get('o1')
        o1 = o1.split()
        o2 = request.form.get('o2')
        o2 = o2.split()
        o3 = request.form.get('o3')
        o3 = o3.split()
        o4 = request.form.get('o4')
        o4 = o4.split()
        o5 = request.form.get('o5')
        o5 = o5.split()
        lis += [o1, o2, o3, o4, o5]
        return "<h1>Success, please go back to the previous page by hitting the back arrow key to continue</h1>"
        
    else:
        return 'Invalid request'

@app.route('/url3', methods=['GET', 'POST'])
def process_form3():
    global lis
    if request.method == 'POST':
        gr1 = request.form.get('gr1')
        gr1 = gr1.split()
        lis += [gr1]
        return "<h1>Sucess, please go back to the previous page by hitting the back arrow key to continue</h1>"
    else:
        return 'Invalid request'
@app.route('/run', methods=['GET', 'POST'])

def run(): #Actual python code starts here
    try:
        global lis
        fin = open('wordlelist.txt', 'r')

        d = fin.read().split()

        t1 = lis[0]
        t2 = lis[1]
        t3 = lis[2]
        t4 = lis[3]
        t5 = lis[4]
        greens = [t1, t2, t3, t4, t5]
        z1 = lis[5]
        z2 = lis[6]
        z3 = lis[7]
        z4 = lis[8]
        z5 = lis[9]
        lett = [t1, t2, t3, t4, t5]
        lett += z1
        lett += z2
        lett += z3
        lett += z4
        lett += z5
        org = [z1, z2, z3, z4, z5]
        gray = []
        words = lis[10]
        for word in words:
            for j in word:
                if j not in lett:
                    gray += [j]
        ins = []
        for i in range(len(greens)):
            if greens[i] != '':
                ins += [i]
        gray = list(set(gray))
        ans = []
        for i in d:
            cur = list(map(str, i))
            able = True
            for j in range(5):
                if (greens[j]):
                    if (cur[j] != greens[j]):
                        able = False
                        break
            if (able == False):
                continue
            temp = []
            for k in range(len(cur)):
                if k not in ins:
                    temp += [cur[k]]
                else:
                    temp += ['']
            for j in range(len(org)):
                for k in range(len(org[j])):
                    if able == False:
                        break
                    if org[j][k] == '':
                        continue
                    if org[j][k] in greens:
                        if (temp.count(org[j][k]) != 0):
                            if temp.index(org[j][k]) != j and cur.index(j) != greens.index(j):
                                pass
                        else:
                            able = False
                    else:
                        if temp.count(org[j][k]) == 0 or temp.index(org[j][k]) == j:
                            able = False
            if able == False:
                continue
            for j in gray:
                if cur.count(j) > 0:
                    able = False
            if able == False:
                continue
            ans += [i]
        words_per_line = 12  

        result = "<h1>These are the words that are possible:"
        for i, word in enumerate(ans):
            result += f"<h3>{word}</h3>"
            if (i + 1) % words_per_line == 0:
                result += "<br>"

        return result
    except:
        afa = "You have entered something incorrectly or left blank spaces in the third submit box please try again"
        return f"<h1>{afa}</h1>"

@app.route('/reset', methods=['POST'])
def reset_form():
    global lis
    lis = [] 
    return '<h1>Form reset successful, please go back to the previous page'
if __name__ == '__main__':
    app.run(debug = False)



