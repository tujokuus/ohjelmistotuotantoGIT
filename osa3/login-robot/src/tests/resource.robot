*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Register Command
    Input  new

Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command


Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
