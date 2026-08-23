import pandas as pd
import requests
from bs4 import BeautifulSoup as Soup

TALLY_URL = "http://localhost:9000"
COMPANY_NAME = "PRAJWAL & COMPANY"


def create_ledger_xml(ledger_name, parent, opening_balance):
    return f"""
<LEDGER NAME="{ledger_name}" ACTION="CREATE">
    <NAME.LIST>
        <NAME>{ledger_name}</NAME>
    </NAME.LIST>
    <PARENT>{parent}</PARENT>
    <OPENINGBALANCE>{opening_balance}</OPENINGBALANCE>
</LEDGER>
"""


def create_master_xml(ledger_data):
    ledger_tags = ""

    for _, row in ledger_data.iterrows():
        ledger_tags += create_ledger_xml(
            ledger_name=row["LedgerName"],
            parent=row["Parent"],
            opening_balance=row["OpeningBalance"]
        )

    return f"""<ENVELOPE>
 <HEADER>
  <TALLYREQUEST>Import Data</TALLYREQUEST>
 </HEADER>
 <BODY>
  <IMPORTDATA>
   <REQUESTDESC>
    <REPORTNAME>All Masters</REPORTNAME>
    <STATICVARIABLES>
     <SVCURRENTCOMPANY>{COMPANY_NAME}</SVCURRENTCOMPANY>
    </STATICVARIABLES>
   </REQUESTDESC>
   <REQUESTDATA>
    <TALLYMESSAGE xmlns:UDF="TallyUDF">
      {ledger_tags}
    </TALLYMESSAGE>
   </REQUESTDATA>
  </IMPORTDATA>
 </BODY>
</ENVELOPE>"""


def tally_request(xml_string):
    try:
        response = requests.post(
            TALLY_URL,
            data=xml_string.encode("utf-8"),
            headers={"Content-Type": "application/xml"},
            timeout=10
        )

        response.raise_for_status()

    except requests.exceptions.ConnectionError:
        print("\n❌ Unable to connect to TallyPrime.")
        print("Please make sure:")
        print("1. TallyPrime is running.")
        print("2. The company is open.")
        print("3. TallyPrime HTTP Server is enabled.")
        print("4. The HTTP port is set to 9000.\n")
        return

    except requests.exceptions.Timeout:
        print("\n❌ TallyPrime did not respond within 10 seconds.\n")
        return

    except requests.exceptions.RequestException as error:
        print(f"\n❌ Connection error: {error}\n")
        return

    try:
        xml_data = Soup(response.text, "xml")

        errors = xml_data.find_all("LINEERROR")

        if errors:
            print("\n❌ TallyPrime returned an error:")

            for error in errors:
                print(f"   {error.get_text(strip=True)}")

            print()
            return

        created = xml_data.find("CREATED")
        altered = xml_data.find("ALTERED")
        deleted = xml_data.find("DELETED")
        errors_count = xml_data.find("ERRORS")

        print("\n✅ TallyPrime response received.")
        print(f"Created : {created.get_text(strip=True) if created else '0'}")
        print(f"Altered : {altered.get_text(strip=True) if altered else '0'}")
        print(f"Deleted : {deleted.get_text(strip=True) if deleted else '0'}")
        print(f"Errors  : {errors_count.get_text(strip=True) if errors_count else '0'}")
        print()

    except Exception as error:
        print(f"\n❌ Unable to process TallyPrime response: {error}\n")


def main():
    try:
        df = pd.read_csv("Ledger_Creation.csv")

    except FileNotFoundError:
        print("\n❌ Ledger_Creation.csv was not found.")
        print("Make sure the CSV file is in the project folder.\n")
        return

    required_columns = {"LedgerName", "Parent", "OpeningBalance"}

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        print("\n❌ Missing required CSV columns:")
        print(", ".join(missing_columns))
        print()
        return

    if df.empty:
        print("\n❌ Ledger_Creation.csv contains no ledger records.\n")
        return

    print(f"\n📄 Processing {len(df)} ledger(s)...")

    master_xml = create_master_xml(df)

    tally_request(master_xml)


if __name__ == "__main__":
    main()