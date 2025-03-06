# English
## Alternate.nl Stock Checker

This Python script refreshes a given Alternate.nl product page until it's in stock, then plays a really loud noise and opens the page in your browser. Useful for GPUs! *Note that you must complete the purchase yourself.*

**THIS SCRIPT IS WRITTEN WITH THE ASSUMPTION THAT YOU USE FIREFOX OR A FIREFOX FORK AS YOUR DEFAULT BROWSER. CHROME USERS WILL NEED TO MAKE LARGER CHANGES!**

## Requirements
- Python 3.10
- Firefox installed somewhere on your PC
- Geckodriver, found at https://github.com/mozilla/geckodriver/releases.

Download the source code and extract the .zip somewhere convenient.
Put the Geckodriver executable anywhere, I recommend in the same directory as the script.
Edit lines 11, 15, 18, and 45 of the script to match your setup.
Finally, run the script in a terminal, `python checker.py`

With luck, it should open a browser window and automatically refresh it every second. If the product comes back in stock, prepare your ears!!

# Nederlands
## Alternate.nl Voorraadchecker

Dit Python-script vernieuwt een opgegeven Alternate.nl productpagina totdat het product op voorraad is, speelt dan een erg luid geluid af en opent de pagina in je browser. Handig voor GPU's! *Let op: je moet de aankoop zelf afronden.*

**DIT SCRIPT IS GESCHREVEN MET DE VERONDERSTELLING DAT JE FIREFOX OF EEN FIREFOX-FORK ALS STANDAARDBROWSER GEBRUIKT. CHROME-GEBRUIKERS ZULLEN GROTERE AANPASSINGEN MOETEN DOEN!**

## Vereisten
- Python 3.10
- Firefox geïnstalleerd ergens op je pc
- Geckodriver, te vinden op https://github.com/mozilla/geckodriver/releases.

Download de broncode en pak het .zip-bestand uit op een handige locatie.
Plaats het Geckodriver-uitvoerbare bestand ergens, ik raad aan in dezelfde map als het script.
Bewerk regels 11, 15, 18 en 45 van het script zodat ze overeenkomen met jouw setup.
Voer ten slotte het script uit in een terminal met `python checker.py`.

Met een beetje geluk opent het een browservenster en vernieuwt het automatisch elke seconde. Als het product weer op voorraad is, bereid je oren dan voor!!