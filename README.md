In AWS their are multiple ways to deploy your web app. I will try to briefly explain some of them.
# Build web app 
Build web app is the easiest way to deploy your web app in AWS. Because, The AWS will create the whole environment for you. You just need to upload your code. To get the idea you can just download flask-app. zip from my repository. The file (flask-app. zip) has a whole code file with (requirements.txt) file. The file (requirements.txt) contains all libraries needs for your code to run (e.g. flask, flask-mysql, etc...). The steps to deploy your app are described bellow:
1. open your management concole.
2. Scroll down to Build a Solution.
3. Click on Build a web app.
<img width="919" alt="screen shot 2018-10-17 at 8 50 21 pm" src="https://user-images.githubusercontent.com/31826320/47125232-53cd9a00-d250-11e8-952d-3616e4e3b737.png">

4. Enter your app information. As shown in the picture bellow I enter the name of application is intro and platform I selected python. Then, click on create application. 
<img width="1233" alt="screen shot 2018-10-17 at 8 51 06 pm" src="https://user-images.githubusercontent.com/31826320/47125234-53cd9a00-d250-11e8-8fac-201265a1c20e.png">
5. The application will take a few minutes to be created. Because, the environment has to take time for creating instances.<img width="1270" alt="screen shot 2018-10-17 at 8 52 15 pm" src="https://user-images.githubusercontent.com/31826320/47125235-53cd9a00-d250-11e8-842c-203cce7ee134.png">
6. Click on the link as shown in the picture will open you the website. This link can be used in route53 for the domain. 
<img width="1667" alt="screen shot 2018-10-17 at 9 18 50 pm" src="https://user-images.githubusercontent.com/31826320/47125566-4b765e80-d252-11e8-8ba3-33525d469af0.png">
7. The picture bellow will show you the template that AWS deploy it for you to show you the environment work very well.
<img width="1678" alt="screen shot 2018-10-17 at 9 20 08 pm" src="https://user-images.githubusercontent.com/31826320/47125611-7791df80-d252-11e8-86f5-8703a4c67d12.png">
8. Click on upload and deploy to deploy your app.
<img width="1667" alt="screen shot 2018-10-17 at 9 18 50 pm" src="https://user-images.githubusercontent.com/31826320/47125566-4b765e80-d252-11e8-8ba3-33525d469af0.png">
9. In upload application you should click on choose file and upload zip file that contains your code (e.g. flask-app. zip)
<img width="1467" alt="screen shot 2018-10-17 at 9 23 28 pm" src="https://user-images.githubusercontent.com/31826320/47125703-f129cd80-d252-11e8-83da-009c2a5410d3.png">


                                            Congratulations!!! you have your own app. 

# EC2
Coming Soon!
