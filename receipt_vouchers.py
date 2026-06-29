import pandas as pd
import requests

def create_receipt_vouchers(date, account_name, ledger_name, amount, narration):

    return f"""
<ENVELOPE>
 <HEADER>
  <TALLYREQUEST>Import Data</TALLYREQUEST>
 </HEADER>
 <BODY>
  <IMPORTDATA>
   <REQUESTDESC>
    <REPORTNAME>All Masters</REPORTNAME>
    <STATICVARIABLES>
     <SVCURRENTCOMPANY>KRFIN</SVCURRENTCOMPANY>
    </STATICVARIABLES>
   </REQUESTDESC>
   <REQUESTDATA>
    <TALLYMESSAGE xmlns:UDF="TallyUDF">
      <VOUCHER VCHTYPE="Receipt" ACTION="Create">
        <DATE>{date}</DATE>
        <NARRATION>{narration}</NARRATION>
        <VOUCHERTYPENAME>Receipt</VOUCHERTYPENAME>
        <PARTYLEDGERNAME>{ledger_name}</PARTYLEDGERNAME>
        <PERSISTEDVIEW>Accounting Voucher View</PERSISTEDVIEW>
        <EFFECTIVEDATE>{date}</EFFECTIVEDATE>
        <ALLLEDGERENTRIES.LIST>
         <LEDGERNAME>{ledger_name}</LEDGERNAME>
         <ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>
         <AMOUNT>{amount}</AMOUNT>
        </ALLLEDGERENTRIES.LIST>
        <ALLLEDGERENTRIES.LIST>
         <LEDGERNAME>{account_name}</LEDGERNAME>
         <ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE>
         <AMOUNT>-{amount}</AMOUNT>
        </ALLLEDGERENTRIES.LIST>
      </VOUCHER>
    </TALLYMESSAGE>
   </REQUESTDATA>
  </IMPORTDATA>
 </BODY>
</ENVELOPE>
"""

def send_to_tally(xml_data):
    headers = {"Content-Type": "application/xml"}
    response = requests.post("http://localhost:9000", data=xml_data.encode("utf-8"), headers=headers)
    print("Response:", response.text)

df = pd.read_csv("receipt_entries.csv")

for _, row in df.iterrows():
    xml_data = create_receipt_vouchers(
        date = row["Date"],
        account_name = row["Account Name"],
        ledger_name = row["Ledger Name"],
        amount = row["Amount"],
        narration = row["Narration"]
    )
    send_to_tally(xml_data)





