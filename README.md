# wekkk9-project



## Brief
### Requirements
The requirements the project had to meet were:
- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
  - Service #1: The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.
  - Service #2 + #3 - These will both generate a random “Object”, this object can be whatever you like as we encourage creativity in this project.
  - Service #4 - This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

### Aproach
To fulfill these requiremenst I decided to create an application with 4 main services and an sql service to store the data. what my app does is produce a random string of 2 letters and 2 numbers and produce a prize coresponding to ticket that it was given:
- service 1: front end that the user interact with, initially just shows a button but once click will render a template showing ticket and prize produced.
- service 2: returns a random 2 charcter string.
- service 3: produces a random 2 number from 0 - 99
- service 4: returns the prize depending on teh ticket that was produced.
- database: stores the ticket data and prize 

### Tracking

To keep myself on track I used a Treello board during the developement of My app, though i didnt have specific sprints as i felt as i was working alone i didnt need to specifiy what i would be doing in each sprint.

![Imgur](https://i.imgur.com/U5JZOP5.png)


### Initial Risk assessment
before i started hard coidng the app i didn a breif and quick risk assessment that believed to be teh risks involved with the project, i outlined the potential risks, impacts and possible mitigations that might be needed.



![Imgur](https://i.imgur.com/wB000WG.png)
### Version Control
I used github as teh version control provider, as i am familiar with it asnd i made use of teh branching system with in github as shown below this made shure that if i had made a mistake on a branch that could effect teh whole app it wouldnt effect teh working main branch meaning no down-time. when The pipline was intrudoced i could use a web hook making the approved changes be automatically implemented and built.

![Imgur](https://i.imgur.com/2zma8MQ.png)
## Designs
### App architecture

![Imgur](https://i.imgur.com/Hy4nlFG.png)
### ERD
only a basic table was needed to store the data that will be passed into the data base.
![Imgur](https://i.imgur.com/i9Ydk4O.png)
### First pipeline
the first pipleine shows my first initial built piplein using jenkins and a web hook where i would make a change github would push teh change to jenkins server, jenkins would carry out teh necersary tests and produce a log for it. afte rteh tests it would build and push the image to the artifact repository, using docker and docker hub, and then lastly pull back down teh image to deploy the app on the current virtual machine.

![Imgur](https://i.imgur.com/Xhze8bI.png)
#### Testing
 These images how teh coverage reports of my testing of each service and these tests would be carried out before each new build and deploy.
![Imgur](https://i.imgur.com/jkAQE8Z.png)
![Imgur](https://i.imgur.com/FVK3DwN.png)
![Imgur](https://i.imgur.com/5XVZCnq.png)
![Imgur](https://i.imgur.com/tlatXPr.png)
#### Logging
i used jenkins inbuilt logging and display teh status of each built where green shows that teh stage wwas passed and red signifies a faliure.

![Imgur](https://i.imgur.com/xr3anA8.png)
![Imgur](https://i.imgur.com/qPYvK5w.png)
### Second version
The second version of my pipline i set up docker swarm where teh jenkins machine would be the swarm manager(the machine that links teh other machines together) and deployed my app to the swarm workers in teh docker swarm and used docker stack to deploy teh app to the swarm.  
![Imgur](https://i.imgur.com/GsId9ql.png)
### Third version
this version used ansible to create and configure fresh Vm's that had the jenkins machine public ssh key on it allowing to be ssh'd into it. ansible allowed the configuration of the swarm and the set up pf these machine to be done automatically, allowing teh app to be more portible. also the jenkins machine wasnt teh swarm manager anymore, another machine was designated this role.
![Imgur](https://i.imgur.com/iOZ8Nf9.png)
### Final version
the final version of teh pipline incorporated an nginx container that distributes incoming traffic of teh appp equally across teh swarm.

![Imgur](https://i.imgur.com/8MF1aD3.png)
### network architechture
this is the network achitecture behind the pipeline, showing there was a machine that had jenkins and teh nginx on it with ansible and then dedicated swamr manager and workers.

![Imgur](https://i.imgur.com/Cpkezzh.png)


### end of development risk assessment
i revisited my risk assessment to change and add new risks that where found at the end of the development.
![Imgur](https://i.imgur.com/8VvxT9C.png)
### furture improvements

## Author
George Rhodes

