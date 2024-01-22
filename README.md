*A simple demo of databrix.org, which contents project description and database*
# Deploy on your local machine

## Requirement:
1. VS Code
2. Git GUI
3. pipenv (python package)

## Step 1: Clone this repository
1. Open your VS Code and select **Source Control** in the left sidebar

2. Copy this URL `https://github.com/databrix-org/demo-databrix.org-yuqiang`

3. Click the **...** on the top of Menu (Views and More actions) --> Select **Clone**

4. Select **Clone from Github** 

5. Paste URL into the search box and Select the Repo

6. Clone it into a directory, where you want to store these scripts

## Step 2: Install packages

1. Open your Python Terminal

2. Open the directory of Repo in the Terminal, where you just stored scripts in it.

3. Create a virtual environment using pipenv. Run code: `pipenv install`

4. Activate the virtual environment. Run code: `pipenv shell`

5. Install required packages in this virtual environment. Run code: `pipenv install requirements.txt`

## Step 3: Run the frontend and backend Server

1. Open your Python Terminal and open the directory of Repo in your Terminal

2. Run the backend Server. Run code: `uvicorn backend_main:app --reload`

3. Do not close this Python Terminal and Open another python Terminal

4. Open the directory of Repo in second Terminal.

5. Run the frontend Server. Run code: `streamlit run Homepage.py`
