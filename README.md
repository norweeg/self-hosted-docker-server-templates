# Home Docker Service Templates

This repository contains what you need to get started self-hosting various services while also giving you a little knowledge around docker and docker-compose.  The templates will set up the following:

* Base
  * [DuckDNS](https://duckdns.org)
  * [Traefik](https://traefik.io)
  * [Portainer](https://portainer.io)
  * [Watchtower](https://hub.docker.com/r/centurylink/watchtower/)
* [Pydio](https://pydio.com/)
* [NextCloud](https://nextcloud.com/)
* [Rocket.Chat](https://rocket.chat)
* [Gucamole](https://guacamole.apache.org/)
* [Bookstack](https://www.bookstackapp.com/)
* [Heimdall](https://heimdall.site/)
* [Mastodon](https://mastodon.social/about)
* [Airsonic]( https://airsonic.github.io/)
* [ProjectSend](https://www.projectsend.org/)
* [Syncthing](https://syncthing.net/)

## Before You Begin

You will need a computer, preferably running Linux, but anything will do.  Download and install Docker and Docker-compose following the instructions for your OS

* [Docker](https://www.docker.com/community-edition)
* [Docker-Compose](https://docs.docker.com/compose/install/)

Please also, in a developer's text editor e.g. NotePad++, read through docker-compose.base.yaml as it contains detailed instructions in the form of comments.  Before starting your stack, you will need to

* Register for [DuckDNS](https://www.duckdns.org/) and have your subdomain name and token ready
* Forwarded ports 80 and 443 through your router to your host machine
* Read through and get a basic understanding of the configuration options in every .yaml file you intend to use
* Replaced **ALL** placeholder values with your desired configuration following the model of the placeholder in all docker-compose .yaml files you intend to use and in ./configs/traefik.toml
* Made any other changes to the configuration of a service in a docker-compose .yaml file that you desire e.g. changing the domains to a custom domain that is not a subdomain of duckdns.org
* If using Docker for Windows, you must comment out all Linux/Mac specific lines in all docker-compose .yaml files you intend to use and un-comment all Windows-specific lines.  To help you spot them, I have used ### to designate comments in lines you will need to change.

## Starting Your Stack

At your system's command prompt, change directory to the base directory your local copy of this repository and run the following command:

`docker-compose -f docker-compose.base.yaml up -d`

This will download the images for and start the base of your stack with basic services.  To add additional services from this repository, add them to the command with additional -f flags e.g.

`docker-compose -f docker-compose.base.yaml -f ./add-ons/docker-compose.NextCloud.yaml -f ./add-ons/docker-compose.RocketChat.yaml up -d`

**Please note:** docker-compose.base.yaml must come first on this list.  All the add-ons build upon this base.  The order of the rest of the files does not matter.

## Making Changes to Services/Containers in Your Stack

To make a change to any service or container in your stack without bringing down and recreating them all, simply edit the docker-compose .yaml file that defines it, save, and re-run your docker-compose command from above.  Docker-compose is inteligent enough to only recreate containers/services you edited in the file.  You can also make changes using the edit functionality in the Portainer Docker GUI (included in the base .yaml file), however, it will not be able to automatically resolve if any dependant containers also need to be recreated.

## Removing Your Stack

If you want to bring everything down and remove all service/containers, Docker networks, and Docker volumes, simply run the following, specifying each docker-compose .yaml file you used to create it.

`docker-compose -f docker-compose.base.yaml -f ... -f ... down`

This will delete the entire stack, including data stored in Docker volumes, permanently.  This will not affect volumes which are bind mounted to a container.  Data in bind mounted volumes must be manually deleted.

## Other Docker-compose Commands

Docker-compose can do more than just bring everything up or bring everything down.  To manage your stack from the command line, pleaes refer to the [Docker-compose CLI reference](https://docs.docker.com//compose/reference/)

## For more about self-hosting your own online services:

* [/r/selfhosted on Reddit]{https://www.reddit.com/r/selfhosted/}
* [/r/HomeServer on Reddit]{https://www.reddit.com/r/HomeServer/}

## Assorted other links of interest:

* [/r/Rad_Decentralization on Reddit]{https://www.reddit.com/r/Rad_Decentralization/}
* [/r/Privacy on Reddit]{https://www.reddit.com/r/privacy/}
* [/r/WebApps on Reddit]{https://www.reddit.com/r/WebApps/}
* [/r/Docker on Reddit]{https://www.reddit.com/r/docker/}
* [/r/DevOps on Reddit]{https://www.reddit.com/r/devops/}


Finally, please contact me if you find something wrong with any of these configs.  My ability to test them 100% is limited and I don't use 100% of them myself, so these compose files are my best attempt based on reading the documentation for the app or container. 
