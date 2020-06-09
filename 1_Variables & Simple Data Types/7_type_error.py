# intiger  and float should be converted to string before passing to string concatination
age = 19
message_1 = "happy " + str(age) + "th birthday"
print(message_1)

#or use formatted string
message_3 = f"happy {age}th birthday"
print(message_3)