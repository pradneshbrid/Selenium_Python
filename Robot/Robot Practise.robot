*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           OperatingSystem

*** Variables ***
${BASE_URL}       https://rahulshettyacademy.com/seleniumPractise/
${CHROME_DRIVER}  E://Chrome Driver//chromedriver.exe
${SEARCH_TERM}    ber
${PROMO_CODE}     rahulshettyacademy
${calculated_sum}    0
*** Test Cases ***
Verify Shopping Cart Functionality
    [Documentation]    Test case for verifying product selection, cart, and promo code functionality.
    Open Browser To Application
    Search And Add Products
    Verify Selected Products
    Proceed To Checkout
    Verify Cart Products
    Apply Promo Code
    Validate Discount And Total
    Close Browser

*** Keywords ***
Open Browser To Application
    Open Browser    ${BASE_URL}    chrome    executable_path=${CHROME_DRIVER}
    Set Selenium Implicit Wait    5

Search And Add Products
    Input Text    css:input.search-keyword    ${SEARCH_TERM}
    Sleep    4
    ${products}=    Get WebElements    xpath://div[@class='products']/div
    ${length}=    Get Length    ${products}
    ${Evaluate}    Evaluate    """${length}""" > """0"""
    Run Keyword If    """${Evaluate}""" == """True"""    Log    Elements are present
    ...    ELSE    Fail    Elements are not present
    ${buttons}=    Get WebElements    xpath://div[@class='product-action']/button
    ${buttons_len}    Get Length    ${buttons}
    ${selected_products}=    Create List
    FOR    ${button}    IN RANGE    1    ${buttons_len}+1
        ${product_name}=    Get Text    xpath=(//div[@class="products"]/div/h4)[${button}]
        Append To List    ${selected_products}    ${product_name}
        Sleep   5
        Click Element    (//*[contains(text(),"ADD TO CART")])[${button}]
    END
    Log    Selected Products: ${selected_products}
    Set Suite Variable    ${selected_products}

Verify Selected Products
    ${products}=    Set Variable    ${selected_products}
    Should Not Be Empty    ${products}

Proceed To Checkout
    Click Element    css:img[alt='Cart']
    Click Element    xpath://button[text()='PROCEED TO CHECKOUT']
    Wait Until Element Is Visible    class:promoCode

Verify Cart Products
    ${veggies}=    Get WebElements    css:p.product-name
    ${cart_products}=    Create List
    FOR    ${veg}    IN    @{veggies}
        ${veg_name}=    Get Text    ${veg}
        Append To List    ${cart_products}    ${veg_name}
    END
    Log    Cart Products: ${cart_products}
    Lists Should Be Equal    ${selected_products}    ${cart_products}

Apply Promo Code
    ${amount1}=    Get Text    css:.discountAmt
    Convert To Number    ${amount1}
    Log    Initial Amount: ${amount1}
    Set Global Variable    ${amount1}
    Input Text    class:promoCode    ${PROMO_CODE}
    Click Element    css:.promoBtn
    Wait Until Element Is Visible    css:span.promoInfo
    ${promo_info}=    Get Text    css:span.promoInfo
    Log    Promo Info: ${promo_info}
    ${amount2}=    Get Text    css:.discountAmt
    Convert To Number    ${amount2}
    Log    Amount After Discount: ${amount2}
    Set Global Variable    ${amount2}



Validate Discount And Total
    ${Check}    Run Keyword And Return Status    Evaluate    ${amount1} > ${amount2}
    Run keyword if     """${check}""" == """True"""    Log     AMount 1 is greater than Amount 2
    ...    ELSE     Fail     AMount 2 is greater than Amount 1
    ${veggie_prices}=    Get WebElements    xpath://tr/td[5]/p
    FOR    ${price}    IN    @{veggie_prices}
        ${price_text}=    Get Text    ${price}
        ${calculated_sum}=    Evaluate    ${calculated_sum} + float(${price_text})
    END
    Log    Calculated Total: ${calculated_sum}
    Should Be True    ${calculated_sum} >= ${amount2}