# Accuknox Assignment

## Overview
This project contains solutions for the **Accuknox Django Assignment**:

1. **Django Signals**
   - Are signals synchronous or asynchronous?  
   - Do signals run in the same thread as the caller?  
   - Do signals run in the same database transaction as the caller?  

2. **Python Custom Class**
   - `Rectangle` class which supports iteration  
   - Iteration outputs `{'length': value}` followed by `{'width': value}`  

---

## Setup Instructions
```bash
git clone https://github.com/<your-username>/accuknox_assignment.git
cd accuknox_assignment
python -m venv venv
venv\Scripts\activate   # (Windows)
python manage.py makemigrations 
python manage.py migrate
pip install -r requirements.txt
python manage.py runserver
python rectangle.py → To run the rectangle file
```
---
## To run the rectangle file
```bash
python rectangle.py
```
---

## Django Signals Testing

http://127.0.0.1:8000/test-signal/  → Proves signals run synchronously

http://127.0.0.1:8000/test-thread/  → Proves signals run in the same thread

http://127.0.0.1:8000/test-transaction/  → Proves signals run in the same transaction

✅ Console logs will clearly show the proof.

--- 

## Author

👤 Gayathri S.

🔗 [GitHub](https://github.com/Gayathrisathiyarajan/accuknox_assignment)

