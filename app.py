import streamlit as st
import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText
import math
import random

st.set_page_config(page_title='@urDesti',page_icon='https://i.etsystatic.com/15452447/r/il/d69775/1656294668/il_fullxfull.1656294668_8ou2.jpg')
choice=st.sidebar.selectbox('Dashboard',('Home','Hotels','View bookings'))
st.sidebar.image('https://i2.wp.com/chasingdaisiesblog.com/wp-content/uploads/2021/01/DIGITAL-peachy-dreams-picture-wall-collage-kit-peach-pink-aesthetic-travel-DIGITAL.jpeg?strip=all')
st.sidebar.image("https://images.unsplash.com/photo-1515876305430-f06edab8282a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FtcGVydmFufGVufDB8fDB8fHww&w=1000&q=80")
if(choice=='Home'):
    st.title('Welcome to @urDesti')
    st.image('https://www.ibphub.com/imgs/blog/86.jpg')
    st.write('You can choose your destination and book resort or hotel across India.')
elif(choice=='Hotels'):
    st.image('https://virtuoso-prod.dotcms.cloud/images/landing-pages/hotels/perk-grid.png')
    ch=st.selectbox('Menu',('Choose','North','South'))
    if(ch=='Home'):
        st.text('We provide you a list of hotels which are rated as 3 and above. \nBook fast and enjoy your vacation😊')
        st.image('https://media.istockphoto.com/id/456859205/photo/multiple-photographs-of-vacation-scenes.jpg?s=612x612&w=0&k=20&c=fX2gODiFol1sbYDwPJ5LqC_QeABp2ibs8I4DQp0q8Lo=')
    elif(ch=='North'):
        d=pd.read_csv('north.csv')
        st.table(d)
        i=st.text_input("Enter the place name")
        b=pd.read_csv('hotels.csv')                
        b1=b[b['Places']==i]
        st.table(b1)
        st.text('Only available hotels are displayed')
        d=st.checkbox('Book now',)
        if d:
            email_receiver = st.text_input('email id')
            if st.button("Send Email"):
                digits='0123456789'
                OTP=''
                for i in range(4):
                    OTP+=digits[math.floor(random.random()*10)]
                    otp = OTP + " is your OTP"
                ms= otp
                msg = MIMEText(ms)
                msg['From'] = 'rithikasekaran29@gmail.com'
                msg['To'] = email_receiver
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('rithikasekaran29@gmail.com', 'ordj bsin kwzd mywp')
                server.sendmail('rithikasekaran29@gmail.com',email_receiver, msg.as_string())
                server.quit()
                st.success('OTP sent successfully')
            qd=st.toggle('Book now')
            if qd:
                q=st.number_input('OTP')
                w=st.text_input('first name')
                e=st.text_input('last name')
                r=st.text_input('id of the place')
                t=st.text_input('duration: Number of days and nights')
                y=st.text_input('total members')
                h=st.text_input('Hotel')
                u=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")                                
                if st.button('Book'):
                    b=pd.read_csv('booking.csv')
                    r=pd.DataFrame(data=[[q,w,e,r,t,y,u,h]],columns=b.columns)
                    b=pd.concat([b,r], ignore_index=True)
                    b.to_csv('booked.csv',index=False)                    
                    ms= 'Thank you for using @urDesti.'
                    msg = MIMEText(ms)
                    msg['From'] = 'rithikasekaran29@gmail.com'
                    msg['To'] = email_receiver
                    msg['Subject'] = 'Hotel booking'
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('rithikasekaran29@gmail.com', 'ordj bsin kwzd mywp')
                    server.sendmail('rithikasekaran29@gmail.com',email_receiver, msg.as_string())
                    server.quit()                
                    st.header('Booked successfully')
    elif(ch=='South'):
        de=pd.read_csv('south.csv')
        st.table(de.loc[:,['ID','Places']])
        il=st.text_input("Enter the place name")
        ba=pd.read_csv('hotels.csv')                
        b1=ba[ba['Places']==il]
        st.table(b1)
        st.text('Only available hotels are displayed')
        d=st.checkbox('Book now',)
        if d:
            email_receiver = st.text_input('email id')
            if st.button("Send Email"):
                digits='0123456789'
                OTP=''
                for i in range(4):
                    OTP+=digits[math.floor(random.random()*10)]
                    otp = OTP + " is your OTP"
                ms= otp
                msg = MIMEText(ms)
                msg['From'] = 'rithikasekaran29@gmail.com'
                msg['To'] = email_receiver
                msg['Subject'] = 'Hotel booking'
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('rithikasekaran29@gmail.com', 'ordj bsin kwzd mywp')
                server.sendmail('rithikasekaran29@gmail.com',email_receiver, msg.as_string())
                server.quit()
                st.success('OTP sent successfully')
            qd=st.toggle('Book now')
            if qd:
                q=st.number_input('OTP')
                w=st.text_input('first name')
                e=st.text_input('last name')
                r=st.text_input('id of the place')
                t=st.text_input('duration: Number of days and nights')
                y=st.text_input('total members')
                h=st.text_input('Hotel')
                u=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")                                
                if st.button('Book'):
                    b=pd.read_csv('booking.csv')
                    r=pd.DataFrame(data=[[q,w,e,r,t,y,u,h]],columns=b.columns)
                    b=pd.concat([b,r], ignore_index=True)
                    b.to_csv('booked.csv',index=False)                    
                    ms= 'Thank you for using @urDesti.'
                    msg = MIMEText(ms)
                    msg['From'] = 'rithikasekaran29@gmail.com'
                    msg['To'] = email_receiver
                    msg['Subject'] = 'Hotel booking'
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('rithikasekaran29@gmail.com', 'ordj bsin kwzd mywp')
                    server.sendmail('rithikasekaran29@gmail.com',email_receiver, msg.as_string())
                    server.quit()                
                    st.header('Booked successfully')
else:
    st.image('https://static.vecteezy.com/system/resources/previews/005/581/333/large_2x/bangkok-thailand-january-20-2022-india-magnifying-glass-close-up-with-colorful-world-map-photo.jpg')
    st.write('Enter the OTP again to view your booking')
    e=st.number_input('OTP:')
    st.write('Click enter')
    b=pd.read_csv('booked.csv')
    bs=b[b['OTP']==e]
    st.table(bs)

                
                    
        
