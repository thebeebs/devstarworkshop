## USING GIT WITH THE COMMAND LINE ##

If you choose Java and you are going to use git command line to import the code, and if you decide to not use an IDE such as Eclipse with a compiler and maven ready to use, you should need to install your own Maven running in your machine in order to debug locally your changes. Otherwise you'll have to rely on Develepor Cloud Service and its Maven. 

So, let's start by locally clone the code you need. At this point you should already have copied the URL for the git remote repository you'll be cloning....

1. Create a local folder in your machine. 

2. From inside that folder run ## git clone ## : e.g: git clone https://URLofRepository/nameOfRepository.git

3. You should need to enter the credentials to the repository. These credentials should have been given to you in a previous step.

4. After having the code cloned, and before pushing any change in order to trigger the build and respective deployment, please create a dummy file inside this folder. This should be enough to trigger the change.

5. After creating the dummy file run ## git add . ## , please notice the point(.) at the end of the expression. 

6. Now run ## git commit ## and write a message for the commit

7. Finally, run ## git push ## and if successfull, your code should be pushed and commited to the remote repository.

