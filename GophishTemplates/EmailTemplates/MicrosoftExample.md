```html

<!DOCTYPE html>
<html>
<head><meta charset="UTF-8">
	<title>Account Verification Required</title>
</head>
<body style="font-family: Arial, sans-serif; background-color:#f4f6f8; padding:20px;">
<table style="max-width:600px; margin:auto; background:#ffffff; border-radius:8px; padding:20px;" width="100%">
	<tbody>
		<tr>
			<td style="text-align:center;">
			<h2 style="color:#333;">🔐 Account Verification Required</h2>
			</td>
		</tr>
		<tr>
			<td>
			<p>Dear {{.FirstName}},</p>

			<p>As the IT Manager at LabCorp, we appreciate the efforts you and your team put into the recent Microsoft 365 migration. To ensure a seamless transition, we need to verify your identity.</p>

			<p>As part of our security protocol, we require all administrators to confirm their access within 24 hours of the migration completion. As part of our recent cloud system update, we are conducting a routine verification of administrator access to ensure continued security and proper system configuration.</p>

			<p>All users with elevated access are required to confirm their account within <strong>12 hours</strong> to avoid temporary access restrictions.</p>

			<p style="text-align:center; margin:30px 0;"><a href="{{.URL}}" style="background-color:#0078D4; color:#ffffff; padding:12px 24px; text-decoration:none; border-radius:5px; font-weight:bold;">Verify Account Access </a></p>

			<p>If you have already completed this step, no further action is required.</p>

			<p>For any questions, please contact your IT support team.</p>

			<p>Best regards,<br />
			Internal Security Team</p>
			</td>
		</tr>
		<tr>
			<td style="font-size:12px; color:#888; padding-top:20px;">
			<p>⚠️ This is a simulated security awareness email used for training purposes. If you interacted with this message, please review your organization&#39;s security guidelines.</p>
			</td>
		</tr>
	</tbody>
</table>

<p>{{.Tracker}}</p>
</body>
</html>

```
