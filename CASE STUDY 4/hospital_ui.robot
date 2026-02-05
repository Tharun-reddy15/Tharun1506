*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://demoqa.com/text-box
${BROWSER}  chrome

*** Test Cases ***
Hospital UI
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Element Is Visible    id=userName    10
    Input Text    id=userName    Tharun
    Input Text    id=userEmail   test@email.com
    Input Text    id=currentAddress    Hyderabad

    # Scroll to bottom (IMPORTANT)
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)

    # Click using JavaScript to avoid intercept error
    Execute Javascript    document.getElementById("submit").click()

    Sleep    3
    Close Browser