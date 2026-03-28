# Personal Finance Control System
# Author: Juan Fonte
# Description: Simple web app to manage personal finances

from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
DEBUG_MODE = True
DATA_FILE = 'data.json'

def load_transactions():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_transactions(transactions):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(transactions, f, indent=2, ensure_ascii=False)

def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction['type'] == 'income':
            balance += float(transaction['amount'])
        else:
            balance -= float(transaction['amount'])
    return balance

def get_filtered_transactions(transactions, filter_type=None):
    if filter_type and filter_type != 'all':
        return [t for t in transactions if t['type'] == filter_type]
    return transactions

@app.route('/')
def index():
    transactions = load_transactions()
    filter_type = request.args.get('filter', 'all')
    filtered_transactions = get_filtered_transactions(transactions, filter_type)
    balance = calculate_balance(transactions)
    
    income_total = sum(float(t['amount']) for t in transactions if t['type'] == 'income')
    expense_total = sum(float(t['amount']) for t in transactions if t['type'] == 'expense')
    
    return render_template(
        'index.html',
        transactions=filtered_transactions,
        balance=balance,
        income_total=income_total,
        expense_total=expense_total,
        current_filter=filter_type,
        now=datetime.now()
    )

@app.route('/add', methods=['POST'])
def add_transaction():
    try:
        transaction_type = request.form.get('type')
        amount = request.form.get('amount')
        description = request.form.get('description')
        date = request.form.get('date', datetime.now().strftime('%Y-%m-%d'))
        
        if not all([transaction_type, amount, description]):
            return redirect(url_for('index'))
        
        # Validate input
        try:
            amount = float(amount)
            if amount <= 0:
                return redirect(url_for('index'))
        except ValueError:
            return redirect(url_for('index'))
        
        transactions = load_transactions()
        
        new_transaction = {
            'id': len(transactions) + 1,
            'type': transaction_type,
            'amount': str(amount),
            'description': description,
            'date': date
        }
        
        transactions.append(new_transaction)
        save_transactions(transactions)
        
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error adding transaction: {e}")
        return redirect(url_for('index'))

@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    try:
        transactions = load_transactions()
        transactions = [t for t in transactions if t['id'] != transaction_id]
        
        for i, t in enumerate(transactions, 1):
            t['id'] = i
        save_transactions(transactions)
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error deleting transaction: {e}")
        return redirect(url_for('index'))

@app.route('/api/balance')
def api_balance():
    transactions = load_transactions()
    balance = calculate_balance(transactions)
    income_total = sum(float(t['amount']) for t in transactions if t['type'] == 'income')
    expense_total = sum(float(t['amount']) for t in transactions if t['type'] == 'expense')
    
    return jsonify({
        'balance': round(balance, 2),
        'income': round(income_total, 2),
        'expense': round(expense_total, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
DEBUG_MODE