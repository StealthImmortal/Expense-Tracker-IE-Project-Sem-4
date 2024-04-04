**Transaction Logging:** Users can add transactions by providing details such as amount, category, type (income or expense), date, and optional comment. These transactions are stored in an SQLite database table named 'transactions'.

**View Transactions:** Users can view all transactions recorded in the database. This feature allows users to have a comprehensive overview of their financial activities.

**View Balance:** This feature calculates and displays the user's income, expenses, and current balance. It retrieves the sums of amounts for income and expenses separately and then calculates the balance by subtracting expenses from income.

**Categorize Transactions:** Users can view transactions categorized under specific categories like Food, Travel, Fuel, Shopping, and Bills & Misc. This feature helps users to analyze their spending patterns for different expense categories.

**User Interface via Command Line Interface (CLI):** The main function provides a simple CLI interface for users to interact with the budget tracker. Users can select options to perform tasks like adding transactions, viewing transactions, checking balance, categorizing transactions, and exiting the application. The interface guides the user through the available functionalities and prompts for necessary inputs.
