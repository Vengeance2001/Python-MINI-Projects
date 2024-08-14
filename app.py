from flask import Flask, render_template, request, send_file
import qrcode 
import qrcode.constants
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    link = request.form['link']
    qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="black")
    #storing image in buffer
    buff = io.BytesIO()
    img.save(buff, 'PNG')
    buff.seek(0)
    return  send_file(buff, mimetype='image/png', as_attachment=True, download_name='qrfile.png')

if __name__ == 'main':
    app.run(debug=True)









