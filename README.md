

# Bank_Management_System
## Description
This is a simple API using Flask and MongoDB. The application can perform CRUD operations and store the data in the database
- Flask allows you to build a web application by providing tools, libraries, and technologies. This web application will be a web page, a wiki, or a big web-based calendar application or commercial website. Flask is classified into a micro-framework that means it has little to no dependencies on external libraries.
- MongoDB is an open source NoSQL database management program. NoSQL is used as an alternative to traditional relational databases. NoSQL databases are quite useful for working with large sets of distributed data. MongoDB is a tool that can manage document-oriented information, store or retrieve information.
---
## Pre-requisites
Install Python 3.6 
- [Installation guide on Windows](https://www.tutorialspoint.com/how-to-install-python-in-windows)
- [Installation guide on Unix](https://docs.python-guide.org/starting/install3/linux/)
---
## Getting Started
1. Clone the repository using:
    >git clone https://github.com/code-moro/Bank_Management_System.git

2. Go to console, open the folder and install dependencies from requirements.txt file using:
   >pip install -r requirements.txt
  
3. Install mongodb .You can refer to the official [installation guide of mongodb](https://docs.mongodb.com/manual/installation/).

4. In config.py change your mongodb username and password.

5. Run the run-app.py using:
   >python run-app.py
   
6. [Use Postman to check the endpoints.](https://www.postman.com/downloads/)

---
## API Endpoints

### 1. /createuser
 To create a user using POST method.
 
 The Input format for this endpoint is:
 
 ![Post 1](/Resource/PostRequest.png)
 
 The Successful Output of this endpoint is:
 
 ![Post 2](/Resource/PostSuccessful.png)
 
 If Mobile already exist then the output is:
 
 ![Post 2](/Resource/PostPhoneumber.png)
 
 ---
 
 ### 2. /finduser/<user_id>
 To display a user using GET method.
 
 To get an existing user by User ID using GET method.
 
 ![Post 1](/Resource/GetRequest.png)
 
 The Successful Output of this endpoint is:
 
 ![Post 2](/Resource/GetSuccessful.png)
 
If User ID does not exist then the output is:
 
 ![Post 2](/Resource/GetNotFound.png)
 
 ---
 
 ### 3. /updateuser/<user_id>
 To update data of an existing user by User ID using PUT method.
 
 The Input format for this endpoint is:
 
 ![Post 1](/Resource/PutRequest.png)
 
 The Successful Output of this endpoint is:
 
 ![Post 2](/Resource/PutSucessful.png)
 
 If User ID does not exist then the output is:
 
 ![Post 2](/Resource/PutNotFound.png)
 
 ---
 
 ### 4. /deleteuser/<user_id>
 To delete an existing user by User ID using DELETE method.
 
 The Input format for this endpoint is:
 
 ![Post 1](/Resource/DeleteRequest.png)
 
 The Successful Output of this endpoint is:
 
 ![Post 2](/Resource/DeleteSuccessful.png)
 
 If User ID does not exist then the output is:
 
 ![Post 2](/Resource/DeleteNotFound.png)
 
 ---
 
