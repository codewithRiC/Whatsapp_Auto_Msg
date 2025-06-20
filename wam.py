import pywhatkit
import time

# Your target contacts' numbers
phone_numbers = [           ## Replace with actual phone numbers and can have as many as numbers you need
    "+918888888888",
    "+919999999999"
]

# Message to send
message = """Have a great day! This is a test message sent using pywhatkit.
Feel free to modify it as needed.
You can use multiple lines here.
"""

# Send messages instantly with a delay between them
for i, phone_number in enumerate(phone_numbers):
    # Use 15 seconds delay before sending and 8 seconds close time
    pywhatkit.sendwhatmsg_instantly(
        phone_number, 
        message,
        wait_time=15,  # Wait 15 seconds before sending
        tab_close=True  # Close tab after sending
    )
    
    print(f"Sent message to {phone_number}")
    
    if i < len(phone_numbers) - 1:  # Don't wait after last message
        time.sleep(10)  # Wait 10 seconds between messages
 
        
        