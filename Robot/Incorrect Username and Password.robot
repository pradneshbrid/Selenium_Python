*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}             https://rahulshettyacademy.com/loginpagePractise/
${BROWSER}         Chrome
${PASSWORD}        12345
${EMAIL_XPATH}     //p[normalize-space(text())="Please email us at"]//strong/a
${USERNAME_XPATH}  //input[@id="username"]
${PASSWORD_XPATH}  //input[@id="password"]
${SIGNIN_XPATH}    //input[@id="signInBtn"]
${ERROR_XPATH}     (//form[@id="login-form"]/div)[1]

*** Test Cases ***
Login With Captured Email Headless
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Call Method    ${options}    add_argument    --disable-gpu
    Create Webdriver    Chrome    options=${options}
    Go To    ${URL}
    Set Selenium Implicit Wait    10

    Click Element    //a[@class="blinkingText"]
    ${windows}=    Get Window Handles
    Switch Window    ${windows}[1]
    Wait Until Element Is Visible    ${EMAIL_XPATH}    10
    ${Email_ID}=    Get Text    ${EMAIL_XPATH}
    Log To Console    Email ID: ${Email_ID}
    Capture Page Screenshot    email_page.png

    Switch Window    ${windows}[0]
    Input Text    ${USERNAME_XPATH}    ${Email_ID}
    Input Text    ${PASSWORD_XPATH}    ${PASSWORD}
    Capture Page Screenshot    before_login.png

    Click Button    ${SIGNIN_XPATH}
    Wait Until Element Is Visible    ${ERROR_XPATH}    10
    ${error_message}=    Get Text    ${ERROR_XPATH}
    Log To Console    Error Message: ${error_message}
    Capture Page Screenshot    error_message.png

    Close Browser
    [Teardown]    Close All Browsers