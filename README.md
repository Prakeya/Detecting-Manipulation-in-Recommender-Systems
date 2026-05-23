# Detecting-Manipulation-in-Recommender-Systems

A Jacobian-based framework for detecting manipulation and hidden bias in recommender systems. The project analyzes how small input changes affect recommendations using Jacobian sensitivity analysis and SVD spectral distortion, helping identify abnormal influence patterns and unfair recommendation behavior.

## Project Structure

- `app.py`: Flask application for the manipulation detector.
- `templates/index.html`: Web interface for the detector.
- `A17_Report.pdf`: Detailed project report.
- `Detecting-Manipulation-in-Recommender-Systems.pdf`: Project presentation.
- `requirements.txt`: Python dependencies.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Data Requirement**:
   The app requires `ratings.csv` and `movies.csv` (MovieLens format) in the root directory to function. Please ensure these files are present before running the app.

3. Run the application:
   ```bash
   python app.py
   ```

## Methodology

The detector uses spectral methods and Jacobian-based sensitivity analysis to identify if a user's recommendations have been significantly distorted by malicious injections in the rating matrix.
