import requests

def create_payment_vouchers():

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
     <SVCURRENTCOMPANY>Parkwood Dummy</SVCURRENTCOMPANY>
    </STATICVARIABLES>
   </REQUESTDESC>
   <REQUESTDATA>
    <TALLYMESSAGE xmlns:UDF="TallyUDF">
      <VOUCHER VCHTYPE="Payment" ACTION="Create">
        <DATE>20240101</DATE>
        <NARRATION>Being Payment made</NARRATION>
        <VOUCHERTYPENAME>Payment</VOUCHERTYPENAME>
        <PARTYLEDGERNAME>Cash</PARTYLEDGERNAME>
        <PERSISTEDVIEW>Accounting Voucher View</PERSISTEDVIEW>
        <EFFECTIVEDATE>20240101</EFFECTIVEDATE>
        <ALLLEDGERENTRIES.LIST>
         <LEDGERNAME>Raghav</LEDGERNAME>
         <ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE>
         <AMOUNT>-222</AMOUNT>
        </ALLLEDGERENTRIES.LIST>
        <ALLLEDGERENTRIES.LIST>
         <LEDGERNAME>Cash</LEDGERNAME>
         <ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>
         <AMOUNT>222</AMOUNT>
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

xml_data = create_payment_vouchers()
send_to_tally(xml_data)

