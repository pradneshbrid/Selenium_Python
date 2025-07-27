*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://rahulshettyacademy.com/
${PRACTICE_URL}    https://rahulshettyacademy.com/AutomationPractice/
${CHROMEDRIVER}    E://Chrome Driver//chromedriver.exe    

*** Test Cases ***
Basic Browser Operations
    # Open the browser using Chrome WebDriver
    Open Browser    ${URL}    chrome    executable_path=${CHROMEDRIVER}
    # Maximize the browser window
    Maximize Browser Window
    # Get and log the title and URL
    ${title}=    Get Title
    Log    Title: ${title}
    ${url}=    Get Location
    Log    URL: ${url}
    # Navigate to another URL
    Go To    ${PRACTICE_URL}
    Capture Page Screenshot
    # SeleniumLibrary.Minimize Browser Window
    # Perform browser operations
    Go Back
    Reload Page
    # Close the browser
    # Close Browser
