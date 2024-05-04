

# Personal Finance Tracker

Personal Finance Tracker is a Python application that allows users to track their income and expenses. It provides a user-friendly graphical interface built with the Tkinter library.

## Features

- Add new transactions with details like purpose, amount, type (income or expense), and date.
- View all transactions in a tabular format with sorting and searching capabilities.
- Update existing transactions by modifying the amount, type, or date.
- Delete transactions either individually or by purpose.
- Display a summary of total income, total expenses, number of incomes, number of expenses, and net value.
- Read bulk transactions from a file.
- Save and load transactions to/from a JSON file.

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running the following command:

```
pip install tkinter
```

## Usage

1. Navigate to the project directory.
2. Run the following command to start the application:

```
python main.py
```

3. The main menu will be displayed, providing options to add, view, update, delete transactions, display a summary, and read bulk transactions from a file.
4. Follow the on-screen instructions to interact with the application.

## File Structure

- `main.py`: The main Python file that contains the application logic and the `FinanceTrackerGUI` class.
- `transactions.json`: A JSON file used to store and load transactions.
- `README.md`: This file, containing information about the project.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Tkinter library for providing the GUI framework.
- The JSON library for handling JSON data.