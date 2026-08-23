\# Tally Automation using Python



A Python-based accounting automation project that integrates with \*\*TallyPrime\*\* through its HTTP/XML interface to automate repetitive accounting operations such as ledger processing, payment vouchers, receipt vouchers, and individual voucher creation.



The project demonstrates how structured accounting data from CSV files can be processed using Python and transmitted directly to TallyPrime.



\---



\## 🚀 Features



\- Automate ledger creation and processing in TallyPrime

\- Create Payment Vouchers using Python

\- Create Receipt Vouchers using Python

\- Create individual accounting vouchers

\- Read transaction data from CSV files

\- Convert accounting data into Tally XML requests

\- Send XML requests to TallyPrime through HTTP

\- Receive and process TallyPrime XML responses

\- Validate successful transaction creation using TallyPrime response codes

\- Reduce repetitive manual accounting data entry



\---



\## 🏗️ Project Architecture



```text

CSV Input

&#x20;   │

&#x20;   ▼

Python Automation Script

&#x20;   │

&#x20;   ▼

XML Request Generation

&#x20;   │

&#x20;   ▼

TallyPrime HTTP Server

&#x20;   │

&#x20;   ▼

TallyPrime Company

&#x20;   │

&#x20;   ▼

XML Response

&#x20;   │

&#x20;   ▼

Python Response Handling

```



\---



\## 📁 Project Structure



```text

Tally-Automation/

│

├── ledger\_creation.py

├── payment\_vouchers.py

├── receipt\_vouchers.py

├── single\_voucher.py

│

├── Ledger\_Creation.csv

├── payment\_entries.csv

├── receipt\_entries.csv

│

├── README.md

└── .gitignore

```



\### File Description



| File | Description |

|---|---|

| `ledger\_creation.py` | Automates ledger creation and processing in TallyPrime |

| `payment\_vouchers.py` | Reads payment data from CSV and creates Payment Vouchers |

| `receipt\_vouchers.py` | Reads receipt data from CSV and creates Receipt Vouchers |

| `single\_voucher.py` | Creates an individual Payment Voucher directly through XML |

| `Ledger\_Creation.csv` | Input data used for ledger processing |

| `payment\_entries.csv` | Input data for Payment Vouchers |

| `receipt\_entries.csv` | Input data for Receipt Vouchers |

| `.gitignore` | Specifies files and folders that should not be tracked by Git |

| `README.md` | Project documentation |



\---



\## ⚙️ Technologies Used



\- \*\*Python 3\*\*

\- \*\*TallyPrime\*\*

\- \*\*Tally XML / HTTP Interface\*\*

\- \*\*Pandas\*\*

\- \*\*Requests\*\*

\- \*\*BeautifulSoup\*\*

\- \*\*lxml\*\*

\- \*\*CSV\*\*

\- \*\*Git\*\*

\- \*\*GitHub\*\*



\---



\## 🔧 Prerequisites



Before running the automation:



1\. Install Python 3.

2\. Install TallyPrime.

3\. Open the required company in TallyPrime.

4\. Enable TallyPrime's HTTP server.

5\. Ensure the TallyPrime HTTP server is running on:



```text

http://localhost:9000

```



6\. Install the required Python libraries:



```bash

pip install pandas requests beautifulsoup4 lxml

```



\---



\## 📊 CSV Input Format



\### Payment Entries



The `payment\_entries.csv` file follows this structure:



```csv

Date,Account Name,Ledger Name,Amount,Narration

20260401,Cash,Office Expenses,500,Being payment made for office expenses

```



\### Receipt Entries



The `receipt\_entries.csv` file follows this structure:



```csv

Date,Account Name,Ledger Name,Amount,Narration

20260401,Bank,Sales,1500,Being receipt received from customer

```



The CSV-based approach separates transaction data from the Python automation logic, allowing the scripts to process structured accounting entries.



\---



\## ▶️ How to Run



\### 1. Ledger Creation



Run:



```bash

python ledger\_creation.py

```



The script sends the required XML request to TallyPrime for ledger processing.



A successful response contains:



```xml

<ERRORS>0</ERRORS>

```



\---



\### 2. Payment Voucher Automation



Run:



```bash

python payment\_vouchers.py

```



The script reads payment transactions from:



```text

payment\_entries.csv

```



and sends them to TallyPrime as Payment Voucher XML requests.



A successful transaction returns:



```xml

<CREATED>1</CREATED>

<ERRORS>0</ERRORS>

```



