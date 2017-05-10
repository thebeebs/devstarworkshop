## Mission 4. Destroy the Reactor Core! ##

### Mission Description ###

The spy should now have exposed the secrets of the database where the Death Star stores the coordinates to it's Reactor Core! When our spy returns with the information, find out the coordinates and attack it with your fighter!

### Mission Awards ###

1. The first squad to destroy the core reactor will be awarded **500** points
2. The second squad to destroy the core reactor will be awarded **375** points
3. The third squad to destroy the core reactor will be awarded **250** points
4. The fourth squad to destroy the core reactor will be awarded **125** points

### Mission Instructions ###

1. You should now have recieved information from the spy about the credentials to the Death Star MySQL database where the coordinates for the Core Reactor is kept. Develop a MySQL query that queries the **MissionDatabase** table to retrieve information about the Reactor Core coordinates!

2. When you have the coordinates, hit the Reactor Core at the following URL:
```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/reactorCore/{x-coordinate_goes_here}/{y-coordinate_goes_here}/{Your_squad_name_goes_here}/{Your_microservice_name_goes_here}```. **The Reactor Core will get hit by GET bullets!**
Example: GET ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/reactorCore/45/45/RedSquad/RedXWingJavaclient/```

3. Deploy a new version of your microservice either by using [Continous Integration and Deployment](deployment/cicd.md) or the [manual](deployment/manually.md) approach. 

4. When your updated microservice is live, you could use it to hit the Death Star's iterate endpoint!

5. If you feel that your microservice is not behaving correctly or might not have been deployed correctly, have a look at the logs as described [here](../logs.md). If you are using the Continuous Integration and Deployment strategy, explore the status of your build in Developer Cloud as described [here](../devcs.md)

### Next: End ###

If you haven't already completed the TIE Fighters mission you can do that [here](iterate.md). If you have, your missions are completed! Congratulations!
