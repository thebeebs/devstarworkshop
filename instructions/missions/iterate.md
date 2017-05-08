## Mission 5. Iterate the base URL! ##

### Mission Description ###

In this mission you have to develop a function "smart" enough to discover the real endpoint! The real base URL will be hidden among a list of several fake base URL's! 


### Mission Awards ###

1. The first squad to hit the real base URL will be awarded **500** points
2. The second squad to hit the real base URL will be awarded **400** points
3. Subsequent squads will be awarded **300** points

### Mission Instructions ###

1. After getting a set of possible base URL's to hit, your team will need to develope a loop function (for or while to iterate along the possible values). Your function should iterate and concatenate until finding the base URL. Example:

```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/fighters/{x-coordinate_goes_here}/{y-coordinate_goes_here}/{Your_squad_name_goes_here}/{Your_microservice_name_goes_here}```. The shield will get hit by either GET or POST bullets!
Example: GET ```https://ds-backend-gse00010206.apaas.em2.oraclecloud.com/fighters/22/22/Red Squad/javaxwingclient/```

2. Deploy a new version of your microservice either by using [Continous Integration and Deployment](deployment/cicd.md) or the [manual](deployment/manually.md) approach. 

3. When your updated microservice is live, you could use it to hit the Death Star's iterate endpoint!

### Next: End ###

To be continued...
