import requests
import re

# a = "https://stepik.org/media/attachments/lesson/24472/sample0.html" #input()
# b = "https://stepik.org/media/attachments/lesson/24472/sample2.html" #input()

a = "https://stepik.org/media/attachments/lesson/24472/sample0.html"
b = "https://stepik.org/media/attachments/lesson/24472/sample1.html"

# a = "https://stepik.org/media/attachments/lesson/24472/sample1.html"
# b = "https://stepik.org/media/attachments/lesson/24472/sample2.html"

# a = "https://stepik.org/media/attachments/lesson/24472/sample1.html"
# b = "https://stepik.org/media/attachments/lesson/24472/sample0.html"

# def c_1(a, b):
#    a_s = re.search(r"\bsample.\b", requests.get(a).text)
#    b_s = re.search(r"\bsample.\b", requests.get(b).text)
#
#    if a_s[0] in b:
#        if b_s[0] in b:
#            print("Yes")
#        else:
#            print("No")
#    elif a_s[0] in a or b_s[0] in a:
#        print("No")
#    else:
#        print("Yes")
#
#c_1(a, b)