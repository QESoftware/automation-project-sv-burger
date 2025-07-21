
# SV Burger Automation — Fast Food Reservation Page 🧪🍔

This project contains a suite of automated tests using **Selenium** and **Pytest** to validate key functionalities of the **SV Burger** web application, a fast food reservation system. The tests cover core flows such as authentication, user registration, and input validation.

---

## 🚀 Technologies Used

- Python 3.10+
- Selenium WebDriver
- Pytest
- WebDriver Manager
- ActionChains
- Pytest Fixtures
- Git

---

## 📁 Project Structure

```bash
svburger-automation/
├── tests/
│   ├── test_authentication.py
│   ├── test_signup.py
│   └── conftest.py
├── utils/
│   └── helpers.py (optional)
├── requirements.txt
└── README.md
```

💡 *Note: All test cases may currently reside in a single file (`test_e2e.py`) while you organize the structure.*

---

## ✅ Included Test Cases

### 🔐 Authentication (Sign In)

- Attempt to sign in without entering an email
- Sign in with an incorrect password

### 👤 User Registration (Sign Up)

- Sign up using only required fields
- Sign up with valid first/last names
- Sign up with boundary values for name fields (6 and 10 characters)
- Attempt to sign up with an invalid password (less than 6 characters)

### 🧪 Validations (Boundary & Error Handling)

- Alert handling on failed actions
- Verification of successful redirect after registration

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/QESoftware/automation-project-sv-burger.git
cd automation-project-sv-burger
```

---

## 📦 Dependencies

Install the required dependencies:

```bash
pip install pytest-html
python -m pip install --upgrade pip
```

Run tests with:

```bash
pytest --html=report.html
```

### Required packages:

- selenium
- pytest
- webdriver-manager

You can generate the `requirements.txt` file with:

```bash
pip freeze > requirements.txt
```

---

## ▶️ Running the Tests

To run the tests:

```bash
pytest test_e2e.py --headed
```

If you're using **PyCharm**:

- Right-click the test file and choose **"Run with pytest"**
- Make sure `pytest` is installed in your Python interpreter

---

## ✍️ Author

**Sara Laniado** — QA Automation Engineer  
📧 slaniado2018@gmail.com
