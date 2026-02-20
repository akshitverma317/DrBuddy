#!/usr/bin/env python
# Fix message merging issue by adding unique IDs to each bot message

with open('templates/chat.html', 'r') as f:
    content = f.read()

# Add message counter at the beginning of script
old_script_start = '\t\t<script>\n\t\t\tfunction typeWriter'
new_script_start = '\t\t<script>\n\t\t\tlet messageCounter = 0;\n\t\t\t\n\t\t\tfunction typeWriter'

content = content.replace(old_script_start, new_script_start)

# Replace the bot message creation with unique IDs
old_bot_message = '''// Create bot message with copy button
						var botHtml = '<div class="d-flex justify-content-start mb-4 message-row"><div class="img_cont_msg"><img src="https://cdn-icons-png.flaticon.com/512/387/387569.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer" style="position: relative;"><button class="copy-btn" data-message="' + data.replace(/"/g, '&quot;') + '"><i class="fas fa-copy"></i> Copy</button><span id="bot-message"></span><span class="msg_time">' + str_time + '</span></div></div>';
						$("#messageFormeight").append(botHtml);
						
						// Streaming text effect
						var messageElement = $("#messageFormeight").find('#bot-message').last()[0];'''

new_bot_message = '''// Create bot message with copy button
						// Create unique ID for this message
						messageCounter++;
						var uniqueId = 'bot-message-' + messageCounter;
						
						var botHtml = '<div class="d-flex justify-content-start mb-4 message-row"><div class="img_cont_msg"><img src="https://cdn-icons-png.flaticon.com/512/387/387569.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer" style="position: relative;"><button class="copy-btn" data-message="' + data.replace(/"/g, '&quot;') + '"><i class="fas fa-copy"></i> Copy</button><span id="' + uniqueId + '"></span><span class="msg_time">' + str_time + '</span></div></div>';
						$("#messageFormeight").append(botHtml);
						
						// Streaming text effect - target specific unique ID
						var messageElement = document.getElementById(uniqueId);'''

content = content.replace(old_bot_message, new_bot_message)

with open('templates/chat.html', 'w') as f:
    f.write(content)

print("✅ Fixed message merging issue - Each bot message now has a unique ID!")
