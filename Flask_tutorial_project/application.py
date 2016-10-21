from flask import Flask, render_template, request, redirect

app_bismayan = Flask(__name__)

app_bismayan.vars = {}
app_bismayan.questions = {}
app_bismayan.questions['How many eyes do you have?'] = ('1', '2', '3')
app_bismayan.questions['Which fruit do you like best?'] = ('banana', 'mango', 'pineapple')
app_bismayan.questions['Do you like cupcakes?'] = ('yes', 'no', 'maybe')
app_bismayan.nquestions = len(app_bismayan.questions)


@app_bismayan.route('/index_bismayan', methods=['GET', 'POST'])
def index_bismayan():
    num_questions = app_bismayan.nquestions
    if request.method == 'GET':
        return render_template('userinfo_bismayan.html', num=num_questions)
    else:
        # return 'request was a POST'
        app_bismayan.vars['name'] = request.form['name_bismayan']
        app_bismayan.vars['age'] = request.form['age_bismayan']
        with open('{0}_{1}.txt'.format(app_bismayan.vars['name'], app_bismayan.vars['age']), 'w') as f:
            f.write('Name: {} \n'.format(app_bismayan.vars['name']))
            f.write('Age: {} \n'.format(app_bismayan.vars['age']))
        return redirect('/main_bismayan')


@app_bismayan.route('/main_bismayan')
def main_bismayan2():
    if len(app_bismayan.questions) == 0:
        return render_template('end_bismayan.html')
    else:
        return redirect('/next_bismayan')


@app_bismayan.route('/next_bismayan', methods=['GET'])
def next_bismayan():  # remember the function name does not need to match the URL
    # for clarity (temp variables)
    n = app_bismayan.nquestions - len(app_bismayan.questions) + 1
    q = app_bismayan.questions.keys()[0]  # python indexes at 0
    a1, a2, a3 = app_bismayan.questions.values()[0]  # this will return the answers corresponding to q

    # save the current question key
    app_bismayan.currentq = q
    return render_template('layout_bismayan.html', num=n, question=q, ans1=a1, ans2=a2, ans3=a3)


@app_bismayan.route('/next_bismayan', methods=['POST'])
def next_bismayan2():
    # can't have two functions with the same name
    # Here, we will collect data from the user.
    # Then, we return to the main function, so it can tell us whether to
    # display another question page, or to show the end page.

    f = open('%s_%s.txt' % (app_bismayan.vars['name'], app_bismayan.vars['age']), 'a')  # a is for append
    f.write('%s\n' % (app_bismayan.currentq))
    f.write('%s\n\n' % (request.form['answer_from_layout_bismayan']))  # this was the 'name' on layout.html!
    f.close()

    # Remove question from dictionary
    del app_bismayan.questions[app_bismayan.currentq]

    return redirect('/main_bismayan')


if __name__ == '__main__':
    app_bismayan.run(debug=True)
