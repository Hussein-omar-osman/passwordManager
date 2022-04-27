
## Password Manager

## Project Description

This an application that will help us manage our passwords and even generate new passwords for us by using the Tkinter GUI based user interface

## Author
Hussein Omar

## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing acounts login details the data.json file.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Copy my credentials to the clipboard

## Technologies used
- Python3.10
    - Modules used:
        - tkinter
        - random
        - pyperclip
        - json

## Behavior Driven Enviroment

- #### Create account and store old accounts
   - Given that a user has provided both a username and password
   - When a user requests to create an account
   - Then the system should create and save the account to data.json file
   - The user can still add old accounts to the json file

    
- #### Display Credential
   - Given that a user has credentials saved
   - The user can search through the accounts stored in the json file
   - Then the system should return all saved credentials

## Project setup instruction.
Git clone from GitHub. Open with IDE of your choose. Open Terminal and run python3.10 main.py. Tkinter GUI will open asking for password, by the way it's 5868. After that you will be greeted with the accounts input window. In here you can input your old accounts or even generate new ones. A neat feature is when search or generate password, the password will be saved on your clipboard and paste any where. 

## Support and contact details
In case of any issues or alert,feel free to contact me via; E-mail: husseinomar6190@gmail.com

##Know bugs
No know bugs

## License
{See below for more details on licensing.}
This is under the [MIT](LICENSE.txt) license Copyright (c) {2022} {Hussein Omar}