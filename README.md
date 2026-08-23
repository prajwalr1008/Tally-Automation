# Tally Automation using Python

A Python-based accounting automation project that integrates with **TallyPrime** through its HTTP/XML interface to automate repetitive accounting operations such as ledger processing, payment vouchers, receipt vouchers, and individual voucher creation.

The project demonstrates how structured accounting data from CSV files can be processed using Python and transmitted directly to TallyPrime.

---

## 🚀 Features

- Automate ledger creation and processing in TallyPrime
- Create Payment Vouchers using Python
- Create Receipt Vouchers using Python
- Create individual accounting vouchers
- Read transaction data from CSV files
- Convert accounting data into Tally XML requests
- Send XML requests to TallyPrime through HTTP
- Receive and process TallyPrime XML responses
- Validate TallyPrime responses for errors and exceptions
- Provide input validation and error handling
- Reduce repetitive manual accounting data entry

---

## 🏗️ Project Architecture

```text
CSV Input
    │
    ▼
Python Automation Script
    │
    ▼
XML Request Generation
    │
    ▼
TallyPrime HTTP Server
    │
    ▼
TallyPrime Company
    │
    ▼
XML Response
    │
    ▼
Response Validation & Error Handling
```

---

## 📁 Project Structure

```text
Tally-Automation/
│
├── ledger_creation.py
├── payment_vouchers.py
├── receipt_vouchers.py
├── single_voucher.py
│
├── Ledger_Creation.csv
├── payment_entries.csv
├── receipt_entries.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File | Description |
|---|---|
| `ledger_creation.py` | Automates ledger creation and processing in TallyPrime |
| `payment_vouchers.py` | Reads payment data from CSV and processes Payment Vouchers |
| `receipt_vouchers.py` | Reads receipt data from CSV and processes Receipt Vouchers |
| `single_voucher.py` | Creates an individual Payment Voucher directly through XML |
| `Ledger_Creation.csv` | Input data used for ledger processing |
| `payment_entries.csv` | Input data for Payment Vouchers |
| `receipt_entries.csv` | Input data for Receipt Vouchers |
| `requirements.txt` | Python dependencies required by the project |
| `.gitignore` | Specifies files and folders that should not be tracked by Git |
| `README.md` | Project documentation |

---

## ⚙️ Technologies Used

- **Python 3**
- **TallyPrime**
- **Tally XML / HTTP Interface**
- **Pandas**
- **Requests**
- **BeautifulSoup**
- **lxml**
- **CSV**
- **Git**
- **GitHub**

---

## 🔧 Prerequisites

Before running the automation:

1. Install Python 3.
2. Install TallyPrime.
3. Open the required company in TallyPrime.
4. Enable the TallyPrime HTTP server.
5. Ensure the TallyPrime HTTP server is running on:

```text
http://localhost:9000
```

6. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/prajwalr1008/Tally-Automation.git
```

Navigate to the project directory:

