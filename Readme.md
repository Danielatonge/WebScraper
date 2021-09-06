## STEP 1: Download a driver for the webdriver plugin
For Chrome users, you can find the driver at (Pick a suitable driver for your Operating System):
```
https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.15/
```
For non-Chrome users, head over to:
```commandline
https://www.selenium.dev/selenium/docs/api/py/index.html
```
and pick your favorite browser and its version to download its driver.

## STEP 2: Modify the code accordingly
In my case, I downloaded the Chrome driver. That's why we have ``webdriver.Chrome``. If you download for Firefox 
or Opera, this line shown below will be a little different. My path was ``/Users/macbookpro/Downloads/chromedriver``
```
11. driver = webdriver.Chrome('/absolute/path/to/driver/you/downloaded')
```

## STEP 3: Create a Virtual environment and install requirements
To create a virtual environment, run the code below:
```commandline
python3 -m venv venv
source venv/bin/activate
```
Run the python code below to install all requirements needed
```commandline
pip install -r requirements.txt
```

## STEP 4: Run the python script
Click the run button if you are using an IDE or run the commandline code below:
```commandline
python3 full_list.py
```