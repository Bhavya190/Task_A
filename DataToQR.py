import gradio as gr
from PIL import Image
import qrcode as qr 
import json


# I used Gradio UI Framework for my project because it is easy to use 
# and it gives us a proper user fiendly interface
# and it has it's own style so i don't have to create my stylesheet.


def get_qr_code(name,profile,profession,mobile_no,email,address,education,gender):         # This function is used to generate qr code. It takes 4 inputs.
   if len(mobile_no) == 10 and mobile_no.isdigit():
        info = {                                             # All inputs are stored in dictionary
            'Name': name,
            'Profession': profession,
            'Profile': profile,
            'E-mail': email,
            'Address': address,
            'Education': education,
            'Gender': gender,
            'Mobile No': mobile_no,
        }
        qr_img = qr.make(json.dumps(info)).convert("RGB")   # json.dumps() used to make dictionary to string form because qr code is only readable in str format.
                                                            # qr.make()  used to make a qr code of information
                                                        # convert()  used to convert qr image to RGB mode.     
                                                          
        return "",qr_img                                       #return the image object to show qrcode in output field
   else:
       return "Invalid Mobile Number. Please enter a 10-digit number.", None

demo = gr.Interface(
    fn=get_qr_code,                                     # calling the get_qr_code function
    inputs = [                                          # 8 input fields(name,profile,profession,mobile_no,email,address,education,gender)
            gr.Textbox(label='Name : ',placeholder='Enter Your Name'), 
            gr.TextArea(label='Profile : ',placeholder='Introduction of yourself'), 
            gr.Textbox(label='Profession : ',placeholder='Enter Your Proffesion'),
            gr.Textbox(label='Mobile No : ',placeholder='Enter Your Mobile Number'),
            gr.Textbox(label='E-mail : ',placeholder='Enter Your E-mail',type='email'),
            gr.TextArea(label='Address : ',placeholder='Enter Your Address'),
            gr.TextArea(label='Education : ',placeholder='Enter Your Eduction'),
            gr.Radio(["Male","Female","Other"] ,label='Gender: ' ),
        ],
    outputs=[
        gr.Textbox(label='Eroor Massage: ', interactive=False),
        gr.Image(label='Scan This QR Code: ',type='pil'), # output in image format
    ],
    title='QR Code Generator',                          # giving title to the page
    description="""Welcome to Bhavya's QR Code Generator. This web-app is made to generate QR code of a personal information. It can use when a person want to share his/her data to a company 
    but not in .pdf/.docx formate. This Qrcode generator web-app is generating low size file(in KB) so when you download the QR code it will consume small amount of storage rather than store in .pdf/.docx\n
        feature-1: It use Gradio UI.
        feature-2: It takes email by textbox(type='email').
        feature-3: It checks whethere Mobile Number has 10 digits.
        feture-4: it shows error maggage if number is not ok. 
        feature-5: It is easy to use.
        feature-6: It is responsive and will work on any device.
        
    """,   #welcome note and description of project and functionalities in brif 
    
)

demo.launch()                                            #launch the demo

