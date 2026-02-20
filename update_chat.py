with open('templates/chat.html', 'r') as f:
    content = f.read()

# Add auto-scroll after user message
old_text1 = '''$("#text").val("");
					$("#messageFormeight").append(userHtml);

					$.ajax({'''

new_text1 = '''$("#text").val("");
					$("#messageFormeight").append(userHtml);
					
					// Auto scroll to bottom after user message
					var scrollHeight = $("#messageFormeight")[0].scrollHeight;
					$("#messageFormeight").animate({scrollTop: scrollHeight}, 500);

					$.ajax({'''

content = content.replace(old_text1, new_text1)

# Add auto-scroll after bot response
old_text2 = '''$("#messageFormeight").append($.parseHTML(botHtml));
					});
					event.preventDefault();'''

new_text2 = '''$("#messageFormeight").append($.parseHTML(botHtml));
						
						// Auto scroll to bottom after bot response
						var scrollHeight = $("#messageFormeight")[0].scrollHeight;
						$("#messageFormeight").animate({scrollTop: scrollHeight}, 500);
					});
					event.preventDefault();'''

content = content.replace(old_text2, new_text2)

with open('templates/chat.html', 'w') as f:
    f.write(content)

print('Auto-scroll functionality added successfully!')