\---



\### 3. Receipt Voucher Automation



Run:



```bash

python receipt\_vouchers.py

```



The script reads receipt transactions from:



```text

receipt\_entries.csv

```



and creates Receipt Vouchers in TallyPrime.



A successful transaction returns:



```xml

<CREATED>1</CREATED>

<ERRORS>0</ERRORS>

```



\---



\### 4. Single Voucher Creation



Run:



```bash

python single\_voucher.py

```



This script demonstrates the direct creation of an individual Payment Voucher through TallyPrime's XML interface.



A successful response returns:



```xml

<CREATED>1</CREATED>

<ERRORS>0</ERRORS>

```



\---



\## 🔌 TallyPrime Integration



The project communicates with TallyPrime using HTTP requests.



The Python scripts send XML data to the local TallyPrime server:



```python

requests.post(

&#x20;   "http://localhost:9000",

&#x20;   data=xml\_data.encode("utf-8"),

&#x20;   headers={"Content-Type": "application/xml"}

)

```



The accounting transaction is converted into an XML request and submitted to TallyPrime.



TallyPrime then returns an XML response containing information such as:



\- Created transactions

\- Altered transactions

\- Deleted transactions

\- Ignored transactions

\- Errors

\- Exceptions



\---



\## 🧾 Example Payment Transaction



A payment transaction can be represented as:



```text

Date:          01-Apr-2026

Account:       Cash

Ledger:        Office Expenses

Amount:        ₹500

Narration:     Being payment made for office expenses

```



The Python script converts this structured data into a Tally-compatible XML request.



\---



\## 🧾 Example Receipt Transaction



A receipt transaction can be represented as:



```text

Date:          01-Apr-2026

Account:       Bank

Ledger:        Sales

Amount:        ₹1,500

Narration:     Being receipt received from customer

```



The Python script converts the transaction into XML and submits it to TallyPrime.



\---



\## ✅ Testing



The automation was tested with a running TallyPrime company.



Successful tests included:



\- Ledger processing

\- Payment Voucher creation

\- Receipt Voucher creation

\- Individual Payment Voucher creation



Successful voucher creation returned:



```text

CREATED: 1

ERRORS: 0

EXCEPTIONS: 0

```



The project also handles TallyPrime validation errors, such as invalid voucher dates and missing ledgers, through the XML response returned by TallyPrime.



\---



\## 💡 Business Use Case



Accounting professionals frequently perform repetitive data-entry activities involving ledgers, payments, receipts, and other accounting transactions.



This project demonstrates how Python automation can connect accounting workflows with TallyPrime to:



\- Reduce repetitive manual data entry

\- Improve consistency

\- Process structured accounting data

\- Automate routine voucher creation

\- Integrate accounting software with Python

\- Provide a foundation for larger accounting automation solutions



\---



\## 📚 Learning Outcomes



This project demonstrates practical experience in:



\- Python automation

\- Accounting process automation

\- TallyPrime integration

\- XML-based API communication

\- HTTP requests

\- CSV data processing

\- Pandas

\- Error handling

\- Git and GitHub

\- Finance and accounting workflow automation



\---



\## 🔮 Future Enhancements



Potential future improvements include:



\- Automatic voucher date validation

\- Batch voucher processing

\- Excel input support

\- Automated ledger creation from transaction files

\- Duplicate transaction detection

\- Advanced error logging

\- Pre-submission transaction validation

\- GUI interface for non-technical users

\- Tally response dashboard

\- Automated bank reconciliation

\- GST-related transaction automation

\- Automated accounting reports



\---



\## 🛠️ Error Handling



The project uses TallyPrime's XML response to identify whether a transaction was successfully processed.



Example successful response:



```xml

<RESPONSE>

&#x20;   <CREATED>1</CREATED>

&#x20;   <ALTERED>0</ALTERED>

&#x20;   <ERRORS>0</ERRORS>

&#x20;   <EXCEPTIONS>0</EXCEPTIONS>

</RESPONSE>

```



If TallyPrime rejects a transaction, the response provides an error message that can be used to identify and correct the underlying issue.



\---



\## 👨‍💻 Author



\*\*Prajwal R\*\*



B.Com (Hons) – International Accounting \& Finance  

ACCA Finalist | CA Intermediate



GitHub: \[@prajwalr1008](https://github.com/prajwalr1008)



\---



\## ⭐ Project



If you find this project useful, consider giving the repository a ⭐ on GitHub.

