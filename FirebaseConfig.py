import urllib.request
import pyrebase
import urllib3

firebaseConfig = {'apiKey': "AIzaSyAac0RhFD_luIkl05jhfoXbfWRtqt3R4d0",
                  'authDomain': "smarthome-d601c.firebaseapp.com",
                  'projectId': "smarthome-d601c",
                  'storageBucket': "smarthome-d601c.appspot.com",
                  'messagingSenderId': "240020175173",
                  'appId': "1:240020175173:web:1c574fa74c8e89e75c662c",
                  'measurementId': "G-C78S201Z2B",
                  'databaseURL': "https://fir-#######-rtdb.europe-##########.app/"
                  }
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

"""login"""
# email = input("Enter your email")
# password = input("Enter your pass")
# try:
# auth.sign_in_with_email_and_password(email, password)
# print("succesfully")
# except:
# print("OMG")

"""sigup"""
# email = input("Enter your email")
# password = input("Enter your password")
# confirmpass = input("confirm pass")
# if confirmpass == password:
#    try:
#       auth.create_user_with_email_and_password()
#       print("awsome!!")
#    except:
#       print("Please try again")


# upload file cục bộ lên cloud và hiện đường dẫn tới đó
# filename = input("File muốn upload lên cloud")
# cloudfilename = input("Đặt tên file trên cloud")
# storage.child(cloudfilename).put(filename)
# print(storage.child(cloudfilename).get_url(None))


# Tải file trên cloud về máy và đặt tên là download.txt
# cloudfilename = input("Nhập tên file muốn tải")
# storage.child(cloudfilename).download("", "download.txt")


# Đọc file
# cloudfilename = input("Nhập tên file muốn tải")
# url = storage.child(cloudfilename).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)


# Database
data = {'Age': 23, 'Address': "Ha Noi", 'email': "ahihi@gmail.com", 'employed': True, 'Name': "Cuong"}
db.push(data)
