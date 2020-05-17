# Birthday-Reminder

This is a basic python script to check who among our friends are celebrating their birthday today.
It also lets you find friend(s) whose birthday(s) you might have missed with 'Recent Birthday' or even lets you find those friends whose birthday(s) are coming.

name for the script and module is **FacebookBirthday**.
> see **Usage Recommendation**

script uses selenium and a chrome headless browser option, so it will not open up.

## Prerequistes for executing Source Code
1. Python 3 and above
Libraries Required:
2. Selenium
3. Download chromedriver according to your chrome version and OS that you are using from https://chromedriver.chromium.org/downloads . Also, to check Chrome Browser version that you are using right now, search < chrome://version > in the google chrome search bar.

### For setting up Selenium & chromedriver on a Mac, follow the link below
http://jonathansoma.com/lede/foundations-2017/classes/more-scraping/selenium/

## Usage Recommendation
It is highly recommended that you use **main** module instead of using ~~FacebookBirthday~~.
**main** module gives you more control over the inner **FacebookBirthday**. all the options in `main` are configurable for one time change.

## Options
Script has three options

    1 number 1 represents that you want to view `Today Birthday List           
    2 number 2 represents that you want to view `Upcoming Birthday List
    3 number 3 represents that you want to view `Recent Birthday List

Depending on what you choose, Your Friend names will be displayed

> **Recent Birthday(s) are the ones that you missed!!**

## Script run
Depending on what module you chose to run below are some commands that will help you run script

* If you choose to run from **main** module. Do the below one time change

    ```python
        def get_birthday_friends():
            birthdays(<Email_id>, <password>,<Options>, <chrome driver exe path>)
    ```
    > Option parameter are mentioned in Option section (1 ,2 or 3)

    ```shellscript
         python3 main.py
    ```
* If you choose to run module **FacebookBirthday**. Do the following( this have to be done everytime you run script)

    ```shellscript
        python3 FacebookBirthday <Chrome_Driver_Path>
    ```

    |`NOTE` | Here you will be prompted for email , password and option(see option section above). |
    |-|-|

|`NOTE` | `python3` can command can be changed with `python` depends upon what did you set in env variables.|
|-|-|


## Enqueue impl
- [x] Find friends who all are celebrating birthdays
- [ ] Create personalized wish
- [ ] Run script on startUp  

## Contributing
Pull requests are welcome. For major changes, please open an `issue` first to discuss what you would like to change.