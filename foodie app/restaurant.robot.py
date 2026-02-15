*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Add Restaurant
    Create Session    foodie    http://localhost:5001
    ${response}=    POST On Session    foodie    /api/v1/restaurants
    ...    json={"name":"Robot Hotel"}
    Status Should Be    201    ${response}