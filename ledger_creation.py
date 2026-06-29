import pandas as pd
import requests
from bs4 import BeautifulSoup as Soup

main_tag="""<ENVELOPE>
 <HEADER>
  <TALLYREQUEST>Import Data</TALLYREQUEST>
 </HEADER>
 <BODY>
  <IMPORTDATA>
   <REQUESTDESC>
    <REPORTNAME>All Masters</REPORTNAME>
    <STATICVARIABLES>
     <SVCURRENTCOMPANY>VARS PARKWOOD OWNERS ASSOCIATION</SVCURRENTCOMPANY>
    </STATICVARIABLES>
   </REQUESTDESC>
   <REQUESTDATA>
	<TALLYMESSAGE xmlns:UDF="TallyUDF">"""

df=pd.read_csv('Ledger_Creation.csv')

ledger_tag=""""""
# Negative Number for debit opening balance, and positive number for credit opening balance.
for _,row in df.iterrows():
    ledger_tag+="""<LEDGER NAME="""+'"'+row['LedgerName']+'"'+"""ACTION="CREATE">
    <NAME.LIST>
    <NAME>"""+row['LedgerName']+"""</NAME>
    </NAME.LIST>
    <PARENT>"""+row['Parent']+"""</PARENT>
    <OPENINGBALANCE>"""+str(row['OpeningBalance'])+"""</OPENINGBALANCE>
    </LEDGER>"""

closing_tag="""</TALLYMESSAGE>
   </REQUESTDATA>
  </IMPORTDATA>
 </BODY>
</ENVELOPE>"""

master_tag=main_tag+ledger_tag+closing_tag

def tally_request(xml_string):
    headers={'Content-Type': 'soap/xml'}
    xml_data=requests.post('http://localhost:9000', data=xml_string, headers=headers).text
    xml_data=xml_data.replace('&amp;','&#38;')
    xml_data=xml_data.replace('&apos;','&#39;')
    xml_data = Soup(xml_data,'xml')
    print(xml_data)

#Execute the tag

tally_request(master_tag)
