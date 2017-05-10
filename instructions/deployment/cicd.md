## Continuous Integration and Deployment ##

If you have opted to use this approach, it means you will not to have to worry about compilation, package and deployment. 
Since your code is already cloned, all you need to do is to make a change on it, commit the change to your local repository and push it to the remote original repository in Developer Cloud Service. This will immediatelly trigger Developer Cloud Service continous integration pipeline, which it means that your code will compile, package a zip file and deploy automatically in Oracle Application Container Cloud.

Let's first make a change to make sure that when you push the code, a difference in repositories is identified and the build job is properly triggered.
So, depending on the language you chose, have your code opened and make the suggested change:

 **Node.JS**: Open file *app.js* and in the first line of it insert a comment line with your name and team. 
 
                        eg: //lisa.jones red team

 **Java**: Open file *XwingServlet.java* and in the first line of it insert a comment line with your name and team. 
 
                        eg: /* lisa.jones red team*/

 **PHP**: TBD
 
                        eg: tbd

Save the file.

Depending on what type of git clone approach you've followed, you should now have 2 ways of commiting and pushing your code:

1. git command line

    1.1. run: 
    
       git add .     ,please notice the point(.) at the end of the expression;

    1.2. run: 
    
       git commit     and write a message for the commit;

    1.3. run  
    
       git push       and if successfull, your code should be pushed and commited to the remote repository.
    

2. git Eclipse 

  In Eclipse:
  1. Go to Git Staging view; 
  
  2. You should have visible the file you've changed in the Unstated Changes area. 
  
  3. Drag & Drop the file from the previous point onto Stated Changes area. 
  
  4. Write a nice commit message and click Commit and Push.

After pushing the code to the remote repository in Developer Cloud Service, why don't have a look on the result:
[click here](scale.md) to go to the Developer Cloud Service.

