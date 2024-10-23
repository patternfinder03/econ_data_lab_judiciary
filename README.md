# econ_data_lab_judiciary

### Description
This project automates YouTube video commenting using Selenium in Python. It currently requires manual setup for Gmail and Chrome profiles.

### Prerequisites
1. **Anaconda**: Make sure you have Anaconda installed.
2. **Python**: Ensure Python is installed via Anaconda.
3. **Selenium**: This project relies on Selenium for browser automation.

Install Selenium using:
pip install selenium

### Setup Instructions

1. Clone the repository:
git clone https://github.com/patternfinder03/econ_data_lab_judiciary.git
cd yourrepo

2. Create a new Anaconda environment:
conda create --name myenv python=3.9
conda activate myenv

3. Install the required dependencies:
pip install selenium

4. Navigate to the `src` folder:
cd src

5. Generate Chrome path:
python make_chrome_path.py

6. Important: 
   - Create a new Gmail account.
   - Log in to this new account on your own Chrome profile.

### Running the Script

1. Open `comment.py` and edit the bottom section to specify the YouTube video link you want to comment on.

2. Run the script to post a comment:
python comment.py

### Notes
- You will need to manually adjust the script to select the YouTube video for commenting.
