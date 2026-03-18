# 🌐 Browser History Simulator

A web-based simulation of a browser's history navigation system using the **Stack Data Structure (LIFO)**.
This project demonstrates how real-world browsers implement **BACK** and **NEXT** functionality efficiently.

---

## 🚀 Live Demo

🔗 https://browser-history-simulator.onrender.com/

---

## 📌 Features

* 🔗 Visit new URLs
* ⬅ Navigate BACK through history
* ➡ Navigate NEXT through history
* 🔄 Reset browsing session
* 📜 Visual representation of Back & Forward stacks
* 📱 Fully responsive modern UI

---

## 🧠 Core Concept

This project is based on the **Stack (Last In First Out - LIFO)** data structure.

### How it works:

* **Back Stack** → Stores previously visited pages
* **Forward Stack** → Stores pages when navigating backward
* Visiting a new page clears the forward stack

This mimics the behavior of real browsers like Chrome or Edge.

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
* **Deployment:** Render
* **Data Structure Used:** Stack (LIFO)

---

## 📂 Project Structure

```
browser-history-simulator/
│
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/iitmkushal2506/browser-history-simulator.git
cd browser-history-simulator
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 🎯 Purpose of the Project

* To understand practical applications of **Stack Data Structure**
* To simulate real-world browser navigation systems
* To bridge the gap between **theory (DSA)** and **real-world implementation**
* To build a **full-stack mini project** using Flask

---

## 💡 Future Improvements

* Add URL validation
* Add animations & transitions
* Store history using database
* Multi-tab simulation
* User authentication

---

## 👨‍💻 Author

**Kushal Batra**

🔗 https://github.com/iitmkushal2506

---

## ⭐ Acknowledgement

This project was built as part of a **Data Structures assignment** to demonstrate real-world use of stacks in browser navigation systems.

---

## 📜 License

This project is open-source and available for learning purposes.
