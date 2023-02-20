# Flight Deal Finder

The purpose of this application is to find flights over the next 6 months at a price that is below the targetted price point that has been set by the user.

## How it works
1) The user will fill a new google sheet in the following format below. The city and price limit needs to be set for each destination (IATA codes will be automatically filled later).

<img width="366" alt="image" src="https://user-images.githubusercontent.com/105379503/219991230-da773fa8-2322-41df-a4cb-010da6ba9bd9.png">

2) The user needs to create an account in [Sheety](https://sheety.co/), [Tequila](https://tequila.kiwi.com/portal/login), [Twilio](https://www.twilio.com/?g=%2F) to access their APIs.

5) In Sheety, create a new project (with google sheets) and paste your url into the input bar as shown below.

<img width="848" alt="image" src="https://user-images.githubusercontent.com/105379503/219992998-9f012858-8f35-4c11-99ef-4521677af397.png">

Then enter your URL as generated below into [data_manager.py](https://github.com/StevenD24/Flight-Deal-Finder/blob/main/Flight%20Deal%20Finder/data_manager.py).

<img width="751" alt="image" src="https://user-images.githubusercontent.com/105379503/219993488-95e0a9d7-1720-463b-bd33-e19469173c15.png">

<img width="388" alt="image" src="https://user-images.githubusercontent.com/105379503/219993973-52732108-9560-45e9-8d82-37f702ce3077.png">

4) Fill in the API key generated by Tequila in [flight_search.py](https://github.com/StevenD24/Flight-Deal-Finder/blob/main/Flight%20Deal%20Finder/flight_search.py).

<img width="440" alt="image" src="https://user-images.githubusercontent.com/105379503/219992330-c7380960-cf06-4018-8f50-44f286f8867f.png">

5) Fill in the 4 strings inside [notification_manager.py](https://github.com/StevenD24/Flight-Deal-Finder/blob/main/Flight%20Deal%20Finder/notification_manager.py) using your generated tokens from Twilio.

<img width="443" alt="image" src="https://user-images.githubusercontent.com/105379503/219992085-eeff8951-1097-4218-9b36-5826dc50587a.png">

6) The application is now ready to run. Run main.py and the IATA codes will automatically populate as shown below:

<img width="375" alt="image" src="https://user-images.githubusercontent.com/105379503/219995114-8de9fb4a-f19c-4111-8bdf-3adab36bee38.png">

7) Wait for the application to pull the information from the APIs and see the results!

Example of the expected SMS text:

<img width="300" alt="image" src="https://user-images.githubusercontent.com/105379503/219995068-5daf1b7d-8744-47de-800b-3a7d32277180.png">

