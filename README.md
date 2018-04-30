# Self-hosted Docker Server Templates

This repository contains what you need to get started self-hosting various services while also giving you a little knowledge around docker and docker-compose.  The templates will set up the following:

* Base
  * [DuckDNS](https://duckdns.org)
  * [Traefik](https://traefik.io)
  * [Portainer](https://portainer.io)
  * [Watchtower](https://hub.docker.com/r/centurylink/watchtower/)
  * [A Postfix Mail Relay](https://hub.docker.com/r/mwader/postfix-relay/)
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
* [Draw.io](https://draw.io)
* [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki)

To-dos

* [ ] [Mailu](https://mailu.io)
* [ ] [Discourse](https://discourse.org)
* [ ] [Riot.im](https://riot.im)
* [ ] [Gitlab](https://about.gitlab.com/)

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
* If your service utilizes email to send registration confirmations, forgotten passwords, user notifications, etc., you will either need to setup and a [gmail account alias](https://support.google.com/mail/answer/22370?hl=en) and use [Google's SMTP server](https://www.digitalocean.com/community/tutorials/how-to-use-google-s-smtp-server) to send emails or use a custom domain with [Mailgun](https://www.mailgun.com/), following their directions to verify your domain and then use their SMTP to send emails.  Alternatively, you can also setup and use [Mailu](https://mailu.io/), but be aware spam email filters *might* think your domain is spammy because they won't recognize it.  If you use Mailgun, you will need to upgrade from free to basic (which is still free if you're forwarding 10,000 emails or less per month) in order to be able to deliver to email addresses other than the one you registered with.  You will need to enter a credit card to upgrade.
* If using Docker for Windows, you must comment out all Linux/Mac specific lines in all docker-compose .yaml files you intend to use and un-comment all Windows-specific lines.  To help you spot them, I have used ### to designate comments in lines you will need to change.
* Many if not most of these templates are written assuming you're running from a Linux environment.  Attempts were made to make the templates compatible with windows, but there is no guarantee that they will work and you're probably better off using Linux, or at least a linux environment.  You can emulate this in Windows using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).  To control Docker for Windows from WSL, follow [these instructions](https://blogs.msdn.microsoft.com/commandline/2017/12/08/cross-post-wsl-interoperability-with-docker/).  Provided helper scripts will be written in Bash shell because that is what I know, therefore, they will only run in a Linux environment.  Docker for windows has a Linux container mode, which runs the containers in a Linux virtual machine using Hyper-V, but this requires Hyper-V and Hyper-V requires a Windows 10 professional or enterprise license and is not available in Windows 10 Home.

## Starting Your Stack

At your system's command prompt, change directory to the base directory your local copy of this repository and run the following command:

`docker-compose -f docker-compose.base.yaml up -d`

This will download the images for and start the base of your stack with basic services.  To add additional services from this repository, add them to the command with additional -f flags e.g.

`docker-compose -f docker-compose.base.yaml -f ./add-ons/docker-compose.NextCloud.yaml -f ./add-ons/docker-compose.RocketChat.yaml up -d`

**Please note:** docker-compose.base.yaml must come first on this list.  All the add-ons build upon this base.  The order of the rest of the files does not matter.

## Some Notes About Mastodon

If you are adding Mastodon to your stack, after you edit add-ons/docker-compose.Mastodon.yaml, updating the version of the mastodon images to one of the tags available on [this page](https://hub.docker.com/r/tootsuite/mastodon/tags/)(e.g. image: tootsuite/mastodon:v2.3.3), you must run the following commands to prepare your Mastodon instance:

```bash
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml up mastodon-db mastodon-redis
docker-compose run --rm mastodon-web rake secret
#copy the output into configs/mastodon.env for the value of SECRET_KEY_BASE
docker-compose run --rm mastodon-web rake secret
#copy the output into configs/mastodon.env for the value of OTP_SECRET
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake mastodon:webpush:generate_vapid_key
#copy the output into configs/mastodon.env for the values of VAPID_PRIVATE_KEY and VAPID_PUBLIC_KEY
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake db:migrate
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web chown -R 991:991 /mastodon/public/assets /mastodon/public/packs /mastodon/public/system
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake assets:precompile
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake mastodon:add_user
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake mastodon:confirm_email USER_EMAIL=your@email
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake mastodon:make_admin USERNAME=yourname
###after running all of the above commands, you can now bring your entire stack up with the up -d command.  Make sure to -f all of your compose files!
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml up -d
```

To update mastodon, change the version in the image: clause of mastodon-web, mastodon-streaming, and mastodon-sidekiq (e.g. image: tootsuite/mastodon:v2.3.3), then run the following commands:

```bash
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml stop mastodon-web mastodon-streaming mastodon-sidekiq
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake db:migrate
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml run --rm mastodon-web rake assets:precompile
###after running all of the above commands, you can now bring your entire stack up with the up -d command.  Make sure to -f all of your compose files!
docker-compose -f docker-compose.base.yaml -f addons/docker-compose.Mastodon.yaml up -d
```

This updates the database to be compatible with the new version and builds any new assets.

For more rake commands, including other administrative commands, refer to [this guide.](https://github.com/tootsuite/documentation/blob/master/Running-Mastodon/List-of-Rake-tasks.md)

## Making Changes to Services/Containers in Your Stack

To make a change to any service or container in your stack without bringing down and recreating them all, simply edit the docker-compose .yaml file that defines it, save, and re-run your docker-compose command from above.  Docker-compose is inteligent enough to only recreate containers/services you edited in the file.  You can also make changes using the edit functionality in the Portainer Docker GUI (included in the base .yaml file), however, it will not be able to automatically resolve if any dependant containers also need to be recreated.

## Removing Your Stack

If you want to bring everything down and remove all service/containers, Docker networks, and Docker volumes, simply run the following, specifying each docker-compose .yaml file you used to create it.

`docker-compose -f docker-compose.base.yaml -f ... -f ... down`

This will delete the entire stack, including data stored in Docker volumes, permanently.  This will not affect volumes which are bind mounted to a container.  Data in bind mounted volumes must be manually deleted.

## Other Docker-compose Commands

Docker-compose can do more than just bring everything up or bring everything down.  To manage your stack from the command line, pleaes refer to the [Docker-compose CLI reference](https://docs.docker.com//compose/reference/)

## For more about self-hosting your own online services

* [/r/HomeServer on Reddit](https://www.reddit.com/r/HomeServer/)
* [/r/selfhosted on Reddit](https://www.reddit.com/r/selfhosted/)
* [Awesome Self-hosted](https://github.com/Kickball/awesome-selfhosted)

## Assorted other links of interest

* [/r/Rad_Decentralization on Reddit](https://www.reddit.com/r/Rad_Decentralization/)
* [/r/Privacy on Reddit](https://www.reddit.com/r/privacy/)
* [/r/WebApps on Reddit](https://www.reddit.com/r/WebApps/)
* [/r/Docker on Reddit](https://www.reddit.com/r/docker/)
* [/r/DevOps on Reddit](https://www.reddit.com/r/devops/)

Finally, please contact me if you find something wrong with any of these configs.  My ability to test them 100% is limited and I don't use 100% of them myself, so these compose files are my best attempt based on reading the documentation for the app or container.
