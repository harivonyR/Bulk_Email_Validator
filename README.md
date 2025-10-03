# How to build a bulk email validator

This project is a Bulk Email Verifier powered by the Piloterr API.
It allows you to **check whether email addresses exist** and are valid.

The script takes a list of emails as input and returns a DataFrame (or CSV) with the verification status for each address.
---

## Use case 

+ Boost the effectiveness of marketing campaigns
+ Prevent domain blacklisting and protect sender reputation
+ Improve email deliverability and reduce bounce rates
+ Optimize costs by avoiding invalid recipients

---

## Requirements
 
External dependencies must be installed with `pip`:

```bash
pip install requests
```

---

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/harivonyR/Bulk_Email_Validator
```

### 2. Open the project folder
```bash
cd Bulk_Email_Validator
```

### 3. Create your credential file
Copy the example file:
```bash
copy credential.example.py credential.py
```

Open `credential.py` and paste your **PILOTERR API KEY**:
```python
x_api_key = "paste your API key here !"
```

### 4. Install dependencies
```bash
pip install requests
```

### 5. Run the scraper
```bash
python main.py
```

---