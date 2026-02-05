# MiniProject 2 - Finger ERP Analysis

## What This Project Does
This project analyzes brain signals related to finger movements. It calculates the average brain response (ERP - Event Related Potential) for each of the 5 fingers.

## Files Included
1. **fingers_erp.py** - Contains the main function `calc_mean_erp`
2. **main.py** - Runs the function and displays results
3. **README.md** - This file with instructions

## How to Use

### Step 1: Prepare Your Files
Make sure you have these data files in the same folder:
- `events_file_ordered.csv` (finger movement events)
- `brain_data_channel_one.csv` (brain signal data)

### Step 2: Run the Code
Open your terminal/command prompt and run:
```
python main.py
```

### What Happens
1. The function loads both CSV files
2. For each finger (1-5), it:
   - Finds all trials where that finger moved
   - Extracts brain data from 200ms before to 1000ms after each movement
   - Averages across all trials for that finger
3. Creates a plot showing the brain response for each finger
4. Returns a 5x1201 matrix with the results

## Understanding the Code

### The Function Structure
```python
def calc_mean_erp(trial_points, ecog_data):
    # 1. Load data
    # 2. Create empty result matrix (5 fingers x 1201 time points)
    # 3. For each finger:
    #    - Find all trials
    #    - Extract brain segments
    #    - Calculate average
    # 4. Plot results
    # 5. Return matrix
```

### Key Concepts
- **1201 time points**: 200 before + 1 at start + 1000 after = 1201 total
- **5 fingers**: Each row in the output represents one finger (1-5)
- **Averaging**: Multiple trials are averaged to get a cleaner signal

## Expected Output
- A plot showing 5 lines (one per finger)
- A 5x1201 matrix stored in `fingers_erp_mean`
- Console output showing the shape and statistics

## Tips for Beginners
- Make sure numpy and matplotlib are installed: `pip install numpy matplotlib`
- Keep all files in the same folder
- If you get an error, check that the CSV file names match exactly
- The plot window might need to be closed before the program finishes

## Questions?
If something doesn't work:
1. Check that your CSV files are in the correct location
2. Make sure you have the required packages installed
3. Look at the error message - it usually tells you what's wrong!
