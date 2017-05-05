## Mission 3. Take down the shield! ##

### Mission Description ###

Your squad is ready and it should now have one or more microservices with at least one of them having 2 CPUs.

The Death Star is protected by it's powerful shield. As long as we can't break through the shield, we will have a hard time hitting the core reactors of the Death Star.
To start firing at the shield, we first need to have the Death Star exposing it's coordinates. This will happen when half of the other squads making up our army have deployed their first fighters!

### Mission Awards ###

1. The first squad to hit the shield will be awarded **500** points
2. The second squad to hit the shield will be awarded **400** points
3. Subsequent squads will be awarded **300** points

### Mission Instructions ###

1. When half of the squads in our army have been deployed, the Death Star will expose the coordinates of it's shield in the Dashboard. When that has happened, we can continue to step 2.
2. We now need to fire at the coordinates of the shield! Use your selected weapon to implement a function that fires against the shield. The base URL of the shield is ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/shield/{Coordinates_goes_here}/{Your_squad_name_goes_here}/{Your_microservice_name_goes_here}```. The shield will get hit by either GET or POST bullets!
Example: GET ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/shield/943x2323/RedSquad/javaxwingclient```
3. Deploy a new version of your microservice either by using [Continous Integration and Deployment](deployment/cicd.md) or the [manual](deployment/manually.md) approach. 
4. When your updated microservice is live, you could use it to hit the Death Star's shield!

### Next: First Mission ###

Your squad is now confident to start fighting the Death Star. Be ready, not the real fun starts! [Click here](shield.md) to continue on to the next mission!
