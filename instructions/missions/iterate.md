## Mission 5. Shoot down the TIE Fighters ##

### Mission Description ###

The Death Star has sent out 100 TIE Fighters to attack your fighters! You need to take them down as soon as possible. The mission is completed when a squad has show down all the TIE Fighters.

### Mission Awards ###

1. The first squad to scale a microservice will be awarded **500** points
2. The second squad to scale a microservice will be awarded **375** points
3. The third squad to scale a microservice will be awarded **250** points
4. The fourth squad to scale a microservice will be awarded **125** points

### Mission Instructions ###

1. You should now have recieved information from the spy that will give you the y-coordinates of the TIE Fighters. The example below would shoot down ***one*** of the TIE Fighters. ***The x-coordinate is 45***.

```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/fighters/45/{y-coordinate_goes_here}/{Your_squad_name_goes_here}/{Your_microservice_name_goes_here}```. **The fighters will get hit by GET bullets!**
Example: GET ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/fighters/45/5784358433/RedSquad/RedXWingJavaclient/```

2. Deploy a new version of your microservice either by using [Continous Integration and Deployment](deployment/cicd.md) or the [manual](deployment/manually.md) approach. 

3. When your updated microservice is live, you could use it to hit the Death Star's iterate endpoint!

### Next: End ###

If you haven't already completed the Reactor Core mission you can do that [here](database.md). If you have, your missions are completed! Congratulations!
