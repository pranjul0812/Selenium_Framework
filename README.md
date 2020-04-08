# Selenium_Framework
Disclaimer: the test site has now added capcha while login so the scripts can no longer be give the desired result.
to run the commands successfully you need to do below changes after cloning the project.
rename the project/folder name as "automation_framework_prac" instead of "Selenium_Frameowrk"
install pytest, pytest-html, ddt
change the chromedriver/iedriver path in the base/webdriverfactory.py
change the path for the testdata.csv in /tests/courses/register_courses_csv_data_test.py
open the cmd in automation_framework_prac folder
run commands:- pytest -s -v /tests/test_suite_demo.py --browser chrome --html='nameofreportfile'.html
all the logs will be appends to automation.log file(please delete the file before running the pytest command to get the fresh logs)
reprot(html) file be generated in the automation_framework_prac folder.
