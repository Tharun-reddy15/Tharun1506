*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
TC002.robot
    open browser    https://www.google.com/    firefox
    title should be    Google
    close browser