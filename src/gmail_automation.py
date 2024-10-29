# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
# Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
from unidecode import unidecode

# Chrome options
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-infobars")

# WebDriver service
service = ChromeService('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options)

french_first_names = [
    "Amélie", "Antoine", "Aurélie", "Benoît", "Camille", "Charles", "Chloé", "Claire", "Clément", "Dominique",
    "Élodie", "Émilie", "Étienne", "Fabien", "François", "Gabriel", "Hélène", "Henri", "Isabelle", "Jules",
    "Juliette", "Laurent", "Léa", "Léon", "Louise", "Lucas", "Madeleine", "Marc", "Margaux", "Marie",
    "Mathieu", "Nathalie", "Nicolas", "Noémie", "Olivier", "Pascal", "Philippe", "Pierre", "Raphaël", "René",
    "Sophie", "Stéphane", "Suzanne", "Théo", "Thomas", "Valentin", "Valérie", "Victor", "Vincent", "Yves",
    "Zoé", "Adèle", "Adrien", "Alexandre", "Alice", "Alix", "Anatole", "André", "Angèle", "Anne",
    "Baptiste", "Basile", "Bernard", "Brigitte", "Céleste", "Céline", "Christophe", "Cyril", "Denis", "Diane",
    "Édouard", "Éléonore", "Émile", "Félix", "Florence", "Georges", "Gérard", "Guillaume", "Hugo", "Inès",
    "Jacques", "Jean", "Jeanne", "Joséphine", "Julien", "Laure", "Lucie", "Maëlle", "Marcel", "Martine",
    "Maxime", "Michel", "Nina", "Océane", "Paul", "Perrine", "Quentin", "Romain", "Solène", "Thérèse"
]

french_last_names = [
    "Leroy", "Moreau", "Bernard", "Dubois", "Durand", "Lefebvre", "Mercier", "Dupont", "Fournier", "Lambert",
    "Fontaine", "Rousseau", "Vincent", "Muller", "Lefèvre", "Faure", "André", "Gauthier", "Garcia", "Perrin",
    "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Garnier", "Chevalier", "François",
    "Legrand", "Gérard", "Boyer", "Gautier", "Roche", "Roy", "Noel", "Meyer", "Lucas", "Gomez",
    "Martinez", "Caron", "Da Silva", "Lemoine", "Philippe", "Bourgeois", "Pierre", "Renard", "Girard", "Brun",
    "Gaillard", "Barbier", "Arnaud", "Martins", "Rodriguez", "Picard", "Roger", "Schmitt", "Colin", "Vidal",
    "Dupuis", "Pires", "Renaud", "Renault", "Klein", "Coulon", "Grondin", "Leclerc", "Pires", "Marchand",
    "Dufour", "Blanchard", "Gillet", "Chevallier", "Fernandez", "David", "Bouquet", "Gilles", "Fischer", "Roy",
    "Besson", "Lemoine", "Delorme", "Carpentier", "Dumas", "Marin", "Gosselin", "Mallet", "Blondel", "Adam",
    "Durant", "Laporte", "Boutin", "Lacombe", "Navarro", "Langlois", "Deschamps", "Schneider", "Pasquier", "Renaud"
]

# Randomly select a first name and a last name
your_first_name = random.choice(french_first_names)
your_last_name = random.choice(french_last_names)

# Generate a random number
random_number = random.randint(1000, 9999)

# Retirer les accents des prénoms et nom de famille
your_first_name_normalized = unidecode(your_first_name).lower()
your_last_name_normalized = unidecode(your_last_name).lower()


your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}"


your_birthday = "02 3 1989" #dd m yyyy exp : 24 11 2003
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "econ_data_lab_2024"

def save_account(email, password, file_name="generated_emails.txt"):
    with open(file_name, "a") as file:
        file.write(f"Gmail: {email}@gmail.com\nPassword: {password}\n\n")


def fill_form(driver, username):
    try:
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Fill in first name and last name
        first_name = driver.find_element(By.NAME, "firstName")
        last_name = driver.find_element(By.NAME, "lastName")
        first_name.clear()
        first_name.send_keys(your_first_name)
        last_name.clear()
        last_name.send_keys(your_last_name)
        
        # Click the next button
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Wait for birthday fields to be visible and fill in the birth date
        wait = WebDriverWait(driver, 20)
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))
        birthday_elements = your_birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(birthday_elements[1])
        day_field = driver.find_element(By.ID, "day")
        day_field.clear()
        day_field.send_keys(birthday_elements[0])
        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        # Select gender
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value(your_gender)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Custom email option if present
        time.sleep(2)
        if driver.find_elements(By.ID, "selectionc4"):
            create_own_option = wait.until(EC.element_to_be_clickable((By.ID, "selectionc4")))
            create_own_option.click()

        # Fill in username
        create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(username)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        time.sleep(2)

        # Enter password and confirm
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(your_password)
        confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(your_password)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()
        
        time.sleep(2)

        # Skip phone number and recovery email if possible
        try:
            skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
            for button in skip_buttons:
                button.click()
        except Exception as e:
            print("No skip option available:", e)


        time.sleep(5)

        # Agree to terms
        agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()

        time.sleep(5)

        print(f"Account created successfully:\n{{\ngmail: {username}@gmail.com\npassword: {your_password}\n}}")
        return True

    except Exception as e:
        print(f"Failed to create account {username}@gmail.com: {e}")
        return False

    finally:
        driver.quit()


for i in range(3):
    driver = webdriver.Chrome(options=chrome_options)
    
    # Generate random name and username
    first_name = random.choice(french_first_names)
    last_name = random.choice(french_last_names)
    first_name_normalized = unidecode(first_name).lower()
    last_name_normalized = unidecode(last_name).lower()
    random_number = random.randint(1000, 9999)
    username = f"{first_name_normalized}.{last_name_normalized}{random_number}"
    
    # Attempt to fill form and create account
    success = fill_form(driver, username)
    if success:
        save_account(username, your_password)