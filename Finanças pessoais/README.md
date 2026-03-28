# My Finance Control System

A simple and elegant web application for managing personal finances built with Flask and Python.

**Created by: Juan Fonte**

## Features

✅ **Add Transactions** - Quickly add income or expense transactions  
✅ **Automatic Date** - Transactions are automatically dated  
✅ **Filter by Type** - View all, income only, or expenses only  
✅ **Live Balance** - Real-time balance calculation and display  
✅ **Delete Transactions** - Remove incorrect entries  
✅ **Persistent Storage** - Data saved in JSON format  
✅ **Responsive Design** - Works on desktop, tablet, and mobile  
✅ **Color-coded** - Green for income, red for expenses  

## Project Structure

```
Finanças pessoais/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── data.json          # Transaction data (auto-created)
├── templates/
│   └── index.html     # Main HTML template
└── static/
    └── style.css      # CSS styling
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Flask directly:

```bash
pip install Flask==3.1.3
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Open in Browser

Open your web browser and navigate to:

```
http://localhost:5000
```

## Usage

### Adding a Transaction

1. Select the transaction type:
   - **Income** - Money coming in (salary, bonus, etc.)
   - **Expense** - Money going out (groceries, rent, etc.)

2. Enter the amount (numerical value)

3. Add a description (e.g., "Salary", "Grocery shopping")

4. Select the date (defaults to today)

5. Click "Add Transaction"

### Filtering Transactions

Click the filter buttons at the top:
- **All** - Show all transactions
- **Income** - Show only income transactions
- **Expenses** - Show only expense transactions

### Deleting a Transaction

Click the "Delete" button in the action column for any transaction. Confirm the deletion when prompted.

### Viewing Balance

The balance summary at the top displays:
- **Total Balance** - Net balance (income - expenses)
- **Total Income** - Sum of all income transactions
- **Total Expenses** - Sum of all expense transactions

## Data Storage

All transactions are automatically saved to `data.json` in the same directory as `app.py`. The file is created automatically on first use.

### data.json Format

```json
[
  {
    "id": 1,
    "type": "income",
    "amount": "5000.00",
    "description": "Monthly Salary",
    "date": "2026-03-28"
  },
  {
    "id": 2,
    "type": "expense",
    "amount": "500.00",
    "description": "Grocery Shopping",
    "date": "2026-03-28"
  }
]
```

## API Endpoints

### GET `/`
Home page - displays all transactions with summary

**Query Parameters:**
- `filter` (optional): Filter by type - `all`, `income`, or `expense`

### POST `/add`
Add a new transaction

**Form Parameters:**
- `type` (required): `income` or `expense`
- `amount` (required): Numerical amount greater than 0
- `description` (required): Transaction description
- `date` (optional): Date in YYYY-MM-DD format

### POST `/delete/<transaction_id>`
Delete a transaction by ID

**URL Parameters:**
- `transaction_id` (required): ID of the transaction to delete

### GET `/api/balance`
Get balance information as JSON

**Response:**
```json
{
  "balance": 4500.00,
  "income": 5000.00,
  "expense": 500.00
}
```

## Features Explained

### Real-time Balance Update
The application updates the balance display every 2 seconds using a background API call.

### Automatic Date Assignment
If no date is provided, the current date is automatically assigned to new transactions.

### Input Validation
- Amount must be a positive number
- All required fields must be filled
- Negative amounts are rejected

### ID Management
Transaction IDs are automatically managed and recalculated when transactions are deleted.

## Customization

### Changing Colors

Edit `static/style.css` and modify these CSS variables:
- `--success-color: #27ae60;` (Income - Green)
- `--danger-color: #e74c3c;` (Expense - Red)
- `--primary-color: #3498db;` (Primary - Blue)

### Changing Port

Edit `app.py` line 87:
```python
app.run(debug=True, host='localhost', port=5000)
```

Change `5000` to your desired port number.

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, change it in `app.py`:
```python
app.run(debug=True, host='localhost', port=5001)
```

### data.json Not Being Created
Ensure the application directory has write permissions. The file is created automatically when you add the first transaction.

### Transactions Not Saving
Check that:
1. The `data.json` file exists in the same directory as `app.py`
2. The application has write permissions to the directory
3. The JSON file is not corrupted

## Browser Support

✅ Chrome/Edge (latest)  
✅ Firefox (latest)  
✅ Safari (latest)  
✅ Mobile browsers (iOS Safari, Chrome Mobile)  

## Future Enhancements

- Category tags for transactions
- Recurring transactions
- Monthly/yearly reports
- Search functionality
- Export to CSV
- Data visualization (charts)
- Multi-user support with authentication
- Budget limits and alerts



## Author

Juan Fonte  

---

**Version:** 1.0  
**Last Updated:** March 28, 2026
