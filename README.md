# robo-advisor-project
Robo Advisor:

Setup:

1. Clone this repository onto your computer.

git clone https://github.com/megc1/robo-advisor-project

cd robo-advisor-project

2. Create a new virtual environment and use pip to install python-dotenv.

3. Request an API key from www.alphavantage.co.

4. Create a .env file 

touch .env

5. Within your .env file, add the following code, replacing "SECURE_KEY" with your API Key:
ALPHAVANTAGE_API_KEY='SECURE_KEY'

7. Create a csv file called prices.csv

To run:

1. On your terminal:
  i) cd ~/Desktop/robo-advisor-project (if you select a different name of your folder, use that in place of "robo-advisor-project")
  ii) cd app
  iii) conda activate name-of-virtual-environment (enter the name of the virtual environment you created instead of name-of-    virtual-environment)
  iv) python robo_advisor.py

2. Follow the prompts presented on the terminal. Your data will be written to prices.csv.
