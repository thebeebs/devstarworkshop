## Mission 3. Take down the shield! ##

### Mission Description ###

Your squad is ready and it should now have one or more microservices with at least one of them having 2 CPUs.

The Death Star is protected by it's powerful shield. As long as we can't break through the shield, we will have a hard time hitting the core reactors of the Death Star.
To start firing at the shield, we first need to have the Death Star exposing it's coordinates. Keep an eye out on what our spy is saying. It should be in the SPY section of the Dashboard.

### Mission Awards ###

1. The first squad to scale a microservice will be awarded **500** points
2. The second squad to scale a microservice will be awarded **375** points
3. The third squad to scale a microservice will be awarded **250** points
4. The fourth squad to scale a microservice will be awarded **125** points

### Mission Instructions ###

1. Make sure that our spy has reported some more information. If not, you have to wait a bit!
2. We now need to fire at the coordinates of the shield! Use your selected weapon to implement a function that fires against the shield. The base URL of the shield is ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/shield/{x-coordinate_goes_here}/{y-coordinate_goes_here}/{Your_squad_name_goes_here}/{Your_microservice_name_goes_here}```. **The shield will get hit by GET bullets!**
Example: GET ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/shield/43/43/Red Squad/javaxwingclient```
3. Deploy a new version of your microservice either by using [Continous Integration and Deployment](../deployment/deployment.md) or the [manual](../deployment/manually.md) approach. 
4. When your updated microservice is live, you could use it to hit the Death Star's shield!

### Next: Fourth Mission ###

Your squad is now confident to start fighting the Death Star. Be ready, now the real fun starts! [Click here](database.md) to continue on to the next mission!
