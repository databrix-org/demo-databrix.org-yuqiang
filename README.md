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

6. Create a directory. And clone it into this directory, where you want to store these scripts

## Step 2: Install packages

1. Open a TERMINAL in VS Code

2. Open the directory of Repo in the Terminal. Normally you are already in this directory after cloning.

3. Install pipenv. Run code `pip install pipenv`

4. Create new virtual environment and specify python version. Run code `python -m pipenv --python 3.12.1`

5. Activate this virtual environment and install pipenv in this environment. Run code `python -m pipenv shell` and `pip install pipenv`

6. Install all packages needed. Run code `pipenv install`

7. If you use Windows, please install colorama. Run code `pipenv install colorama`

## Step 3: Run the frontend and backend Server

1. Run the backend Server. Run code: `uvicorn backend_main:app --reload`

2. Do not close this Terminal and Open another Terminal.

3. Open the directory of Repo in second Terminal. Using `cd C:\path\to\repo`

4. Activate the virtual environment you have created in step 2. Run code `python -m pipenv shell`

5. Run the frontend Server. Run code: `streamlit run Homepage.py`
