🔐 Phishing Website Detection using Machine Learning & Streamlit


Author: Satyam Pandey
College: MLK PG College
Domain: Cybersecurity, Machine Learning
Status: ✅ Completed

📌 Project Description
This project is an AI-powered phishing website detector that uses machine learning models to identify potentially dangerous websites based on their URL structure and characteristics. It provides a real-time prediction interface built with Streamlit and is designed for educational, demonstrative, and research purposes in digital forensics and cybersecurity.

🚀 Features
✅ Trained ML Model (Random Forest Classifier)

🧠 Real-time phishing detection based on URL features

💻 Streamlit web app for interactive predictions

📊 Evaluation report: Accuracy, Precision, Recall, F1 Score

🧪 Synthetic phishing dataset

🗃️ Well-organized folder structure (dataset, models, app)

🛠️ Technologies Used
Tool	Purpose
Python	Programming
Scikit-learn	ML Model
Streamlit	Web Interface
Pandas, NumPy	Data Handling
Joblib	Model Serialization

📁 Folder Structure
Copy
Edit
📦 Phishing-Website-Detection
├── app
│   ├── app.py
│   └── utils.py
├── models
│   └── phishing_model.pkl
├── dataset
│   └── phishing.csv
├── README.md
├── requirements.txt
🧪 Sample Features Used
URL Length

Use of HTTPS

Contains IP Address

Number of Dots in URL

Use of Prefix/Suffix (like -)

📈 Model Performance
Accuracy: ~89%

Precision: ~90%

Recall: ~88%

F1 Score: ~89%

(Note: Metrics based on synthetic data. Use real datasets for production use.)

🔧 How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/Hackersatyampandey/Phishing-Website-Detection-using-Machine-Learning-Streamlit.git
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Launch the app:

bash
Copy
Edit
streamlit run app/app.py
📄 License
This project is licensed under the MIT License.

Let me know if you want me to auto-push this content to your GitHub repo as a new README.md.







You said:
more advanced 


ChatGPT said:
Satyam Bhaiya, yahaan main aapke GitHub repository ke liye ek super advanced, professional-level README.md de raha hoon jo interview, portfolio, ya even publication-level presentation ke liye bhi best hai. Ye version detailed, formatted, aur modern style mein likha gaya hai.

markdown
Copy
Edit
# 🔐 Phishing Website Detection using Machine Learning & Streamlit

> 🚀 **Author**: Satyam Pandey  
> 🎓 **College**: MLK PG College  
> 📁 **Domain**: Cybersecurity | Machine Learning | Digital Forensics  
> 🧠 **Status**: Completed | Interview-Ready | Deployed Locally

---

## 🧾 About the Project

Phishing websites trick users into revealing sensitive information such as passwords, credit card numbers, or personal data. This project provides a **machine learning-based solution** to detect such websites by analyzing key URL features. The model is trained on a synthetic phishing dataset and integrated into an **interactive web interface** using **Streamlit**, offering real-time predictions.

This project demonstrates how AI can be applied in **cybercrime prevention** and **digital investigation**, and is ideal for showcasing technical, analytical, and deployment skills in interviews and portfolios.

---

## 🔍 Key Highlights

- ✅ **Trained ML model** (Random Forest Classifier) for phishing detection
- 🌐 **Streamlit-based real-time interface** for prediction
- 📊 **Performance metrics included**: Accuracy, Precision, Recall, F1 Score
- 💾 Preprocessed synthetic dataset & serialized model (`.pkl`)
- 📁 Professional folder structure (for clean and scalable code)
- 🔐 Demonstrates cybersecurity awareness & data analysis skills

---

## 🧠 Features Extracted from URL

| Feature            | Description                                  |
|--------------------|----------------------------------------------|
| URL Length         | Total characters in the URL                  |
| Has HTTPS          | Presence of secure protocol (`https://`)     |
| Contains IP        | Whether an IP address is used in the domain  |
| Number of Dots     | Suspicious links often contain many dots     |
| Prefix/Suffix Use  | Usage of `-` in domain like `paypal-login.com` |

---

## ⚙️ Technologies Used

- `Python` – Core development
- `scikit-learn` – Machine learning pipeline
- `Streamlit` – Frontend web interface
- `pandas` / `numpy` – Data preprocessing
- `joblib` – Model serialization
- `matplotlib` / `seaborn` *(optional)* – Visualization

---

## 🗂️ Project Structure

Phishing-Website-Detection/
│
├── app/
│ └── app.py ← Streamlit web interface
│
├── models/
│ └── phishing_model.pkl ← Trained ML model
│
├── dataset/
│ └── phishing.csv ← Dataset (synthetic demo)
│
├── requirements.txt ← Required libraries
└── README.md ← Project documentation

yaml
Copy
Edit

---

## 📈 Model Performance (on synthetic data)

| Metric     | Value   |
|------------|---------|
| Accuracy   | ~89%    |
| Precision  | ~90%    |
| Recall     | ~88%    |
| F1 Score   | ~89%    |

> ⚠️ *Note: Performance can improve with real-world datasets like PhishTank, UCI, etc.*

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Hackersatyampandey/Phishing-Website-Detection-using-Machine-Learning-Streamlit.git
   cd Phishing-Website-Detection-using-Machine-Learning-Streamlit
Install required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Launch the Streamlit web app:

bash
Copy
Edit
streamlit run app/app.py
🎯 Use Cases
✅ Educational Project (BCA, B.Tech, Cybersecurity Courses)

✅ Resume/Portfolio Showcase

✅ AI + Web App Demonstration

✅ Cybersecurity Research/Presentation

📬 Contact / Credits
Developer: Satyam Pandey
Institution: MLK PG College
Email: hackersatyampandey@gmail.com

📜 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute with credit.


