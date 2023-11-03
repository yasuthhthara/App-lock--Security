from flask import Flask, request, render_template_string
import pyotp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def time_based_code_generator():
    verification_result = ""  # Initialize verification_result
    generated_code = ""  # Initialize generated_code

    if request.method == 'POST':
        user_code = request.form['code_input']
        secret = request.form['secret_key']

        totp = pyotp.TOTP(secret)
        generated_code = totp.now()

        if user_code == generated_code:
            verification_result = "Code is valid."
        else:
            verification_result = "Code is not valid."

    return render_template_string(HTML_TEMPLATE, verification_result=verification_result, generated_code=generated_code)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>APP LOCK APPLICATION</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: black;
    }
    h1 {
      text-align: center;
      color: #333;
      background-color: white;
      padding: 10px;
    }
    .container {
      background-color: #ffbf00;
      border-radius: 5px;
      padding: 20px;
      margin: 20px auto;
      width: 50%;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    form {
      text-align: center;
      padding: 20px;
    }
    label {
      display: block;
      margin-bottom: 5px;
    }
    input {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
    }
    p {
      text-align: center;
      font-weight: bold;
      margin-top: 20px;
      
    }
  </style>
</head>
<body>
  <h1>App Lock Application</h1>
  <div class="container">
    <p style="color: #000077;">Generated Code: {{ generated_code }}</p>

    <form method="post">
        <label for="secret_key">Secret Key:</label>
        <input type="text" id="secret_key" name="secret_key" value="YourSecretKey" required><br>
        <label for="code_input">Enter the code:</label>
        <input type="text" id="code_input" name="code_input" required>
        <button type="submit" style="background-color: #000077; color: #FFFFFF;">Verify Code</button>
    </form>

    <p style="color: #FF0000;">{{ verification_result }}</p>
</div>

</body>
</html>
"""

if __name__ == '__main__':
    app.run()
