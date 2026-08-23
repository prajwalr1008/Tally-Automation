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

\- Validate TallyPrime responses for errors and exceptions

\- Provide input validation and error handling

\- Reduce repetitive manual accounting data entry



\---



\## 🏗️ Project Architecture



CSV Input

&#x20;   |

&#x20;   v

Python Automation Script

&#x20;   |

&#x20;   v

XML Request Generation

&#x20;   |

&#x20;   v

TallyPrime HTTP Server

&#x20;   |

&#x20;   v

TallyPrime Company

&#x20;   |

&#x20;   v

XML Response

&#x20;   |

&#x20;   v

Response Validation \& Error Handling



\---



\## 📁 Project Structure



Tally-Automation/

|

├── ledger\_creation.py

├── payment\_vouchers.py

├── receipt\_vouchers.py

├── single\_voucher.py

|

├── Ledger\_Creation.csv

├── payment\_entries.csv

├── receipt\_entries.csv

|

├── README.md

└── .gitignore



\### File Description



| File | Description |

|---|---|

| `ledger\_creation.py` | Automates ledger creation and processing in TallyPrime |

| `payment\_vouchers.py` | Reads payment data from CSV and processes Payment Vouchers |

| `receipt\_vouchers.py` | Reads receipt data from CSV and processes Receipt Vouchers |

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

4\. Enable the TallyPrime HTTP server.

5\. Ensure the TallyPrime HTTP server is running on:



`http://localhost:9000`



6\. Install the required Python libraries:



`pip install pandas requests beautifulsoup4 lxml`



\---



\## 📊 CSV Input Format



\### Payment Entries



The `payment\_entries.csv` file follows this structure:



Date,Account Name,Ledger Name,Amount,Narration

20260401,Cash,Office Expenses,500,Being payment made for office expenses



\### Receipt Entries



The `receipt\_entries.csv` file follows this structure:



Date,Account Name,Ledger Name,Amount,Narration

20260401,Bank,Sales,1500,Being receipt received from customer



The CSV-based approach separates transaction data from the Python automation logic, allowing the scripts to process structured accounting entries.



\---



\## ▶️ How to Run



\### 1. Ledger Creation



Run:



`python ledger\_creation.py`



The script reads ledger information from `Ledger\_Creation.csv` and sends the required XML request to TallyPrime for ledger processing.



The response is validated for errors and exceptions.



\### 2. Payment Voucher Automation



Run:



`python payment\_vouchers.py`



The script reads payment transactions from `payment\_entries.csv` and sends them to TallyPrime as Payment Voucher XML requests.



The TallyPrime response is validated for successful processing and errors.



\### 3. Receipt Voucher Automation



Run:



`python receipt\_vouchers.py`



The script reads receipt transactions from `receipt\_entries.csv` and creates Receipt Voucher requests for TallyPrime.



The response is validated for successful processing and errors.



\### 4. Single Voucher Creation



Run:



`python single\_voucher.py`



This script demonstrates the direct creation of an individual Payment Voucher through TallyPrime's XML interface.



The response is validated and reported to the user.



\---



\## 🔌 TallyPrime Integration



The project communicates with TallyPrime using HTTP requests.



The Python scripts send XML data to the local TallyPrime server using the Requests library and the TallyPrime HTTP interface.



The accounting transaction is converted into a Tally-compatible XML request and submitted to TallyPrime.



TallyPrime then returns an XML response containing information such as:



\- Created transactions

\- Altered transactions

\- Deleted transactions

\- Ignored transactions

\- Errors

\- Exceptions



The Python scripts process these responses and provide a summary of the result.



\---



\## 🧾 Example Payment Transaction



A payment transaction can be represented as:



Date: 01-Apr-2026

Account: Cash

Ledger: Office Expenses

Amount: ₹500

Narration: Being payment made for office expenses



The Python script converts this structured data into a Tally-compatible XML request.



\---



\## 🧾 Example Receipt Transaction



A receipt transaction can be represented as:



Date: 01-Apr-2026

Account: Bank

Ledger: Sales

Amount: ₹1,500

Narration: Being receipt received from customer



The Python script converts the transaction into XML and submits it to TallyPrime.



\---



\## 🛠️ Validation \& Error Handling



The project validates input data and processes TallyPrime's XML response to identify whether a transaction was successfully processed.



A typical successful TallyPrime response can contain:



<RESPONSE>

&#x20;   <CREATED>1</CREATED>

&#x20;   <ALTERED>0</ALTERED>

&#x20;   <ERRORS>0</ERRORS>

&#x20;   <EXCEPTIONS>0</EXCEPTIONS>

</RESPONSE>



If TallyPrime rejects a transaction, the response can provide error information that can be used to identify and correct the underlying issue.



The automation scripts provide user-friendly processing summaries including:



\- Created

\- Altered

\- Deleted

\- Errors

\- Successful

\- Failed



This allows users to identify processing issues without manually inspecting the complete XML response.



\---



\## ✅ Testing



The automation was tested with a running TallyPrime company.



Test execution included:



\- Ledger processing

\- Payment Voucher processing

\- Receipt Voucher processing

\- Individual Payment Voucher processing



The tested scripts successfully connected to the TallyPrime HTTP server and received XML responses without reported errors.



The scripts provide processing summaries showing the number of transactions processed, successful operations, and failures.



> \*\*Note:\*\* The exact Created, Altered, Deleted, and Error counts depend on the state of the target TallyPrime company and the transaction being processed.



\---



\## 💡 Business Use Case



Accounting professionals frequently perform repetitive data-entry activities involving ledgers, payments, receipts, and other accounting transactions.



This project demonstrates how Python automation can connect accounting workflows with TallyPrime to:



\- Reduce repetitive manual data entry

\- Improve consistency

\- Process structured accounting data

\- Automate routine voucher processing

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

\- Input validation

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



\## ⚠️ Limitations



\- TallyPrime must be installed and running locally.

\- The required TallyPrime company must be open and accessible.

\- The TallyPrime HTTP server must be available at `localhost:9000`.

\- Ledger names and accounting data must correspond to the target TallyPrime company.

\- The project is currently designed for local TallyPrime automation rather than cloud-based execution.



\---



\## 👨‍💻 Author



\*\*Prajwal R\*\*



B.Com (Hons) – International Accounting \& Finance  

ACCA Finalist | CA Intermediate



GitHub: \[@prajwalr1008](https://github.com/prajwalr1008)



\---



\## ⭐ Project



If you find this project useful, consider giving the repository a ⭐ on GitHub.

