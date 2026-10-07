
# Amazon Review Sentiment Analysis

## 📌 Project Overview

This project is an **Amazon Review Sentiment Analysis System** that automatically classifies customer reviews into three sentiment categories:

* Negative
* Neutral
* Positive

The project explores and compares **Machine Learning, Deep Learning, and Transformer-based NLP models**. The selected Logistic Regression model is integrated into a Streamlit web application for real-time sentiment prediction.

---

## 🎯 Business Problem

E-commerce companies receive a large number of customer reviews every day.

Manually analyzing these reviews is time-consuming and difficult. An automated sentiment analysis system can help businesses understand customer opinions at scale.

### Business Benefits

* Understand customer opinions
* Identify negative customer feedback
* Monitor customer satisfaction
* Analyze large volumes of reviews automatically
* Support data-driven business decisions
* Quickly identify areas requiring improvement

---

## 📊 Dataset

The project uses an **Amazon product review dataset** for sentiment classification.

The dataset contains customer review text and sentiment information prepared for a three-class classification problem.

### Dataset Classes

The sentiment labels were manually encoded as follows:

| Label | Sentiment |
| ----: | --------- |
|     0 | Negative  |
|     1 | Neutral   |
|     2 | Positive  |

The dataset used in the project is included as:

```text
dataset.xlsx
```

---

## 🧹 Text Preprocessing

The review text is processed using a custom `clean_text()` function.

The preprocessing step prepares raw customer reviews before they are passed to the machine learning model.

The **same preprocessing function used during model training is used during deployment** to ensure consistency between training data and new reviews.

### Preprocessing Pipeline

```text
Raw Review
     ↓
Text Cleaning
     ↓
Cleaned Review
     ↓
TF-IDF Vectorization
     ↓
Machine Learning Model
     ↓
Sentiment Prediction
```

The preprocessing function is stored separately in:

```text
preprocessing.py
```

---

## 🤖 Models Compared

Several Machine Learning, Deep Learning, and Transformer-based models were evaluated.

### Machine Learning Models

* Logistic Regression
* Linear SVM
* Naive Bayes

### Deep Learning Models

* Simple RNN
* LSTM

### Transformer Model

* DistilBERT

---

## 📈 Model Comparison

The following table shows the evaluation results obtained from the project.

| Model                   |   Accuracy |  Precision | Recall | F1 Macro |
| ----------------------- | ---------: | ---------: | -----: | -------: |
| **Logistic Regression** |     79.86% |     70.86% | 70.04% |**70.14%**|
| **Linear SVM**          | **81.60%** |     73.16% | 68.76% |   69.22% |
| **DistilBERT**          | **81.94%** | **73.81%** | 65.95% |   64.04% |
| **Naive Bayes**         |     78.47% |     54.18% | 59.97% |   56.49% |
| **Simple RNN**          |     50.69% |     16.90% | 33.33% |   22.43% |
| **LSTM**                |     50.69% |     16.90% | 33.33% |   22.43% |

### 🏆 Model Analysis

Based on the evaluation results:

* **DistilBERT achieved the highest accuracy: 81.94%**
* **Linear SVM achieved 81.60% accuracy**
* **Logistic Regression achieved 79.86% accuracy**
* DistilBERT also achieved the highest precision at **73.81%**
* Logistic Regression provides a strong balance between performance, simplicity, and computational requirements.
* Simple RNN and LSTM achieved significantly lower performance on this dataset.

### 🚀 Selected Deployment Model

Although DistilBERT achieved the highest overall accuracy, **Logistic Regression was selected for deployment** because it provides:

* Highest f1_macro    
* Fast prediction
* Lower computational requirements
* Simple deployment
* Efficient CPU execution
* Easy integration with TF-IDF
* Good classification performance

The deployed model consists of a **TF-IDF Vectorizer + Logistic Regression** pipeline.

---

## 🔗 Final Machine Learning Pipeline

The deployed pipeline works as follows:

