# Spam Email Classifier

A full-stack AI application that detects whether an email is Spam or Not Spam using Machine Learning.

## Features

- Spam email detection
- Machine Learning powered classification
- FastAPI backend
- TF-IDF vectorization
- SGDClassifier based binary classification
- REST API integration

---

## Tech Stack

### Backend
- FastAPI
- Python

### Machine Learning
- TF-IDF Vectorizer
- SGDClassifier

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd spam-email-classifier
```

---

## Backend Setup

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

API will run on:

```plaintext
http://127.0.0.1:8000
```

Swagger Docs:

```plaintext
http://127.0.0.1:8000/docs
```

---

## Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Train/Test Split
4. TF-IDF Vectorization
5. Model Training
6. Evaluation
7. API Integration

---

## Model Performance

- Accuracy: ~98%
- F1 Score: ~0.99