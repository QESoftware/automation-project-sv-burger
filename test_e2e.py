import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.core import driver


@pytest.fixture()
def setup():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()
   driver.implicitly_wait(10)
   yield driver
   driver.quit()

#Sanity for Sign in
def test_Sanity_Sign_In(setup):
   driver = setup
   wait=  WebDriverWait(driver, 5)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign in" button
   driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

   # Step 2: Enter email and password to sign in
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
   driver.find_element(By.XPATH, "//button[@type='submit']").click()
   assert driver.find_element(By.ID, "mainHeader").is_displayed()

   # Step 3: Select a product
   time.sleep(2)
   select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
   actions.move_to_element(select_product).perform()
   wait.until(EC.element_to_be_clickable(select_product)).click()

   # Step 4:Validate and click the "Reserve" button
   time.sleep(2)
   reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
   ActionChains(driver).move_to_element(reserve_button).click().perform()
   time.sleep(2)
   assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

   time.sleep(2)
   # Step 5: Click the "send" button
   send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
   ActionChains(driver).move_to_element(send_button).click().perform()

   time.sleep(2)
   # Step 6: Validate that "SVBurger Summary" is displayed
   assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()


# List of randomly users for parameterization
random_users_list =[
    ["luzzppazz@gmail.com", "luz123@"],
    ["yyennifergoomezz@gmail.com","yennifer456#"],
    ]

@pytest.mark.parametrize("random_names", random_users_list)
#Sanity for Sign Up
def test_Sanity_Sign_Up(setup, random_names):
   driver = setup
   wait = WebDriverWait(driver, 20)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign up" button
   driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

   # Step 2: Fill out the registration form
   driver.find_element(By.XPATH, "//input[@placeholder='Type your first name']").send_keys("luz")
   driver.find_element(By.XPATH, "//input[@placeholder='Type your last name']").send_keys("paz")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys(random_names[0])
   driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys(random_names[1])
   driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(random_names[1])
   driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
   assert driver.find_element(By.ID, "mainHeader").is_displayed()

# Step 3: Select a product
   time.sleep(2)
   select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
   actions.move_to_element(select_product).perform()
   wait.until(EC.element_to_be_clickable(select_product)).click()

   # Step 4:Validate and click the "Reserve" button
   time.sleep(2)
   reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
   ActionChains(driver).move_to_element(reserve_button).click().perform()
   time.sleep(2)
   assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

   time.sleep(2)
   # Step 5: Click the "send" button
   send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
   ActionChains(driver).move_to_element(send_button).click().perform()

   time.sleep(2)
   # Step 6: Validate that "SVBurger Summary" is displayed
   assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()



#Sanity for Reservation and Confirm Reservation
def test_Confirm_and_Reservation_Product(setup):
   driver = setup
   wait = WebDriverWait(driver, 20)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign in" button
   driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

   # Step 2: Enter email and password to sign in
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
   driver.find_element(By.XPATH, "//button[@type='submit']").click()
   assert driver.find_element(By.ID, "mainHeader").is_displayed()

   # Step 3: Select a product
   time.sleep(2)
   select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
   actions.move_to_element(select_product).perform()
   wait.until(EC.element_to_be_clickable(select_product)).click()

   # Step 4:Validate and click the "Reserve" button
   time.sleep(2)
   reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
   ActionChains(driver).move_to_element(reserve_button).click().perform()
   time.sleep(2)
   assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

   time.sleep(2)
   # Step 5: Click the "send" button
   send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
   ActionChains(driver).move_to_element(send_button).click().perform()

   time.sleep(2)
   # Step 6: Validate that "SVBurger Summary" is displayed
   assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()



#Suite 1: SIGN IN (FUNCTIONALITY)
# List of gmail users for parameterization
gmail_users_list =[
    ["amparopaz@gmail.com", "ampa123@"],
    ["mariaguerrero@gmail.com","maria456#"],
    ["juanrestrepo@gmail.com","juan567&"]
    ]

