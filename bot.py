
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

def generuj_meno():
    return 'user' + ''.join(random.choices(string.digits, k=6))

def generuj_heslo():
    return 'Pass' + ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '!'

def vytvor_atomic_mail(driver, wait):
    """Vytvorenie Atomic Mail účtu"""
    meno = generuj_meno()
    heslo = generuj_heslo()
    email = f"{meno}@atomicmail.io"
    
    print(f"📧 Vytváram Atomic Mail: {email}")
    
    # Atomic Mail registrácia
    driver.get("https://atomicmail.io/app/auth/sign-up")
    time.sleep(3)
    
    # Vyplnenie formulára
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        try:
            placeholder = inp.get_attribute("placeholder") or ""
            type_attr = inp.get_attribute("type") or ""
            
            if "email" in placeholder.lower() or type_attr == "email":
                inp.send_keys(email)
            elif "password" in type_attr:
                inp.send_keys(heslo)
            elif "confirm" in placeholder.lower():
                inp.send_keys(heslo)
        except:
            pass
    
    # Kliknutie na Sign Up
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons:
        if "sign up" in btn.text.lower():
            btn.click()
            break
    
    # Čakanie na manuálne vyriešenie CAPTCHA (v cloude to bude problém)
    # Toto je limitácia - Atomic Mail vyžaduje CAPTCHA
    
    return {"email": email, "heslo": heslo, "typ": "atomic_mail"}

def main():
    # Nastavenie prehliadača pre headless režim
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # Tu by bol kód, ale Atomic Mail má CAPTCHA...
        print("❌ Tento spôsob NEBUDE fungovať kvôli CAPTCHA")
        print("Atomic Mail vyžaduje manuálne overenie že nie si robot")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
