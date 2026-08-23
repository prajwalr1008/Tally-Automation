import pandas as pd
import requests
from bs4 import BeautifulSoup as Soup

TALLY_URL = "http://localhost:9000"
COMPANY_NAME = "PRAJWAL & COMPANY"


def create_receipt_voucher(date, account_name, ledger_name, amount, narration):

    return f"""
<ENVELOPE>
 <HEADER>
  <TALLYREQUEST>Import Data</TALLYREQUEST>
 </HEADER>
 <BODY>
  <IMPORTDATA>
   <REQUESTDESC>
    <REPORTNAME>Vouchers</REPORTNAME>
    <STATICVARIABLES>
     <SVCURRENTCOMPANY>{COMPANY_NAME}</SVCURRENTCOMPANY>
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
    try:
        response = requests.post(
            TALLY_URL,
            data=xml_data.encode("utf-8"),
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
        return False

    except requests.exceptions.Timeout:
        print("\n❌ TallyPrime did not respond within 10 seconds.\n")
        return False

    except requests.exceptions.RequestException as error:
        print(f"\n❌ Connection error: {error}\n")
        return False

    try:
        xml_response = Soup(response.text, "xml")

        errors = xml_response.find_all("LINEERROR")

        if errors:
            print("\n❌ TallyPrime rejected the receipt voucher:")

            for error in errors:
                print(f"   {error.get_text(strip=True)}")

            print()
            return False

        created = xml_response.find("CREATED")
        altered = xml_response.find("ALTERED")
        errors_count = xml_response.find("ERRORS")

        created_value = created.get_text(strip=True) if created else "0"
        altered_value = altered.get_text(strip=True) if altered else "0"
        errors_value = errors_count.get_text(strip=True) if errors_count else "0"

        print("\n✅ Receipt voucher processed successfully.")
        print(f"Created : {created_value}")
        print(f"Altered : {altered_value}")
        print(f"Errors  : {errors_value}")
        print()

        return True

    except Exception as error:
        print(f"\n❌ Unable to process TallyPrime response: {error}\n")
        return False


def validate_csv(df):

    required_columns = {
        "Date",
        "Account Name",
        "Ledger Name",
        "Amount",
        "Narration"
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        print("\n❌ Missing required CSV columns:")
        print(", ".join(sorted(missing_columns)))
        print()
        return False

    if df.empty:
        print("\n❌ receipt_entries.csv contains no transactions.\n")
        return False

    return True


def main():

    try:
        df = pd.read_csv("receipt_entries.csv")

    except FileNotFoundError:
        print("\n❌ receipt_entries.csv was not found.")
        print("Make sure the CSV file is in the project folder.\n")
        return

    if not validate_csv(df):
        return

    print(f"\n📄 Processing {len(df)} receipt voucher(s)...")

    successful = 0
    failed = 0

    for index, row in df.iterrows():

        try:
            amount = float(row["Amount"])

            if amount <= 0:
                print(
                    f"\n❌ Voucher {index + 1}: "
                    "Amount must be greater than zero."
                )
                failed += 1
                continue

            date = str(row["Date"]).strip()

            if not date.isdigit() or len(date) != 8:
                print(
                    f"\n❌ Voucher {index + 1}: "
                    f"Invalid date '{date}'. Use YYYYMMDD."
                )
                failed += 1
                continue

            xml_data = create_receipt_voucher(
                date=date,
                account_name=str(row["Account Name"]).strip(),
                ledger_name=str(row["Ledger Name"]).strip(),
                amount=amount,
                narration=str(row["Narration"]).strip()
            )

            if send_to_tally(xml_data):
                successful += 1
            else:
                failed += 1

        except (ValueError, TypeError):
            print(
                f"\n❌ Voucher {index + 1}: "
                "Invalid amount in CSV."
            )
            failed += 1

    print("────────────────────────────────")
    print("Receipt Voucher Summary")
    print("────────────────────────────────")
    print(f"Total     : {len(df)}")
    print(f"Successful: {successful}")
    print(f"Failed    : {failed}")
    print("────────────────────────────────\n")


if __name__ == "__main__":
    main()