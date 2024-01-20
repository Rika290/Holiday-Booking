**Hotel Booking App**
![image](https://github.com/Rika290/Hotel-booking-app/assets/126352441/8603aba4-c812-433d-bfad-5a053ca89fda)


- App link :- https://hotel-booking-app-8yyzqf4xn2giwqzajpbq9d.streamlit.app/ 

*ABOUT*:-
- This is a web app of a fictitious travel agency called '@urDesti' which helps in choosing and booking hotels across India at comparatively low prices

*TOOLS USED*:-
1. SQL
3. Python 
4. Streamlit 

*METHOD*:
1. Database creation:
- Using MySQL queries, different tables to store data on destination and hotels were created.
- Data on places, i.e, North and South were added
- Table for bookings was created which will accept the input from user
- Once saved, these tables were exported as csv files.

2. Backend:
- The csv files are imported to Google Colab notebook
- With Pandas in python, the values from data tables can be accessed and manipulated
- OTP Generator:
   - random model was used for creating the OTP; Using smtplib and MIMEText;
   - an email containing the OTP will be sent to the mail id given by the user

3. Frontend:
- The welcome page icon and heading were setup using streamlit
- An user can navigate to Dashboard for viewing further details
- When the menu bar is accessed, user can choose any place and fill the details accordingly along with OTP
- Once all details are given correctly, the screen pops up a message - Booked successfully
- When the process is completed, the user can access the booking information by entering the OTP
- Finally, an acknowledgement mail from the company will be sent to the user

*REFERENCES*:
- https://www.makeuseof.com/otp-verification-system-python/
- https://docs.python.org/3.5/library/email.html
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- https://docs.streamlit.io/
