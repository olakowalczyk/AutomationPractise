# Automation tests for [Automation Practise Website](http://automationpractice.com/ "automationpractice") 
## $\textcolor{red}{This\ testing\ page\ is\ no\ longer\ available\!}$
This is a simple project for testing website using **Pytest** and **Selenium**.

### Prerequisites
In order to run these tests:
  - **Chrome Web Browser** is needed

### Run project
Get clone from this repo
Open cmd
Run commands:
```
cd "the_repo_folder_path"
pip install pip
pip install -r requirements.txt
```
Run tests:
* Just for run all of the tests put:
```
pytest
```
* For run tests with the report:
```
pytest --html=report.html
```
* For run smoke tests:
```
pytest -m smoketest
```
##### Allure report
If **Allure** is available on your machine to obtain allure report run:
 (How to get Allure you can read here https://docs.qameta.io/allure/)


```
pytest --alluredir='path_for_allure_files'
```
and then:

```
allure serve 'path_for_allure_files'
```