```bash
cd Tally-Automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure TallyPrime is running with the required company open and the HTTP server available at:

```text
http://localhost:9000
```

---

## 📊 CSV Input Format

### Payment Entries

The `payment_entries.csv` file follows this structure:

```csv
Date,Account Name,Ledger Name,Amount,Narration
20260401,Cash,Office Expenses,500,Being payment made for office expenses
```

### Receipt Entries

The `receipt_entries.csv` file follows this structure:

```csv
Date,Account Name,Ledger Name,Amount,Narration
20260401,Bank,Sales,1500,Being receipt received from customer
```

The CSV-based approach separates transaction data from the Python automation logic, allowing the scripts to process structured accounting entries.

---

## ▶️ How to Run

### 1. Ledger Creation

Run:

```bash
python ledger_creation.py
```

The script reads ledger information from:

```text
Ledger_Creation.csv
```

and sends the required XML request to TallyPrime for ledger processing.

The response is validated for errors and exceptions.

---

### 2. Payment Voucher Automation

Run:

```bash
python payment_vouchers.py
```

The script reads payment transactions from:

```text
payment_entries.csv
```

and sends them to TallyPrime as Payment Voucher XML requests.

The TallyPrime response is validated for successful processing and errors.

---

### 3. Receipt Voucher Automation

Run:

```bash
python receipt_vouchers.py
```

The script reads receipt transactions from:

```text
receipt_entries.csv
```

and creates Receipt Voucher requests for TallyPrime.

The response is validated for successful processing and errors.

---

### 4. Single Voucher Creation

Run:

```bash
python single_voucher.py
```

This script demonstrates the direct creation of an individual Payment Voucher through TallyPrime's XML interface.

The response is validated and reported to the user.

---

## 🔌 TallyPrime Integration

The project communicates with TallyPrime using HTTP requests.

The Python scripts send XML data to the local TallyPrime server:

```python
requests.post(
    "http://localhost:9000",
    data=xml_data.encode("utf-8"),
    headers={"Content-Type": "application/xml"}
)
```

The accounting transaction is converted into a Tally-compatible XML request and submitted to TallyPrime.

TallyPrime then returns an XML response containing information such as:

- Created transactions
- Altered transactions
- Deleted transactions
- Ignored transactions
- Errors
- Exceptions

The Python scripts process these responses and provide a summary of the result.

---

## 🧾 Example Payment Transaction

A payment transaction can be represented as:

```text
Date:          01-Apr-2026
Account:       Cash
Ledger:        Office Expenses
Amount:        ₹500
Narration:     Being payment made for office expenses
```

The Python script converts this structured data into a Tally-compatible XML request.

---

## 🧾 Example Receipt Transaction

A receipt transaction can be represented as:

```text
Date:          01-Apr-2026
Account:       Bank
Ledger:        Sales
Amount:        ₹1,500
Narration:     Being receipt received from customer
```

The Python script converts the transaction into XML and submits it to TallyPrime.

---

## 🛠️ Validation & Error Handling

The project validates input data and processes TallyPrime's XML response to identify whether a transaction was successfully processed.

A typical successful TallyPrime response can contain:

```xml
<RESPONSE>
    <CREATED>1</CREATED>
    <ALTERED>0</ALTERED>
    <ERRORS>0</ERRORS>
    <EXCEPTIONS>0</EXCEPTIONS>
</RESPONSE>
```

If TallyPrime rejects a transaction, the response can provide error information that can be used to identify and correct the underlying issue.

The automation scripts provide user-friendly processing summaries including:

```text
Created
Altered
Deleted
Errors
Successful
Failed
```

This allows users to identify processing issues without manually inspecting the complete XML response.

---

## ✅ Testing

The automation was tested with a running TallyPrime company.

Test execution included:

- Ledger processing
- Payment Voucher processing
- Receipt Voucher processing
- Individual Payment Voucher processing

The tested scripts successfully connected to the TallyPrime HTTP server and received XML responses without reported errors.

The scripts provide processing summaries showing the number of transactions processed, successful operations, and failures.

> **Note:** The exact Created, Altered, Deleted, and Error counts depend on the state of the target TallyPrime company and the transaction being processed.

---

## 💡 Business Use Case

Accounting professionals frequently perform repetitive data-entry activities involving ledgers, payments, receipts, and other accounting transactions.

This project demonstrates how Python automation can connect accounting workflows with TallyPrime to:

- Reduce repetitive manual data entry
- Improve consistency
- Process structured accounting data
- Automate routine voucher processing
- Integrate accounting software with Python
- Provide a foundation for larger accounting automation solutions

---

## 📚 Learning Outcomes

This project demonstrates practical experience in:

- Python automation
- Accounting process automation
- TallyPrime integration
- XML-based API communication
- HTTP requests
- CSV data processing
- Pandas
- Input validation
- Error handling
- Git and GitHub
- Finance and accounting workflow automation

---

## 🔮 Future Enhancements

Potential future improvements include:

- Automatic voucher date validation
- Batch voucher processing
- Excel input support
- Automated ledger creation from transaction files
- Duplicate transaction detection
- Advanced error logging
- Pre-submission transaction validation
- GUI interface for non-technical users
- Tally response dashboard
- Automated bank reconciliation
- GST-related transaction automation
- Automated accounting reports

---

## ⚠️ Limitations

- TallyPrime must be installed and running locally.
- The required TallyPrime company must be open and accessible.
- The TallyPrime HTTP server must be available at `localhost:9000`.
- Ledger names and accounting data must correspond to the target TallyPrime company.
- The project is currently designed for local TallyPrime automation rather than cloud-based execution.

---

## 👨‍💻 Author

**Prajwal R**

B.Com (Hons) – International Accounting & Finance  
ACCA Finalist | CA Intermediate

GitHub: [@prajwalr1008](https://github.com/prajwalr1008)
