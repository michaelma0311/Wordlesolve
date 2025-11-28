#Michael Ma Wordle Solver
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

#Linking the flask function routes to index.html, actual python code starts on line 55
@app.route('/')
def home():
    return render_template('wordlesolve.html')

def _clean_letter(value):
    return (value or '').strip().lower()[:1]

def _letter_bucket(value):
    bucket = []
    for ch in (value or '').lower():
        if ch.isalpha():
            bucket.append(ch)
    return bucket

def _parse_guesses(value):
    return [(word.strip().lower()) for word in (value or '').split() if word.strip()]

@app.route('/run', methods=['GET', 'POST'])
def run(): #Actual python code starts here
    try:
        fin = open('wordlelist.txt', 'r')

        d = fin.read().split()
        greens = [_clean_letter(request.form.get(f't{i}')) for i in range(1, 6)]
        oranges = [_letter_bucket(request.form.get(f'o{i}')) for i in range(1, 6)]
        words = _parse_guesses(request.form.get('gr1'))
        lett = [g for g in greens if g]
        for bucket in oranges:
            lett += bucket
        org = oranges
        gray = []
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
            print(i)
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
            #print(temp, cur, greens, org)
            for j in range(len(org)):
                for k in range(len(org[j])):
                    if able == False:
                        break
                    if org[j][k] == '':
                        continue
                    if org[j][k] in greens:
                        """if (temp.count(org[j][k]) != 0):
                            if temp.index(org[j][k]) != j and temp.index(org[j][k]) != greens.index(org[j][k]):
                                pass
                        else:
                            able = False"""
                        continue
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
        #print("HELLO")
        words_per_line = 12  
        result = "<h1>These are the words that are possible:"
        for i, word in enumerate(ans):
            result += f"<h3>{word}</h3>"
            if (i + 1) % words_per_line == 0:
                result += "<br>"

        return result
    except Exception as exc:
        print(exc)
        afa = "Something went wrong. Please double-check your clues and try again."
        return f"<h1>{afa}</h1>"

@app.route('/reset', methods=['POST'])
def reset_form():
    return '<h1>Form reset successful. Start a new submission whenever you like.</h1>'
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


