@echo off
echo 🔧 Setting up Top 10 Crypto Analyzer...

:: Step 1: Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

:: Step 2: Activate virtual environment
echo ⚙️ Activating virtual environment...
call venv\Scripts\activate

:: Step 3: Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

:: Step 4: Install required packages
echo 📚 Installing required Python packages...
pip install -r requirements.txt

:: Step 5: Run the main pipeline
echo 🚀 Running main.py...
python main.py

:: Step 6: Done
echo ✅ Setup and pipeline run complete!
pause
