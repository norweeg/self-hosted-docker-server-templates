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
* [Mastodon](https://mastodon.social/about) (see also: [Upgrading Mastodon](docs/mastodon.md))
* [Airsonic](https://airsonic.github.io/)
* [ProjectSend](https://www.projectsend.org/)
* [Syncthing](https://syncthing.net/)
* [Draw.io](https://draw.io)
* [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki)
* [Discourse](https://discourse.org)
* [Piwigo](https://piwigo.org/)
* [Gitlab](https://about.gitlab.com/)[&#185;](#notes)
* [Wallabag](https://www.wallabag.org/)
* [Transmission Bittorrent Client Webserver](https://transmissionbt.com/)
* [ytdl (Youtube Downloader)](https://github.com/Algram/ytdl-webserver)
* [Riot.im](https://riot.im) (see also: [Riot.im Setup](docs/riot.md))

To-dos

In no particular order, things I hope to add templates for.  Also taking requests.

* [ ] [VSCode-server](https://coder.com/)
* [ ] [Mailu](https://mailu.io)
* [ ] [OpenVPN](https://openvpn.net/)
* [ ] [Pinry](http://getpinry.com/)
* [ ] [ymarks](https://bitbucket.org/ymarks/ymarks-server)
* [ ] [Mozilla Firefox Sync](https://docs.services.mozilla.com/howtos/run-sync-1.5.html)
* [ ] [Lobsters (link aggregation)](https://lobste.rs/)
* [ ] [Wordpress](https://wordpress.org/)
* [ ] [docker-mailserver](https://github.com/tomav/docker-mailserver)
* [ ] [RSS Monster](https://github.com/pietheinstrengholt/rssmonster)
* [ ] [Nunux Reader](https://reader.nunux.org/welcome)
* [ ] [Nunux Keeper](https://keeper.nunux.org/)
* [ ] [Apache OpenMeetings](https://openmeetings.apache.org/index.html)
* [ ] [Cozy Cloud](https://github.com/cozy/cozy-stack)
* [ ] [edX Platform](https://open.edx.org/)
* [ ] [Moodle](https://moodle.org/)
* [ ] [Sakai](https://www.sakaiproject.org/)
* [ ] [Mahara](https://mahara.org/)
* [ ] [OpenStreetMap](http://www.openstreetmap.org/)
* [ ] [HomeHost](https://github.com/ridhwaans/homehost)
* [ ] [Friends Radio](https://github.com/xouabita/friends-radio)
* [ ] [Volumio](https://volumio.org/)
* [ ] [PeerTube](https://joinpeertube.org/en/)
* [x] ~~[Pushjet](https://pushjet.io/)~~ (project seems to be inactive, homepage is unresponsive)
* [ ] [YouTransfer](http://www.youtransfer.io/)
* [ ] [Onion Share](https://github.com/micahflee/onionshare)
* [ ] [Tag Spaces](https://www.tagspaces.org/)
* [ ] [Flox](https://github.com/devfake/flox)
* [ ] [Lychee](https://lychee.electerious.com/)
* [ ] [Media Goblin](https://mediagoblin.org/)
* [ ] [Open Project](https://www.openproject.org/)
* [ ] [Read the Docs](https://docs.readthedocs.org/en/latest/install.html)
* [ ] [Freedom Box](https://wiki.debian.org/FreedomBox/Features)
* [ ] [FreeNAS](https://www.freenas.org/)
* [ ] [OpenMediaVault](http://www.openmediavault.org/)
* [ ] [WikiSuite](http://wikisuite.org/Chat-and-Video-Conference)
* [ ] [Ghost](https://ghost.org/)
* [ ] [Wekan](https://wekan.github.io/)
* [ ] [Kanboard](https://kanboard.org/)
* [ ] [Tiny tiny RSS](https://tt-rss.org/)
* [ ] [LibrePlan](http://www.libreplan.org/)
* [ ] [Hexo](https://hexo.io/)
* [ ] [Searx](https://asciimoo.github.io/searx/)
* [ ] [Rainloop](https://www.rainloop.net/)
* [ ] [Known](https://withknown.com/)
* [ ] [SoGo](https://sogo.nu/)
* [ ] [Taiga.io](https://taiga.io/)
* [ ] [Logitech Media Server](http://www.mysqueezebox.com/download/)
* [ ] [Moode](http://moodeaudio.org/)
* [ ] A GUI to start and manage a stack created from these templates

## Before You Begin

You will need a computer, preferably running Linux, but anything will do. [&#178;](#notes)  Download and install Docker and Docker-compose following the instructions for your OS

* [Docker](https://www.docker.com/community-edition) (or [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) if you do not have Windows 10 Professional or Enterprise.  See description below.)
* [Docker-Compose](https://docs.docker.com/compose/install/)

Please also, in a developer's text editor e.g. NotePad++, read through docker-compose.base.yaml as it contains detailed instructions in the form of comments.  Before starting your stack, you will need to

* Register for [DuckDNS](https://www.duckdns.org/) and have your subdomain name and token ready
* Forwarded ports 80 and 443 through your router to your host machine
* Read through and get a basic understanding of the configuration options in every .yaml file you intend to use
* Copy template.env to .env with `cp template.env .env` and edit .env to contain your configuration **WARNING: Never commit and push your changes to .env to a public git repository unless you want to get hacked!! You would basically be telling everyone where to find you and telling them your adminstrative passwords if you do!**
* Replace **ALL** placeholder values with your desired configuration following the model of the placeholder in ./configs/traefik.toml and any files in ./configs that are referenced in the docker-compose YAML files you intend to use.  **WARNING: Don't commit and push the changes you make to these files to a public git repository!  See above!**
* Made any other changes to the configuration of a service in a docker-compose .yaml file that you desire e.g. changing the domains to a custom domain that is not a subdomain of duckdns.org
* If your service utilizes email to send registration confirmations, forgotten passwords, user notifications, etc., you will either need to setup and a [gmail account alias](https://support.google.com/mail/answer/22370?hl=en) and use [Google's SMTP server](https://www.digitalocean.com/community/tutorials/how-to-use-google-s-smtp-server) to send emails or use a custom domain with [Mailgun](https://www.mailgun.com/), following their directions to verify your domain and then use their SMTP to send emails.  Alternatively, you can also setup and use [Mailu](https://mailu.io/), but be aware spam email filters *might* think your domain is spammy because they won't recognize it.  If you use Mailgun, you will need to upgrade from free to basic (which is still free if you're forwarding 10,000 emails or less per month) in order to be able to deliver to email addresses other than the one you registered with.  You will need to enter a credit card to upgrade.
* If using Docker for Windows, you must comment out all Linux/Mac specific lines in all docker-compose .yaml files you intend to use and un-comment all Windows-specific lines.  To help you spot them, I have used ### to designate comments in lines you will need to change.
* Docker for Windows requires Hyper-V, which is only available on Windows 10 Professional or Enterprise.  Follow these instructions to [enable Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v).  If you use Windows 10 Home, you will need to install and use [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) to run your containers in a VirtualBox Virtual Machine instead.  Both run your containers inside of a Linux Virtual Machine, which is not as lightweight as a container would be on Linux.
* Many if not most of these templates are written assuming you're running from a Linux environment.  Attempts were made to make the templates compatible with windows, but there is no guarantee that they will work and you're probably better off using Linux, or at least a linux environment.  You can emulate this in Windows using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).  To control Docker for Windows from WSL, follow [these instructions](https://blogs.msdn.microsoft.com/commandline/2017/12/08/cross-post-wsl-interoperability-with-docker/).  Provided helper scripts will be written in Bash shell because that is what I know, therefore, they will only run in a Linux environment.  Docker for windows has a Linux container mode, which runs the containers in a Linux virtual machine using Hyper-V, but this requires Hyper-V and Hyper-V requires a Windows 10 professional or enterprise license and is not available in Windows 10 Home.

### A quick note about Traefik and reverse proxies in general

It may be helpful to understand the role of a reverse proxy.  In short, a reverse proxy is like a web server, except it doen't just serve its own web content, it can also receive requests for MANY web servers/services and forward the requests to the appropriate destination based on critera, such as the host name that was requested (e.g. http://example1.example.com vs http://example2.example.com), or the path of the requested content, if a request going to a single domain may need to go to a different destination for some paths (http://example.com/example/path/to/file/ vs http://example.com/example/api/).  There are many reverse proxies available and available as docker containers (Apache, NGinX, Traefik, and others).  I used [Traefik](https://traefik.io/) in the templates for its ease of use (I understood its configuration better than I did NGinX or Apache), but one could substitute a reverse proxy of their choice if they configure it similarly to how I configured Traefik to work.  Traefik bills itself as being specifically adapted for deploying microservices and is compatible with many tools/infrastructures (specifically Docker, Docker-Compose, and [Let's Encrypt](https://letsencrypt.org/)), and unlike NGinX or Apache which take a static configuration file and cannot change their routing rules on-the-fly, Traefik is able to watch labels you add to containers/services and modify its configuration accordingly without needing to be restarted.  It can, if you configure it to do so, email you if a service goes offline.  The example configurations in these templates are what worked for me, but they may not work in all environments, so you may want to make yourself familiar with the Traefik documentation, specifically these pages:

* [Basics](https://docs.traefik.io/basics/) which details the options which must be configured in a file (configs/traefik.toml) in this repository
* [Commons](https://docs.traefik.io/configuration/commons/) which is more stuff that goes in the config file, but isn't necessarily required, e.g. setting a custom error page
* [ACME (Let's Encrypt) Configuration](https://docs.traefik.io/configuration/acme/) which explains how you can automatically secure your services with free SSL certificates from the Let's Encrypt project
* [Docker](https://docs.traefik.io/configuration/backends/docker/) which details the options you can configure per-service by adding docker labels to it in your docker-compose file

The Traefik documentation is pretty clear and has examples, so my annotations regarding it will be brief.  They even provide a short ["cookbook" of example configurations](https://docs.traefik.io/user-guide/examples/)

## Starting Your Stack

At your system's command prompt, change directory to the base directory your local copy of this repository and run the following command:

`docker-compose -f docker-compose.base.yaml config`

This will check to make sure that the edits you made to any relevant .env files are valid.  You can also do this later as you add more files to your stack with the -f option. (see below)

`docker-compose -f docker-compose.base.yaml up -d`

This will download the images for and start the base of your stack with basic services.  To add additional services from this repository, add them to the command with additional -f flags e.g.

`docker-compose -f docker-compose.base.yaml -f ./add-ons/docker-compose.NextCloud.yaml -f ./add-ons/docker-compose.RocketChat.yaml up -d`

**Please note:** docker-compose.base.yaml must come first on this list.  All the add-ons build upon this base.  The order of the rest of the files does not matter.

## Updating Containers In Your Stack

The service "auto-updater" is included and can automatically update containers who have the label "com.centurylinklabs.watchtower.enable=true".  If you would prefer to control when and to which version you update your containers to, or if the automatic updates are causing you issues taking services offline when they don't start up correctly (health checks have been included on most services to help mitigate this), you can disable the auto-updater on a per-service basis by setting the label "com.centurylinklabs.watchtower.enable=false" on that service.  You can also update services using a scheduled cron job that runs the following commands:

```bash
#This will pull the latest image for each service specified in the -f included yaml files
docker-compose -f docker-compose.base.yaml -f ... pull
#This will recreate containers for any service whose image was updated in the previous command
docker-compose -f docker-compose.base.yaml -f ... up -d
#This will cleanup images which are no longer tagged i.e. a newer version of the image was pulled and the untagged image is not in use by any containers, even if the container itself is not running.  -f here means "force" i.e. do not ask for confirmation before deleting the old image, just do it
docker image prune -f
```

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
* [Awesome Sysadmin](https://github.com/n1trux/awesome-sysadmin)
* [gLibre Services](https://alternativeto.net//list/7451/glibre-services)

## Assorted other links of interest

* [/r/Rad_Decentralization on Reddit](https://www.reddit.com/r/Rad_Decentralization/)
* [/r/Privacy on Reddit](https://www.reddit.com/r/privacy/)
* [/r/WebApps on Reddit](https://www.reddit.com/r/WebApps/)
* [/r/Docker on Reddit](https://www.reddit.com/r/docker/)
* [/r/DevOps on Reddit](https://www.reddit.com/r/devops/)

Finally, please contact me if you find something wrong with any of these configs.  My ability to test them 100% is limited and I don't use 100% of them myself, so these compose files are my best attempt based on reading the documentation for the app or container.

## Tools I Recommend

* [Visual Studio Code](https://code.visualstudio.com/) or, alternatively, its 100% free and open source version [VSCodium](https://vscodium.com/)
  * [Visual Studio Code/VSCodium's support for Docker and Docker-Compose](https://code.visualstudio.com/docs/azure/docker)
  * [How to Run VSCode Remotely on your Server](https://coder.com/)
* [Dockly](https://github.com/lirantal/dockly), a terminal-based Docker GUI which can be run as a container itself (an alternative to the Docker GUI Portainer used in these templates)
* [Micro Text Editor](https://micro-editor.github.io/), a terminal-based text editor with a lot of features, for when you're using SSH to connect to your server
* [Terminus](https://eugeny.github.io/terminus/), my favorite, cross-platform terminal with a support for a variety of shells, including bash on the Windows Subsystem for Linux, though micro and dockly behave strangely in it for some reason.
* [PuTTY](https://www.putty.org/) for when stuff just won't work for me in Terminus
* [Windows Subsystem for Linux](https://lifehacker.com/how-to-get-started-with-the-windows-subsystem-for-linux-1828952698) - enables Windows users have access to the same Unix/Unix-like tools that MacOS and Linux users take for granted
* [GitExtensions](http://gitextensions.github.io/) I maintain this repository using this GUI for Git.  Sommetimes I just need to see what I'm doing graphically

### Notes

&#185; Gitlab is *extremely* resource intensive and tends to leak memory over time.  It probably won't run well on a Raspberry Pi and even on a traditional PC, I have had to schedule cron jobs that periodically restart it due to the memory leaks.  Unsure if this is the result of misconfiguration on my part, or just how the software is.  [↩](#self-hosted-docker-server-templates)

&#178; The images used in these templates are mostly only built by their creators to run on x86_64 (Intel/AMD) processors.  If you are a hoping to host one or more of these services on a Raspberry Pi or similar device and it doesn't run with the template as-written, open an issue to have the file or service adapted for use on ARM processors.  [↩](#self-hosted-docker-server-templates)
