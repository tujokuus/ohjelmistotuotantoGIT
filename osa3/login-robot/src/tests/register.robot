*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tuomas  Tuomas123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  tu  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  uomas11/  kalle123
    Output Should Contain  Username must contain only lower case letters from a to z 

Register With Valid Username And Too Short Password
    Input Credentials  tuomas  Tu1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  tuomas  Tuomasaaa
    Output Should Contain  Password must at least contain one non-letter character