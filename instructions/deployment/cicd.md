## Continuous Integration and Deployment ##

If you have opted to use this approach, it means you will not to have to worry about compilation, package and deployment. 
Since your code is already cloned, all you need to do is to make a change on it, commit the change to your local repository and push it to the remote original repository in Developer Cloud Service. This will immediatelly trigger Developer Cloud Service continous integration pipeline, which means that your code will compile, package a zip file and deploy it automatically to Oracle Application Container Cloud.

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
[click here](../devcs.md) to go to the instructions for Developer Cloud Service.

### Next: Back to Mission ###

[Click here](../missions/deploy.md) to go back to the mission instructions!

