*A simple demo of databrix.org, which contents project description and database*
# Deploy on your local machine

> [!CAUTION]
> **Please don´t upload any Credential in GitHub. This may cause unauthorized access and excessive charges!**

## Requirements:
1. VS Code
2. GitHub Desktop
3. python Version 3.12.1


## Step 1: Clone this repository
1. Open your VS Code and select **Source Control** in the left sidebar

2. Copy this URL `https://github.com/databrix-org/demo-databrix.org-yuqiang`

3. Click the **...** on the top of Menu (Views and More actions) --> Select **Clone**

4. Select **Clone from Github** in the search box

5. Paste URL into the search box and Select the Repo showed.

9. Create a directory. And clone it into this directory, where you want to store these scripts

## Step 2: Install packages

1. Open a TERMINAL in VS Code

2. Open the directory of Repo in the Terminal. Normally you are already in this directory after cloning.

3. create new virtual environment and download packages using pipenv. Run code `pip install pipenv`

4.Install pipenv in virtual environment and install required packages. Run code 'pip install pipenv' and `pipenv install`

## Step 3: Run the frontend and backend Server

1. Activate the new environment. Run code `pipenv shell`

2. Run the backend Server. Run code: `uvicorn backend_main:app --reload`

3. Do not close this Terminal and Open another Terminal.

4. Open the directory of Repo in second Terminal. Using `cd C:\path\to\repo`

5. Activate the virtual environment you have created in strp 2. Run code `pipenv shell`

6. Run the frontend Server. Run code: `streamlit run Homepage.py`
