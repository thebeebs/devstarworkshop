## Deploy Manually ##

If you are here is because you are a brave Xwing fighter and you dont need help of your R2D2 with the compilation and deployment.
So remember, depending on language you choose different sets of requirements you follow must! ;) In the first part of this page we give you some hints and basic recommendations regarding compilation, testing locally and packaging. In the bottom of the page you'll find a tutorial with basic instructions to then deploy your application into Oracle Application Container Cloud Service.

  **Java: Maven and JDK installed**
  
  Inside the folder where your code is cloned:
  
  To build and compile:
        
         mvn clean package
  
  Then to run or test locally:
  
         java -jar XwingApp-1.0.jar
         
  If sucessfull, your application should be running in *http://localhost:8080*
    
  ***To Zip the final deployable artefact, you should Zip the manifest.json file together with the jar file.***
   
   
   -----------------------------------------------------------------------------------------------------------------
 
  **Node.js: NPM installed**
    
  To run or test locally:
    
         node ./bin/www
         
  If sucessfull, your application should be running in *http://localhost:3000*
    
  ***To Zip the final deployable artefact, you should Zip everything in the xwingnodeclient folder.***
  
  -----------------------------------------------------------------------------------------------------------------

  **PHP: Apache web server and PHP installed**
  
  PHP TBD
  
  -----------------------------------------------------------------------------------------------------------------

Note: At the end of the compilation process -regardless of language choosen - you should have a **zip file** containing the application and the  respective **manifest.json** file to proceed to deployment as explained above.

## Using Application Container Cloud Service console to deploy ##

Here are the steps you'll need to follow:

1) Open the Oracle Application Container Cloud Service Applications page by going to the Dashboard of your Oracle Cloud My Services account.Open the Service Console.

2) Click Create Application.

![alt text](createappaccs01.PNG)

3) Click an application type: Java SE, Node, or PHP.

![alt text](createappaccs02.PNG)

4) Application Artifacts: These are the available options for identifying the application archive location:

Upload — Navigate to and upload your application archive and optionally a manifest file or deployment file. 
Click Browse to upload each of these files. 
Specifying a manifest file is required if your application archive doesn’t include this file.

Important: Please, use allways the same name for the app you deploy! 

![alt text](createappaccs03.PNG)

### Next: Back to Mission ###

[Click here](../missions/deploy.md) to go back to the misison instructions!


