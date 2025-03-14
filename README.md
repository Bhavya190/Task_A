Dependencies and Libraries=>

Gradio Installation :-  pip install gradio
QRcode Installation :-  pip install qrcode
PIl 
json


To Run Code => 

use f5 or ctrl+f5 or python DataToQR.py


Purpose of each component =>

1.  There are 8 inputs that will fill by user (take data from user).\n
    - for name,profession,mobileno and email I used text inputs
    - for address,education and profile I used textarea inputs
    - for gender I used radio buttons.

2.  when user submit his/her data then get_qr_code function is called.
    Which is basically do one thing that is to generate qr code of user's data and show it as an image in output field.

3. String functions len(),isdigit() are used to check mobile number.

4. get_qr_code function returns qr code of user's data.It is parameterized function.