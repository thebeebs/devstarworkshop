## Mission: Deploy your first fighter! ##

Before you start your first mission, make sure you are ready as per below

- [x] You understand the goal of the workshop
- [x] You have grouped together with your squad
- [x] You have received your squad's Identitiy Domain, the username and the password
- [x] You have selected which weapon you, as a member of your squad, will be using
- [x] You are able to clone the source code of your weapon to your local machine. Either by ```git clone``` command or with an IDE with Git support.

### Mission Description ###

In order to take up the battle against the Alien War Ship, your squad would need to deploy at least one space fighter (microservice) to the cloud.

### Mission Awards ###

- Maximum number of points for this mission: **100**
- Lesser points will be given to subsequent squads.

### Mission Instructions ###

1. To deploy your fighter, you will use Continuous Integration and Deployment.
+ In short, the **Continuous Integration and Deployment** strategy means that you push the code from your local machine to the Git repository. Oracle Developer Cloud will then automatically build, package and deploy your application to Application Container Cloud. 

The flow is highlighted below.

[![Continuous](../cicd.png)](../deployment/cicd.md) 

You will not to have to worry about compilation, package and deployment.
Since your code is already cloned, all you need to do is to make a change on it, commit the change to your local repository and push it to the remote original repository in Developer Cloud Service. This will immediately trigger Developer Cloud Service continous integration pipeline, which means that your code will compile, package a zip file and deploy it automatically to Oracle Application Container Cloud.

Let's first make a change to make sure that when you push the code, a difference in the repository is identified and the build job is properly triggered.
So, depending on the language you chose, have your code opened and make the suggested change:

 **Node.JS**: Open the file *xwingnodeclient/app.js* and on the first line insert a comment line with your squad name.

                        eg: // Yellow

 **Java**: Open the file *src/main/java/com/example/rest/App.java* and on the first line insert a comment line with your squad name.

                        eg: // Yellow

 **PHP**: Open the file *index.php* and edit the line on row 2 (below "<php") and insert a comment line with your squad name.

                        eg: // Yellow
<!--
+ Ruby: Ruby and bundler gem installed

 **Ruby**: Open the file *xwingrubyclient/app.rb* and on the first line insert a comment line with your squad name.

                        eg: # Yellow
-->
Save the file.

Depending on what type of git clone approach you've followed, you should now have 2 ways of commiting and pushing your code.

1. Using the Git command line interface

       git add .

   Please notice the point(.) at the end of the expression;

       git commit -m "Your commit message"

       git push

   If successful, your code should be committed and pushed to the remote repository.


2. Using Eclipse with Git

  In Eclipse:
  1. Go to Git Staging view.

  2. You should now see the file you've changed in the Unstaged Changes area.

  3. Drag & Drop the file from the previous point onto Staged Changes area.

  4. Write a nice commit message and click Commit and Push.

After pushing the code to the remote repository in Developer Cloud Service, why don't have a look on the result:
[click here](..deployment//devcs.md) to go to the instructions for Developer Cloud Service.

2. Monitor the Dev Star dashboard to await your fighter being deployed! If you can't see the Dashboard well on the projector/screen, just open the URL from the Excel document. Your space fighter should appear in the dashboard and complete it's first strike to the Alien War Ship!

### Next: Second Mission ###

If your microservice is already up and running [click here](scale.md) to continue on with the next mission!
