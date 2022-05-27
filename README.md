# UCB-Pseudosensor-Project-4
This is the second project in "M2M and IoT Interface Design and Protocols" (ECEA 5348), the final weather pseudosensor project (a little variety, please?). Thankfully, almost everything in this project was brand new tech to me (besides Python). I have included a summary pdf:
UCB5348-Pseudosensor-Project2.pdf: Project overview, including requirements, assumptions, and other notes, as well as screenshots of the UI in several scenarios.



# What I learned
Similar to UCB-Pseudosensor-Project-3; much of the tech in this project was totally foreign to me. I love a challenge, and I love learning, so overall this was my favorite project in the series. 

However, for starters, Amazon Web Services (AWS) is a HUGE platform. AWS currently offers over 200 services, of which I only used a handful in this project, and it was still quite a challenge. There are hundreds, (if not thousands or tens of thousands) of tutorials available online, but the downside is that finding information for your specific application can be very time consuming (if it even exists). Luckily, for this project, there were some tangentially-related examples in AWS documentation that were a tremendous help.

The specific services I used for this project were:
### Cloud9:
A user friendly and versatile IDE that integrates well with other AWS services (obviously!). It also supports several programming languages for front-end, back-end, and generic use.
### IoT Thing:
This is simply a representation of a device or entity. In the context of this project, we can think of the "Thing" as a thermocouple or thermometer paired with a hygrometer that measures temperature and humidity on demand.
### SQS queue:
The AWS version of a message queue; data enters the queue via the first Lambda function (Lambda to DDB.py), and is dequeued by the 2nd Lambda function which displays output in the console of a Python client via RESTful API request.
### Lambda:
A "serverless" function that is invoked by an event (e.g. Data Processing, Streaming Analytics), rather than called by code. In my case, two Lambda functions were written; the first routes data from the SQS queue to DynamoDB, and the second reads the data in DynamoDB and routes it to the console of a Python client. 
### Amazon API Gateway:
Allows a connection between the client (getWeather.py in our case), and backend services (Lambda).

At the end of the day, I have mixed feelings about AWS. Granted, everything I did was free, but if you look at previous projects, I was able to accomplish the same things with much less complexity and abstraction. 

# So what was the point of all these projects?
If you look back at each project from ECEA 5347-5348, I essentially accomplished the same task every time, but with different technology:

### 5347 Project 1:
Used Qt to quickly create a UI, and read sensor data with minimal code. That could be very useful if you're looking to pitch a variety of designs without high cost.

### 5347 Project 2:
Same concept as Project 1, except the UI was made with HTML/CSS. As a downside, good-looking website UIs tend to take time and specialized skills to create. On the other hand, if you know what you want, web UIs offer customization options and additional features that you can't get with software like Qt. You can also create very basic web UIs very quickly if needed.

### 5348 Project 1:
This project was a very basic introduction to limited AWS services, as well as the concept of message-queueing, both very useful tools in the IoT world.

### 5348 Project 2:
There is a fairly stepp learning curve when getting used to AWS services (just my opinion, obviously), but the real power of AWS lies in scaling of services. With AWS, a small (or large) business could serve large masses of clients without the need to buy large numbers of expensive servers (AWS is essentially renting servers to businesses). In addition, AWS allows access to complex features that would otherwise have to be coded (and hosted) by said business. Not everyone needs AWS, but their is certainly a growing demand for cloud computing services that AWS provides. So, I'm glad I was introduced to some of it, even if the upfront time investment was a bit high. 

### Though the goal in each project was essentially the same, I think this approach is a great way to introduce students to tools that we will almost certainly use in our careers as embedded engineers.
