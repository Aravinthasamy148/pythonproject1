from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('http://sb2.connectedservices.com/sign-in')
    username = page.wait_for_selector("input[type= 'text']")
    username.type('admin@connectedservices.com')
    password = page.wait_for_selector('input[type ="password"]')
    password.type('SB2IVR25$!')
    loginbutton =page.wait_for_selector('button[type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(4000)
    print("CRE Admin successfully opend ")