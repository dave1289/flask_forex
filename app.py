from flask import Flask, session, request, render_template, flash, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True

debug = DebugToolbarExtension(app)

c = CurrencyRates()
c_sym = CurrencyCodes()

@app.route('/', methods=['GET', 'POST'])
def show_home():
   return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_money():
   start = request.form.get('start').upper()
   end = request.form.get('end').upper()
   amount = request.form.get('amount')
   symbol = c_sym.get_symbol(end)
   # insert input checking logic
   if len(start) != 3 or len(end) != 3 or not amount.isdigit():
      flash('Please check form and retry conversion', 'error')
   else:
      try:
         converted = c.convert(start, end, float(amount))   
         return render_template('results.html', converted=round(converted,2), symbol=symbol)
      except:
         flash('Please check currency codes', 'error')
   return redirect('/')


   


   