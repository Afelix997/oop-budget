class Budget:
    def __init__(self,label,income=0):
        self.all_expenses=[]
        self.monthly_expenses=0
        self.monthly_income=float(income)
        self.monthly_budget=float(income)
        self.rem_budget=float(income)
        print(f'{label} created!')
        self.intro_expenses()
        return print(f'Your total monthly expenses adds up to ${self.rem_budget} with a remaining balance of ${self.monthly_expenses}')

    def new_expense(self,expense_type,expense_name,expense_amount=0,monthly_expense=False):
        if monthly_expense == True:
            self.all_expenses.append([expense_type,expense_name,expense_amount,])
            self.monthly_budget -= expense_amount
            self.monthly_expenses+= expense_amount
        self.rem_budget-= float(expense_amount)
         
    
    def intro_expenses(self):
        print('Please fill out these questions on your monthly expenses, if any do not apply to you please input 0 .')
        expense=int(input("How much do you spend a month on groceries?\n"))
        self.new_expense('Food','Groceries',expense,True)
        expense=int(input("How much do you spend a month ordering out?\n"))
        self.new_expense('Food','Ordering Out',expense,True)
        expense=int(input(f"How much do you spend a month on any car payments?\n"))
        self.new_expense('Transportation','Car Payment',expense,True)
        expense=int(input(f"How much do you spend a month on gas\n"))
        self.new_expense('Transportation','Gas',expense,True)
        expense=int(input(f"How much do you spend a month on other transportation needs (Insurance, oil changes , car wash, etc)?\n"))
        self.new_expense('Transportation','Trans Misc',expense,True)
        expense=int(input(f"How much do you spend a month on your Phone bill?\n"))
        self.new_expense('Bill','Phone Bill',expense,True)
        expense=int(input(f"How much do you spend a month on your rent/mortgage\n"))
        self.new_expense('Bill','shelter',expense,True)
        expense=int(input(f"How much do you spend a month on utilities (gas, water, electricity, etc?\n"))
        self.new_expense('Bill','Utilities',expense,True)
        expense=int(input(f"How much do you spend a month on streaming services?\n"))
        self.new_expense('Entertainment','Streaming Services',expense,True)
        expense=int(input(f"How much do you spend a month on other forms of entertainment (movies, bowling, etc)?\n"))
        self.new_expense('Entertainment','Entertainment Misc',expense,True)
        expense=int(input(f"How much do you spend a month on retirement/savings?\n"))
        self.new_expense('Bill','Investments',expense,True)
        expense=int(input(f"And lastly how much do you spend a month on any other misc expenses?\n"))
        self.new_expense('Misc','Misc',expense,True)




