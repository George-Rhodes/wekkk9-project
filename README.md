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


### Tracking
![Imgur](https://i.imgur.com/U5JZOP5.png)
### Initial Risk assessment
![Imgur](https://i.imgur.com/wB000WG.png)
### Version Control
![Imgur](https://i.imgur.com/2zma8MQ.png)
## Designs
### App architecture
![Imgur](https://i.imgur.com/Hy4nlFG.png)
### ERD
![Imgur](https://i.imgur.com/i9Ydk4O.png)
### First pipeline
![Imgur](https://i.imgur.com/Xhze8bI.png)
#### Testing
![Imgur](https://i.imgur.com/jkAQE8Z.png)
![Imgur](https://i.imgur.com/FVK3DwN.png)
![Imgur](https://i.imgur.com/5XVZCnq.png)
![Imgur](https://i.imgur.com/tlatXPr.png)
#### Logging
![Imgur](https://i.imgur.com/xr3anA8.png)
![Imgur](https://i.imgur.com/qPYvK5w.png)
### Second version
![Imgur](https://i.imgur.com/GsId9ql.png)
### Third version
![Imgur](https://i.imgur.com/iOZ8Nf9.png)
### Final version
![Imgur](https://i.imgur.com/8MF1aD3.png)
### network architechture
![Imgur](https://i.imgur.com/Cpkezzh.png)
### stages of pipeline

### end of development risk assessment
![Imgur](https://i.imgur.com/8VvxT9C.png)
### furture improvements

## Author
George Rhodes

