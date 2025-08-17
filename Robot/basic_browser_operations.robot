*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://rahulshettyacademy.com/
${PRACTICE_URL}    https://rahulshettyacademy.com/AutomationPractice/
${CHROMEDRIVER}    E://Chrome Driver//chromedriver.exe    

*** Test Cases ***
Get Title And URL
    Open Browser    ${URL}    chrome    executable_path=${CHROMEDRIVER}
    Maximize Browser Window
    ${title}=    Get Title
    Log    Title: ${title}
    ${url}=    Get Location
    Log    URL: ${url}
    Go To    ${PRACTICE_URL}
    Capture Page Screenshot
    Go Back
    Reload Page
