from flask import Blueprint, render_template,request,redirect,url_for
from flask_login import  login_required, current_user
views= Blueprint('views',__name__)
from website import authenticate
import qrcode
from io import BytesIO
import base64
import io


@views.route('/')
#@login_required
def home():
    return render_template("home2.html",user=current_user) #gives info about current user



@views.route('/dbupd')





@views.route("/qrpage")
def index():
    return render_template("index.html")


@views.route("/payment")
#@login_required
def payment():
    return render_template("payment.html")

@views.route("/cart")
def cart_func():
    image=request.args.get('image')
    title=request.args.get('title')
    price=request.args.get('price')
    print(title)

    return render_template("add_cart.html",title=title,price=price)
# def calc(price,qty):
#     price=price
#     qty=qty
#     gst=18
#     total=price*qty+gst
#     return total












'''@views.route('/qrpage')
def index():
  return  render_template("index.html")

@views.route('/generate', methods=['POST'])
def generate():
    # Get the data from the form
    data = request.form['data']

    # Generate the QR code image
    img = qrcode.make(data)

    # Serve the image as a PNG file
    return serve_pil_image(img)
   



# Define a function to serve a PIL image as a PNG file
def serve_pil_image(pil_img):
    from io import BytesIO
    from flask import send_file
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')'''
    