## Mission 4. Destroy the core database! ##

### Mission Description ###

After destroying the shield your team finds out the coordinates and access credentials of the Death Star central database!

After preparing your xwing with the db credentials, you obtain the endpoint which your squad will now attack!


### Mission Awards ###

1. The first squad to hit the database will be awarded **500** points
2. The second squad to hit the database will be awarded **400** points
3. Subsequent squads will be awarded **300** points

### Mission Instructions ###

2. We now need to fire at the coordinates of the database! Use your selected weapon to implement a function that fires against the shield. This time to get the base URL you first need to access the database and retrieve it from it with a SQL SELECT command! As you get the base URL you can then fire it up as you did in the previous Shield mission: 

```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/shield/{Coordinates_goes_here}/{Your_squad_name_goes_here}/{Your_microservice_name_goes_here}```. The shield will get hit by either GET or POST bullets!
Example: GET ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/shield/943x2323/Red Squad/javaxwingclient```

3. Deploy a new version of your microservice either by using [Continous Integration and Deployment](deployment/cicd.md)![alt text](deployment.png) or the [manual](deployment/manually.md) approach. 

4. When your updated microservice is live, you could use it to hit the Death Star's shield!

### Next: Fifth Mission ###

The Death Star seems to be weaker and weaker.... [Click here](iterate.md) to continue on to the next mission!
