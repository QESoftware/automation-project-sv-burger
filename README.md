SV Burger Automation — Fast Food Reservation Page

This project contains a set of automated tests using Selenium and Pytest to validate key functionalities in the SV Burger web application, a fast food reservation page. The tests cover main flows for authentication, user registration, and data validation.

🚀 Technologies Used

 Python 3.10+

Selenium WebDriver

Pytest

WebDriver Manager

ActionChains

Pytest Fixtures

Git

📁 Project Structure 📦 svburger-automation/

├── tests/

│   ├── test_authentication.py

│   ├── test_signup.py

│   └── conftest.py

├── utils/

│   └── helpers.py (optional)

├── requirements.txt

└── README.md

💡 The current code might be all in a single file (test_e2e.py) while you organize it.

✅ Included Test Cases

🔐 Authentication (Sign In)

Sign in without entering email

Sign in with incorrect password

👤 User Registration (Sign Up)

Registration with only required fields

Registration with valid names/lengths

Registration with first or last name at boundary values (6 and 10 characters)

Registration with invalid password (less than 6 characters)

🧪 Validations (Boundary & Error Handling)

Alert validation on failure

Verification of successful redirect after registration

⚙️ Installation

Clone this repository:

git clone (https://github.com/QESoftware/automation-project-sv-burger/tree/master)

📦 Dependencies

Install the required dependencies:

pip install pytest-html

python -m pip install --upgrade pip

pytest --html=report.html

Required packages:

selenium

pytest

webdriver-manager

You can automatically generate a requirements.txt file using:

pip freeze > requirements.txt

▶️ Running the Tests

pytest test_e2e.py --headed

If you're using PyCharm:

Right-click the test file and select "Run with pytest"

✍️ Author

Sara Laniado — QA Automation Engineer

📧 slaniado2018@gmail.com