@pytest.mark.parametrize("gmail_names", gmail_users_list)
def test_login_via_gmail(setup, gmail_names):
    """
    Test the login functionality with gmail credentials.
     Verifies that after logging in, the user can select a product and reserve it.
    """
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter email and password to sign in
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys(gmail_names[0])
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(gmail_names[1])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.ID, "mainHeader").is_displayed()

    # Step 3: Select a product
    time.sleep(2)
    select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

    # Step 4:Validate and click the "Reserve" button
    time.sleep(2)
    reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
    ActionChains(driver).move_to_element(reserve_button).click().perform()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

    time.sleep(2)
    # Step 5: Click the "send" button
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
    ActionChains(driver).move_to_element(send_button).click().perform()

    time.sleep(2)
    # Step 6: Validate that "SVBurger Summary" is displayed
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()


#Suite 1: SIGN IN (FUNCTIONALITY)
# List of yahoo users for parameterization
yahoo_users_list =[
    ["fernandogarcia@yahoo.com", "fer123@"],
    ["elicohen@yahoo.com","eli123$"],
    ["markmarmur@yahoo.com","mark909!"]
]
@pytest.mark.parametrize("yahoo_names", yahoo_users_list)
def test_login_via_yahoo_mail(setup, yahoo_names):
    """
    Test the login functionality with yahoo mail credentials.
    Verifies that after logging in, the user can select a product and reserve it.
    """
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter email and password to sign in
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys(yahoo_names[0])
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(yahoo_names[1])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.ID, "mainHeader").is_displayed()

    # Step 3: Select a product
    time.sleep(2)
    select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

    # Step 4:Validate and click the "Reserve" button
    time.sleep(2)
    reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
    ActionChains(driver).move_to_element(reserve_button).click().perform()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

    time.sleep(2)
    # Step 5: Click the "send" button
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
    ActionChains(driver).move_to_element(send_button).click().perform()

    time.sleep(2)
    # Step 6: Validate that "SVBurger Summary" is displayed
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()


#Suite 1: SIGN IN (FUNCTIONALITY)
# List of Hotmail users for parameterization
hotmail_users_list =[
    ["margaritadiaz@live.com", "marga345@"],
    ["danacohen@live.com","dana765@"],
    ["juliangonzales@live.com","julian883!"]
]

@pytest.mark.parametrize("hotmail_names", hotmail_users_list)
def test_login_via_hotmail(setup, hotmail_names):
    """
    Test the login functionality with Hotmail credentials.
    Verifies that after logging in, the user can select a product and reserve it.
    """
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter email and password to sign in
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys(hotmail_names[0])
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(hotmail_names[1])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.ID, "mainHeader").is_displayed()

    # Step 3: Select a product
    time.sleep(2)
    select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

    # Step 4:Validate and click the "Reserve" button
    time.sleep(2)
    reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
    ActionChains(driver).move_to_element(reserve_button).click().perform()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

    time.sleep(2)
    # Step 5: Click the "send" button
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
    ActionChains(driver).move_to_element(send_button).click().perform()

    time.sleep(2)
    # Step 6: Validate that "SVBurger Summary" is displayed
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()


#Suite 1: SIGN IN (ERROR HANDLING)
def test_login_without_insert_an_email(setup):
    """
    Test that attempting to log in without an email shows an error message.
    """
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter "8839295" in the password field without entering an email
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")

    # Step 3: Click the " Sign in" Button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Step 4: Check if an alert message "Failed to log in" appears
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f" Alert detected: {alert_text}")
        assert "Failed to log in" in alert_text, " Error: The expected alert message was not found."
        alert.accept()

    except:
      pytest.fail("Test failed: An unexpected alert appeared.")

    print("Test passed: Logging in without an email is not allowed.")



#Suite 1: SIGN IN (ERROR HANDLING)
def test_login_in_with_wrong_password(setup):
    """
    Test that attempting to log in with a wrong passwords shows an error message.
    """
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter an email and wrong password "8839296" in the password field
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839296")

    # Step 3: Click the " Sign in" Button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 4: Check if an alert message "Failed to log in" appears
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f" Alert detected: {alert_text}")
        assert "Failed to log in" in alert_text, " Error: The expected alert message was not found."
        alert.accept()

    except:
      pytest.fail("Test failed: An unexpected alert appeared.")

    print("Test passed: Logging in with a wrong password is not allowed.")


