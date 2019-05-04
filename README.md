# Robo Advisor
[![Build Status](https://travis-ci.org/megc1/robo-advisor-project.svg?branch=master)](https://travis-ci.org/megc1/robo-advisor-project)

## About
This is a command-line application which allows users to specify a stock about which to gain relevant data, a buy recommendation based on user risk preferences, and stock price data visualization.


## To get started:

### Prerequisites:
* Anaconda 3.7
* Python 3.7
* Pip

### Package requirements:
The following Python packages are required to run this program: 
   * requests 
   * json 
   * datetime 
   * csv 
   * os 
   * dotenv 
   * matplotlib

## Setup:

### Installation:
1. First, clone or download this repository onto your computer.
```
git clone https://github.com/megc1/robo-advisor-project
```

```
cd robo-advisor-project
```

3. Request an [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key).

4. Create a .env file 

```
touch .env
```

5. Within your .env file, add the following code, replacing "SECURE_KEY" with your API Key:
```sh
ALPHAVANTAGE_API_KEY='SECURE_KEY'
```

## To run:

1. On your terminal:
```
  i) cd ~/Desktop/robo-advisor-project (if you select a different name of your folder, use that in place of "robo-advisor-project")
  
  ii) cd app
  
  iii) conda activate name-of-virtual-environment (enter the name of the virtual environment you created instead of name-of-    virtual-environment)
 
  iv) python robo_advisor.py
```
2. Follow the prompts presented on the terminal. Your data will be written to a csv file.
