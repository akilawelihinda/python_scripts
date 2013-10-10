Program Overview:
I have developed this script for anybody to use. What this script does is pull data off a MySQL table and then send a text message to the phone number the script pulled.
The program first saves all the MySQL data into local variables. Then it logins into an email account, either the default email account you specified or the email account of the client that 
is stored on the MySQL database. The benefit of having the client's email information is because when the text is sent, it will show up as being sent from the client's email address.
Once this program logs in, it sends an email to the carrier's email address, which will then be delivered as a text to the phone number. Since we do not always know the 
carrier of the phone number we are trying to text, the program attempts to send the email message all of the following carriers: Verizon, AT&T, Sprint, and T-Mobile
(of course only one of the messages will successfully received). Once the carrier receives this email, a text message will automatically be sent to the phone number.

-Make sure your database has a table titled "clients" with exactly 5 columns with the name, phoneNumber, message, Gmail User, and Gmail Password exactly in that order.
-If both the Gmail User and Gmail Password row are blank, then the program will use the default Gmail login, which you must assign by editing the "textEmail.py" file.
 -If the Gmail User and Gmail Password are included, then the program will login using those credentials and send the text message using that email account.
 
 ***MAKE SURE:
 -you enter a default email address and password
 -you enter the host name, user name, password, and database name so that you can connect to your database
 