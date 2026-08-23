import requests
from bs4 import BeautifulSoup as Soup

TALLY_URL = "http://localhost:9000"
COMPANY_NAME = "PRAJWAL & COMPANY"


def create_payment_voucher():
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
      <VOUCHER VCHTYPE="Payment" ACTION="Create">
        <DATE>20260401</DATE>
        <NARRATION>Being Payment made</NARRATION>
        <VOUCHERTYPENAME>Payment</VOUCHERTYPENAME>
        <PARTYLEDGERNAME>Cash</PARTYLEDGERNAME>
        <PERSISTEDVIEW>Accounting Voucher View</PERSISTEDVIEW>
        <EFFECTIVEDATE>20260401</EFFECTIVEDATE>

        <ALLLEDGERENTRIES.LIST>
          <LEDGERNAME>Office Expenses</LEDGERNAME>
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
            print("\n❌ TallyPrime rejected the voucher:")

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

        print("\n✅ Payment voucher processed successfully.")
        print(f"Created : {created_value}")
        print(f"Altered : {altered_value}")
        print(f"Errors  : {errors_value}")
        print()

        return True

    except Exception as error:
        print(f"\n❌ Unable to process TallyPrime response: {error}\n")
        return False


def main():
    print("\n📄 Processing single payment voucher...")

    xml_data = create_payment_voucher()

    success = send_to_tally(xml_data)

    print("────────────────────────────────")
    print("Single Voucher Summary")
    print("────────────────────────────────")

    if success:
        print("Status: Successful")
    else:
        print("Status: Failed")

    print("────────────────────────────────\n")


if __name__ == "__main__":
    main()