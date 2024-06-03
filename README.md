---
title: Spam Email Detection
emoji: 💌
colorFrom: pink
colorTo: blue
sdk: gradio
sdk_version: 3.17.0
app_file: app.py
---

# Email Spam and Phishing URL Detection

This project utilizes Naive Bayes classification to detect whether an email is spam or not, and XGBoost classification to determine if a URL within an email is phishing or legitimate.

# Getting Started
## Project Overview

The project consists of two main components:

1. **Email Spam Detection**: This component employs Naive Bayes classification to classify emails as either spam or not spam based on their content features.

2. **Phishing URL Detection**: This component uses XGBoost classification to identify whether URLs within emails are associated with phishing attempts or legitimate websites.

## Prerequisites
Make sure you have Python 3.10 installed on your system. You can download it from [](python.org)

## Requirements
Ensure you have the following dependencies installed. You can install them using `pip install -r requirements.txt`.

- gunicorn==22.0.0
- python-dateutil==2.8.2
- gradio==4.32.1
- gradio_client==0.17.0
- requests==2.31.0
- beautifulsoup4==4.12.3
- googlesearch_python==1.2.4
- urlextract==1.9.0
- numpy==1.26.3
- pandas==2.2.0
- scikit-learn==1.5.0
- urllib3==2.1.0
- python-whois==0.9.4
- xgboost==2.0.3
- lxml==5.2.2

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/email-spam-phishing-detection.git
   cd email-spam-phishing-detection

2. Install dependencies:
   ```bash
   pip install -r requirements.txt```
   
## Usage
1. **Data Preparation:**
   - Ensure the datasets `spam.csv` and `urldata.csv` are available in the `data/` directory.

2. **Model Training:**
   - If necessary, modify and run the `notebook.ipynb` Jupyter notebook to train or fine-tune the machine learning models.
   - Trained models will be saved in the `models/` directory.

3. **Run the Application:**
   - Execute `app.py` to start the application.
   - Access the application at [Hugging Face Space](https://huggingface.co/spaces/akshatsanghvi/spam-email-detection)

## Acknowledgements

- The email spam classification model is trained using the `spam.csv` dataset, sourced from [Dataset: Spam/ham mail](https://www.kaggle.com/datasets/mfaisalqureshi/spam-email?resource=download)).
- The URL phishing detection model is trained using the `urldata.csv` dataset, sourced from [Phishing Websites Dataset](https://www.kaggle.com/datasets).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

