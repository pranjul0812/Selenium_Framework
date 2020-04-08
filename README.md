# Selenium_Framework
Use Chrome Version >= 80.0.3987.163
Disclaimer: for version below 80 (such as version 73.0.3683.75) >> the test site shows capcha while login so the scripts can no longer give the desired result.
To run the scripts successfully you need to do below changes after cloning the project.
Steps after Cloning the project in local PC:-
rename the project/folder name as "automation_framework_prac" instead of "Selenium_Frameowrk"
install pytest, pytest-html, ddt
change the chromedriver/iedriver path in the base/webdriverfactory.py
change the path for the testdata.csv in /tests/courses/register_courses_csv_data_test.py
open the cmd in automation_framework_prac folder
run commands:- pytest -s -v /tests/test_suite_demo.py --browser chrome --html='nameofreportfile'.html
all the logs will be appends to automation.log file(please delete the file before running the pytest command to get the fresh logs)
reprot(html) file be generated in the automation_framework_prac folder.
