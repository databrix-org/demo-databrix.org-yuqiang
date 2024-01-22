*A simple demo of databrix.org, which contents project description and database*
# Deploy on your local machine

## Requirement:
1. VS Code
2. GitHub Desktop
3. Anaconda prompt


## Step 1: Clone this repository
1. Open your VS Code and select **Source Control** in the left sidebar

2. Copy this URL `https://github.com/databrix-org/demo-databrix.org-yuqiang`

3. Click the **...** on the top of Menu (Views and More actions) --> Select **Clone**

4. Select **Clone from Github** in the search box

5. Paste URL into the search box and Select the Repo showed.

9. Clone it into a directory, where you want to store these scripts

## Step 2: Install packages

1. Open your Anaconda prompt

2. Open the directory of Repo in the Anaconda prompt, where you just stored scripts in it. Using `cd C:\user\repo`

3. create new conda environment. Run code `conda create -n databirx`

4. Activate the new environment named databrix. Run code `conda activate databrix`

5. Install required packages in this virtual environment. Run code: `conda install requirements.txt`

## Step 3: Run the frontend and backend Server

1. Open your Anaconda prompt. Then open the directory of Repo in your Anaconda prompt. Using `cd C:\user\repo`

2. activate the new environment named databrix. Run code `conda activate databrix`

3. Run the backend Server. Run code: `uvicorn backend_main:app --reload`

3. Do not close this Anaconda prompt and Open another Anaconda prompt

4. Open the directory of Repo in second Anaconda prompt. Using `cd C:\user\repo`

5. Activate the new environment named databrix. Run code `conda activate databrix`

5. Run the frontend Server. Run code: `streamlit run Homepage.py`
