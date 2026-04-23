# jeffin_finaltest_2304_p2
Jeffin Francis, This is the Version control for the final test

Jeffin Francis: here are the instructions for the final
test repository.

This app.py is used for python code for the web app.
This Index.html is used the template for the web app.

# 🍽️ Restaurant Staff Management Project

## 📌 Overview

This project demonstrates a simple object-oriented design in Python to model different roles in a restaurant: **Server**, **Team Leader**, and **Manager**. Each role builds on the previous one using inheritance, allowing us to reuse code and clearly represent increasing responsibilities.

---

## 🧠 Reflection

While working on this project, I learned how powerful **inheritance** is in reducing repetition and improving code organization. Instead of rewriting similar attributes and methods for each role, I was able to extend the base `Server` class and gradually add more responsibilities.

One key takeaway was understanding how `super()` works. It allows constructors to chain together so that each class contributes to building the final object. This made it clear how a `Manager` ends up with all duties from `Server` and `TeamLeader`.

I also noticed small details like extra spaces when splitting strings, which reminded me that even simple operations can affect output quality. Overall, this project improved my understanding of class relationships and clean design.

---

## ⚙️ Instructions to Run

1. Make sure you have Python installed (Python 3 recommended).
2. Clone this repository:

   ```
   git clone https://github.com/jfran123/jeffin_finaltest_2304_p2.git
   ```
3. Navigate into the project folder:

   ```
   cd <project-folder>
   ```
4. Run the Python file:

   ```
   python app.py
   ```

---

## 📁 Project Files

* `app.py`
  This app.py is used for python code for the web app.

* `index.html`
  This file is used as a basic template for the web interface.

* `README.md`
  Contains project documentation, reflection, and instructions.

---

## 🧱 Class Structure

### 1. Server

* Base class
* Stores name and basic duties
* Provides a string representation of responsibilities

### 2. TeamLeader

* Inherits from Server
* Adds leadership responsibilities like:

  * Checking attendance
  * Assigning duties

### 3. Manager

* Inherits from TeamLeader
* Adds administrative responsibilities like:

  * Creating schedules
  * Hiring staff

---

## ▶️ Example Usage

```python
m = Manager("Alice")
print(m)
```

Output:

```
My name is Jeffin and I am responsible for:
['clear tables', ' mop the floor', ' take payment', ' serve customer',
 'check attendance', ' assign duty',
 'create schedule', ' hire staff']
```

---

## 🚀 Future Improvements

* Clean up spacing in duties using `.strip()`
* Add a graphical or web interface
* Store employee data dynamically (e.g., using a database)
* Introduce roles like Chef or Host for a more complete system

---


