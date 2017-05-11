## Continuous Integration and Deployment ##

If you have opted to use this approach, it means you will not to have to worry about compilation, package and deployment. 
Since your code is already cloned, all you need to do is to make a change on it, commit the change to your local repository and push it to the remote original repository in Developer Cloud Service. This will immediatelly trigger Developer Cloud Service continous integration pipeline, which means that your code will compile, package a zip file and deploy it automatically to Oracle Application Container Cloud.

Let's first make a change to make sure that when you push the code, a difference in the repository is identified and the build job is properly triggered.
So, depending on the language you chose, have your code opened and make the suggested change:

 **Node.JS**: Open file *xwingnodeclient/app.js* and in the first line of it insert a comment line with your name and team. 
 
                        eg: //lisa.jones red team

 **Java**: Open file *src/main/java/com/example/rest/App.java* and in the first line of it insert a comment line with your name and team. 
 
                        eg: /* lisa.jones red team*/

 **PHP**: TBD
 
                        eg: tbd

Save the file.

Depending on what type of git clone approach you've followed, you should now have 2 ways of commiting and pushing your code:

+1. git command line
  
       git add .
       
   Please notice the point(.) at the end of the expression;
       
       git commit -m "Your commit message"
    
       git push
   
   If successfull, your code should be pushed and commited to the remote repository.
    

+2. git Eclipse 

  In Eclipse:
  1. Go to Git Staging view; 
  
  2. You should have visible the file you've changed in the Unstaged Changes area. 
  
  3. Drag & Drop the file from the previous point onto Staged Changes area. 
  
  4. Write a nice commit message and click Commit and Push.

After pushing the code to the remote repository in Developer Cloud Service, why don't have a look on the result:
[click here](../devcs.md) to go to the instructions for Developer Cloud Service.

### Next: Back to Mission ###

[Click here](../missions/deploy.md) to go back to the misison instructions!

