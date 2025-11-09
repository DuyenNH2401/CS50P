import sys
import requests

respond = requests.get("https://api.coincap.io/v2/assets/bitcoin")
information = respond.json()

try:
    num_coin = float(sys.argv[1])

    amount = num_coin * float(information["data"]["priceUsd"])

    print(f"${amount:,.4f}")

except IndexError:
    sys.exit("Missing command-line argument")

except requests.RequestException:
    sys.exit()

except ValueError:
    sys.exit("Command-line argument is not a number")