```text
User enters Amazon Review
          ↓
     clean_text()
          ↓
     TF-IDF Vectorizer
          ↓
   Logistic Regression
          ↓
    Prediction: 0/1/2
          ↓
     Sentiment Mapping
          ↓
Negative / Neutral / Positive
```

---

## 🚀 Streamlit Application

The trained Logistic Regression pipeline is deployed using **Streamlit**.

The application allows users to enter an Amazon review and receive a sentiment prediction in real time.

### Application Workflow

1. User enters a review.
2. The review is passed through `clean_text()`.
3. The cleaned text is transformed using the saved TF-IDF vectorizer.
4. Logistic Regression predicts the sentiment class.
5. The numeric prediction is converted into the corresponding sentiment.
6. The result is displayed in the Streamlit application.

---

## 📁 Project Structure

```text
Sentiment_App/
│
├── app.py
│
├── preprocessing.py
│
├── lr_model.pkl
│
├── dataset.xlsx
│
├── requirements.txt
│
└── README.md
```

### File Description

| File                  | Description                                    |
| --------------------- | ---------------------------------------------- |
| `app.py`              | Streamlit web application                      |
| `preprocessing.py`    | Text preprocessing and `clean_text()` function |
| `sentiment_model.pkl` | Saved TF-IDF + Logistic Regression pipeline    |
| `dataset.xlsx`        | Amazon review dataset                          |
| `requirements.txt`    | Required Python packages                       |
| `README.md`           | Project documentation                          |

---

## ⚙️ Installation

### 1. Activate the Python Environment

If using Anaconda:

```bash
conda activate ml_env
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

Navigate to the project directory:

```bash
cd Amazon_Sentiment_App
```

Run:

```bash
streamlit run app.py
```

The Streamlit application will start and provide a local URL such as:

```text
http://localhost:8501
```

Open the URL in a web browser to use the application.

---

## 🧪 Example Predictions

### Positive Review

```text
I absolutely love this product! Amazing quality.
```

Expected sentiment:

```text
POSITIVE
```

### Negative Review

```text
Very bad product. I am disappointed with the quality.
```

Expected sentiment:

```text
NEGATIVE
```

### Neutral Review

```text
The product is okay and works as expected.
```

Expected sentiment:

```text
NEUTRAL
```

---

## 💾 Model Saving

The TF-IDF vectorizer and Logistic Regression model are combined into a single Scikit-learn Pipeline.

```python
from sklearn.pipeline import Pipeline

sentiment_pipeline = Pipeline([
    ("tfidf", tfidf),
    ("model", lr_model)
])
```

The trained pipeline is saved using Joblib:

```python
joblib.dump(sentiment_pipeline, "sentiment_model.pkl")
```

This allows the Streamlit application to load the trained model without retraining it.

---

## 🔄 Prediction on New Reviews

When a new review is entered into the Streamlit application:

```text
New Review
    ↓
clean_text()
    ↓
Saved TF-IDF
    ↓
Saved Logistic Regression
    ↓
0 / 1 / 2
    ↓
Sentiment
```

The model does **not** need to be trained again when making predictions.

---

## 📌 Important Note

The `clean_text()` function used during deployment should remain the **same as the function used during model training**.

Changing the preprocessing logic after training can cause differences between training data and new reviews and may affect prediction performance.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Natural Language Processing (NLP)
* TF-IDF
* Logistic Regression
* Linear SVM
* Naive Bayes
* Simple RNN
* LSTM
* DistilBERT
* Hugging Face Transformers
* PyTorch
* Streamlit
* Joblib
* Jupyter Notebook

---

## 🎓 Project Type

**Natural Language Processing (NLP) | Sentiment Analysis | Machine Learning | Deep Learning | Transformer | Streamlit Deployment**

---

## 👨‍💻 Conclusion

This project demonstrates how customer reviews can be automatically classified using different NLP and machine learning approaches.

The experiments show that Transformer-based DistilBERT achieved the highest accuracy, while Logistic Regression provided a strong and computationally efficient solution for deployment.

The final Streamlit application allows users to enter new Amazon reviews and receive real-time sentiment predictions.