#Suite 2: SIGN UP (FUNCTIONALITY)
def test_sign_up_only_with_required_fields(setup):
   driver = setup
   wait = WebDriverWait(driver, 20)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign up" button
   driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

   # Step 2: Fill out the registration form only with required fields( email and password)
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("laniadosaritaaa@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys("mybebe23!")
   driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("mybebe23!")

   # Step 3: Click the " Sign up" Button
   driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
   time.sleep(5)


    # Step 4: Check if an alert appears
   try:
       alert = driver.switch_to.alert
       alert_text = alert.text
       print(f" ALERT DETECTED: {alert_text}")
       pytest.fail(f"TEST FAILED: An unexpected alert was displayed: '{alert_text}'")

   except:
       print("An unexpected alert was displayed. ")

   # Step 5: Verify if the user is redirected to the menu after registration
   try:
       assert driver.find_element(By.ID, "mainHeader").is_displayed()
       print("SUCCESSFUL REGISTRATION: The user was registered and the menu is visible.")

   except:
       print("❌ BUG: The system does not redirect to the menu after filling the required fields.")
       pytest.fail(
           " TEST FAILED: The user should have been redirected to the menu after registering, but it did not happen.")


#Suite 2: SIGN UP (FUNCTIONALITY)
def test_register_with_a_first_name_that_contains_7_chars(setup):
   driver = setup
   wait = WebDriverWait(driver, 20)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign up" button
   driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

   # Step 2: Register with a first name that contains 7 chars on the "first name field"
   driver.find_element(By.XPATH, "//input[@placeholder='Type your first name']").send_keys("Teefili")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("laniadosara@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys("World!")
   driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("World!")

   # Step 3: Click the " Sign up" Button
   driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
   time.sleep(5)

   # Step 4: Check if an alert appears
   try:
       alert = driver.switch_to.alert
       alert_text = alert.text
       print(f" ALERT DETECTED: {alert_text}")
       pytest.fail(f"TEST FAILED: An unexpected alert was displayed: '{alert_text}'")

   except:
       print(" An unexpected alert was displayed. ")

   # Step 5: Verify if the user is redirected to the menu after registration
   try:
       assert driver.find_element(By.ID, "mainHeader").is_displayed()
       print(" SUCCESSFUL REGISTRATION: The user was registered and the menu is visible.")

   except:
       print("❌ BUG: The system does not redirect to the menu after filling the obligatory fields.")
       pytest.fail(
           "TEST FAILED: The user should have been redirected to the menu after registering, but it did not happen.")


#Suite 2: SIGN UP (FUNCTIONALITY)
def test_register_with_a_last_name_that_contains_7_chars(setup):
   driver = setup
   wait = WebDriverWait(driver, 20)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign up" button
   driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

   # Step 2: Register with last name that contains 7 chars on the "last name field"
   driver.find_element(By.XPATH, "//input[@placeholder='Type your last name']").send_keys("laniado")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("sara02@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys("Loove3")
   driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("Loove3")

   # Step 3: Click the " Sign up" Button
   driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
   time.sleep(5)

   # Step 4: Check if an alert appears
   try:
       alert = driver.switch_to.alert
       alert_text = alert.text
       print(f" ALERT DETECTED: {alert_text}")
       pytest.fail(f" TEST FAILED: An unexpected alert was displayed: '{alert_text}'")

   except:
       print(" An unexpected alert was displayed. ")

   # Step 5: Verify if the user is redirected to the menu after registration
   try:
       assert driver.find_element(By.ID, "mainHeader").is_displayed()
       print("SUCCESSFUL REGISTRATION: The user was registered and the menu is visible.")

   except:
       print("❌ BUG: The system does not redirect to the menu after filling the obligatory fields.")
       pytest.fail(
           " TEST FAILED: The user should have been redirected to the menu after registering, but it did not happen.")


#Suite 2: SIGN UP (BOUNDARY VALUES)
def test_register_with_6_chars_in_the_first_name(setup):
   driver = setup
   wait = WebDriverWait(driver, 20)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign up" button
   driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

   # Step 2: Register with last name that contains 6 chars on the "first name field"
   driver.find_element(By.XPATH, "//input[@placeholder='Type your first name']").send_keys("Liiamy")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("sara03@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys("Amore@")
   driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("Amore@")

   # Step 3: Click the " Sign up" Button
   driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
   time.sleep(5)

   # Step 4: Check if an alert appears
   try:
       alert = driver.switch_to.alert
       alert_text = alert.text
       print(f"ALERT DETECTED: {alert_text}")
       pytest.fail(f"TEST FAILED: An unexpected alert was displayed: '{alert_text}'")

   except:
       print(" An unexpected alert was displayed. ")

   # Step 5: Verify if the user is redirected to the menu after registration
   try:
       assert driver.find_element(By.ID, "mainHeader").is_displayed()
       print(" SUCCESSFUL REGISTRATION: The user was registered and the menu is visible.")

   except:
       print("❌ BUG: The system does not redirect to the menu after filling the obligatory fields.")
       pytest.fail(
           " TEST FAILED: The user should have been redirected to the menu after registering, but it did not happen.")


#Suite 2: SIGN UP (BOUNDARY VALUES)
def test_register_with_10_chars_in_the_last_name(setup):
   driver = setup
   wait = WebDriverWait(driver, 20)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign up" button
   driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

   # Step 2: Register with last name that contains 10 chars on the "last name field"
   driver.find_element(By.XPATH, "//input[@placeholder='Type your last name']").send_keys("landolando")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("sara04@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys("Saral3")
   driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("Saral3")

   # Step 3: Click the " Sign up" Button
   driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
   time.sleep(5)

   # Step 4: Check if an alert appears
   try:
       alert = driver.switch_to.alert
       alert_text = alert.text
       print(f"ALERT DETECTED: {alert_text}")
       pytest.fail(f"TEST FAILED: An unexpected alert was displayed: '{alert_text}'")

   except:
       print(" An unexpected alert was displayed. ")

   # Step 5: Verify if the user is redirected to the menu after registration
   try:
       assert driver.find_element(By.ID, "mainHeader").is_displayed()
       print("SUCCESSFUL REGISTRATION: The user was registered and the menu is visible.")

   except:
       print("❌ BUG: The system does not redirect to the menu after filling the obligatory fields.")
       pytest.fail(
           "TEST FAILED: The user should have been redirected to the menu after registering, but it did not happen.")


#Suite 2: SIGN UP (ERROR HANDLING)
def test_Sign_up_with_less_than_6_chars_on_the_password_field(setup):
    driver = setup
    wait = WebDriverWait(driver, 20)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign up" button
    driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

    # Step 2: Register with less than 6 chars on the password field
    driver.find_element(By.XPATH, "//input[@placeholder='Type your first name']").send_keys("Maria")
    driver.find_element(By.XPATH, "//input[@placeholder='Type your last name']").send_keys("laniado")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2025@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys("H3llo")
    driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("H3llo")

    # Step 3: Click the " Sign up" Button
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    time.sleep(5)

    # Step 4: Check if an alert message "Error: Password should be at least 6 characters" appears
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f" Alert detected: {alert_text}")

        # Validate that the alert contains the expected message
        assert "Error: Password should be at least 6 characters" in alert_text, "⚠️Error: The expected alert message was not found."
        alert.accept()

        # Ensure the user is still on the Sign-Up page and hasn't moved forward
        assert driver.current_url == "https://svburger1.co.il/#/SignUp", "Error: User advanced without completing required fields."

    except:
        pytest.fail("Test failed: Expected alert did not appear.")

    print("✅ Test passed successfully. The system don't let sign up with less than 6 chars on the password field")

#Suite 2: SIGN UP (ERROR HANDLING)
def test_Sign_up_with_more_than_10_chars_in_the_password_field(setup):
    driver = setup
    wait = WebDriverWait(driver, 20)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign up" button
    driver.find_element(By.XPATH, '//button[text()= "Sign Up"]').click()

    # Step 2: Register with invalid email with cases like: without @
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Create Password']").send_keys("saraestefania")
    driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("saraestefania")

    # Step 3: Click the " Sign up" Button
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    time.sleep(5)

    # Step 4: Check if an alert message "Password should be at maximum 10 characters" appears
    try:
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f" Alert detected: {alert_text}")

        # Validate that the alert contains the expected message
        assert "Password should be at maximum 10 characters" in alert_text, "️Error: The expected alert message was not found."
        alert.accept()

        # Ensure the user is still on the Sign-Up page and hasn't moved forward
        assert driver.current_url == "https://svburger1.co.il/#/SignUp", "Error: User advanced without completing required fields."

        print("✅ Test passed successfully. The system doesn't allow signing up with more than 10 chars in the password field")

    except TimeoutException:
         pytest.fail("❌ Test failed: Timeout while waiting for the expected alert.")

#Suite 3: Reservation and Confirm Reservation (FUNCTIONALITY)
def test_select_same_meal_twice_to_cancel_order(setup):
   driver = setup
   wait=  WebDriverWait(driver, 5)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign in" button
   driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

   # Step 2: Enter email and password to sign in
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
   driver.find_element(By.XPATH, "//button[@type='submit']").click()
   assert driver.find_element(By.ID, "mainHeader").is_displayed()

   # Step 3: Select a product
   time.sleep(2)
   select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
   actions.move_to_element(select_product).perform()
   wait.until(EC.element_to_be_clickable(select_product)).click()

   # Step 4: Select twice the same meal
   time.sleep(2)
   select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
   actions.move_to_element(select_product).perform()
   wait.until(EC.element_to_be_clickable(select_product)).click()

   # Step 4: Verify if the "Reserve" button is disabled
   try:
       reserve_button = driver.find_element(By.XPATH, '//button[text()=" Reserve "]')

       if reserve_button.get_attribute("disabled"):
           print("Success: The 'Reserve' button is disabled when we click twice the same meal.")
       else:
           print("The 'Reserve' button is NOT disabled when it should be.")

   except:
       print(" The 'Reserve' button was not found.")


#Suite 3: Reservation and Confirm Reservation (FUNCTIONALITY)
def test_functionability_of_log_out_button(setup):
   driver = setup
   wait=  WebDriverWait(driver, 5)
   actions = ActionChains(driver)

   # Step 1: Click the "Sign in" button
   driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

   # Step 2: Enter email and password to sign in
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
   driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
   driver.find_element(By.XPATH, "//button[@type='submit']").click()
   assert driver.find_element(By.ID, "mainHeader").is_displayed()


   # Step 3: Press log out
   time.sleep(2)
   log_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Log out "]')))
   ActionChains(driver).move_to_element(log_out_button).click().perform()
   time.sleep(2)
   assert driver.find_element(By.ID, "mainHeader").is_displayed()


#Suite 3: Reservation and Confirm Reservation (FUNCTIONALITY)
def test_order_two_meals(setup):
       driver = setup
       wait = WebDriverWait(driver, 5)
       actions = ActionChains(driver)

       # Step 1: Click the "Sign in" button
       driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

       # Step 2: Enter email and password to sign in
       driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
       driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
       driver.find_element(By.XPATH, "//button[@type='submit']").click()
       assert driver.find_element(By.ID, "mainHeader").is_displayed()

       # Step 3: Select one meal - Sides
       time.sleep(2)
       select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
       actions.move_to_element(select_product).perform()
       wait.until(EC.element_to_be_clickable(select_product)).click()

       # Step 4: Select second meal - "vegan"
       time.sleep(2)
       select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Vegan"]')))
       actions.move_to_element(select_product).perform()
       wait.until(EC.element_to_be_clickable(select_product)).click()

       # Step 4:Validate and click the "Reserve" button
       time.sleep(2)
       reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
       ActionChains(driver).move_to_element(reserve_button).click().perform()
       time.sleep(2)
       assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

       try:
           # Get the total value of the meals (Vegan + Slides )
           element = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[6]")
           meal_total = element.text.split()[-1]
           print(f"Total summary meals: {meal_total}")

       except TimeoutException:
           pytest.fail("Timeout occurred while trying to get the meal total.")

       # Step 6: Click the "Send" button
       send_button = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
       ActionChains(driver).move_to_element(send_button).pause(1).click().perform()

       try:
           wait = WebDriverWait(driver, 15)

           # Wait for the summary total to appear before retrieving its text
           wait.until(EC.presence_of_element_located( (By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]")))

           # Get the summary total value
           element = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]")
           summary_total = element.text.strip().split()[-1]
           print(f"Total value meals: {summary_total}")

           # Compare values
           if meal_total != summary_total:
               error_message = f"❌ Bug: The summary total ({summary_total}) does not match the sum of the meals ({meal_total}). The service fee is not included in the total order."
               print(error_message)
               pytest.fail(error_message)

       except TimeoutException:
           pytest.fail("Summary total was not found")

# Suite 3: Reservation and Confirm Reservation (BOUNDARY VALUES)
def test_select_minimum_1_meals_in_the_menu_page(setup):
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter email and password to sign in
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.ID, "mainHeader").is_displayed()

    # Step 3: Select one meal - Sides
    time.sleep(2)
    select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

    # Step 4:Validate and click the "Reserve" button
    time.sleep(2)
    reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
    ActionChains(driver).move_to_element(reserve_button).click().perform()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

    try:
        # Get the total value of the meal
        element = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[3]/div[6]")
        meal_total = element.text.split()[-1]
        print(f"Total summary meals: {meal_total}")

    except TimeoutException:
        pytest.fail("Timeout occurred while trying to get the meal total.")

    # Step 6: Click the "Send" button
    send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
    ActionChains(driver).move_to_element(send_button).pause(1).click().perform()

    try:
        wait = WebDriverWait(driver, 15)

        # Wait for the summary total to appear before retrieving its text
        wait.until(EC.presence_of_element_located( (By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]")))

        # Get the summary total value
        element = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]")
        summary_total = element.text.strip().split()[-1]
        print(f"Total value meals: {summary_total}")

        # Compare values
        if meal_total != summary_total:
            error_message = f"❌ Bug: The summary total ({summary_total}) does not match the sum of the meals ({meal_total}). The service fee is not included in the total order."
            print(error_message)
            pytest.fail(error_message)

    except TimeoutException:
        pytest.fail("Summary total was not found")


# Suite 3: Reservation and Confirm Reservation (BOUNDARY VALUES)
def test_select_maximum_3_meals_in_the_menu_page(setup):
        driver = setup
        wait = WebDriverWait(driver, 5)
        actions = ActionChains(driver)

        # Step 1: Click the "Sign in" button
        driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

        # Step 2: Enter email and password to sign in
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert driver.find_element(By.ID, "mainHeader").is_displayed()

        # Step 3: Select one meal -Kids meal
        time.sleep(2)
        select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Kids Meal"]')))
        actions.move_to_element(select_product).perform()
        wait.until(EC.element_to_be_clickable(select_product)).click()

        element = driver.find_element(By.XPATH,   "//div[contains(@class, 'card') and contains(@style, 'background-color: lightblue')]")
        assert element, "The background color did not change to lightblue after selecting Kids Meal."

        # Step 4: Select second meal - Burger
        time.sleep(2)
        select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Burger"]')))
        actions.move_to_element(select_product).perform()
        wait.until(EC.element_to_be_clickable(select_product)).click()

        element = driver.find_element(By.XPATH,"//div[contains(@class, 'card') and contains(@style, 'background-color: lightblue')]")
        assert element, "The background color did not change to lightblue after selecting Burger."

        # Step 5: Select third  meal - "vegan"
        time.sleep(2)
        select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Vegan"]')))
        actions.move_to_element(select_product).perform()
        wait.until(EC.element_to_be_clickable(select_product)).click()

        element = driver.find_element(By.XPATH, "//div[contains(@class, 'card') and contains(@style, 'background-color: lightblue')]")
        assert element, "The background color did not change to lightblue after selecting Vegan."

        # Step 6:Validate and click the "Reserve" button
        time.sleep(2)
        reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
        ActionChains(driver).move_to_element(reserve_button).click().perform()
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

        try:
            wait = WebDriverWait(driver, 10)

            # wait in the total value of the meals is present (Vegan + burger + kids meals )
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[5]/div[6]")))
            meal_total = element.text.strip().split()[-1]
            print(f"Total summary meals: {meal_total}")

        except TimeoutException:
            pytest.fail("Timeout occurred while trying to get the meal total.")

            # verify the button send
        try:
            send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
            driver.execute_script("arguments[0].scrollIntoView(true);", send_button)

            try:
                send_button.click()
            except:
                driver.execute_script("arguments[0].click();", send_button)

        except TimeoutException:
            pytest.fail("didn't find the 'Send' button")

        try:
            wait = WebDriverWait(driver, 15)

            # Wait for the summary total to appear before retrieving its text
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]")))
            summary_total = element.text.strip().split()[-1]
            print(f"Total value meals: {summary_total}")

            # Compare values
            if meal_total != summary_total:
                error_message = f"❌ Bug: The summary total ({summary_total}) does not match the sum of the meals ({meal_total}). The service fee is not included in the total order."
                print(error_message)
                pytest.fail(error_message)

        except TimeoutException:
            pytest.fail("Summary total was not found")


# Suite 3: Reservation and Confirm Reservation (ERROR HANDLING)
def test_insert_3_on_quantity_field(setup):
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter email and password to sign in
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.ID, "mainHeader").is_displayed()

   # Step 3: Select a product
    time.sleep(2)
    select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

   # Step 4:Validate and click the "Reserve" button
    time.sleep(2)
    reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Reserve "]')))
    ActionChains(driver).move_to_element(reserve_button).click().perform()
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//h1[text()='SVBurger Summary']").is_displayed()

    # Step 5: Insert "3" in the "Quantity." field
    quantity_number_field = driver.find_element(By.XPATH, "//input[@max='2']")
    quantity_number_field.clear()
    time.sleep(2)
    quantity_number_field.send_keys("3")


    # Step 5: Clic en "Send"
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Send")]')))
    send_button.click()

    # Step 6: Validate error message "Invalid value in quantity"
    try:
        error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Invalid value in quantity')]")))
        assert error_message.is_displayed(), " ERROR: The expected message did not appear."
        print("Error message displayed correctly: 'Invalid value in quantity'")

    except:
        print(" ERROR: The summary page opened with 3 Kid's Meals (validation failed).")
        pytest.fail("Validation of the Quantity field failed.")

# Suite 3: Reservation and Confirm Reservation (ERROR HANDLING)
def test_select_4_meals_in_the_menu_page(setup):
    driver = setup
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

    # Step 1: Click the "Sign in" button
    driver.find_element(By.XPATH, '//a[@href = "#/SignIn"]/button').click()

    # Step 2: Enter email and password to sign in
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("slaniado2018@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("8839295")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert driver.find_element(By.ID, "mainHeader").is_displayed()

    #Step 3: Select one meal -Kids meal
    time.sleep(2)
    select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Kids Meal"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

    # Step 4: Select second meal - Burger
    time.sleep(2)
    select_product = wait.until( EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Burger"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

    # Step 4: Select third  meal - "vegan"
    time.sleep(2)
    select_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Vegan"]')))
    actions.move_to_element(select_product).perform()
    wait.until(EC.element_to_be_clickable(select_product)).click()

    # Check if the fourth meal is still selectable
    try:
        fourth_meal = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="col-md-8"]//h5[text()="Sides"]')))
        print("f❌ Bug: A fourth meal can be selected when it shouldn't be.")
        assert False, "BUG: A fourth meal was selected when it should be restricted."
    except TimeoutException:
        print("Correct: More than three meals cannot be selected")

































































