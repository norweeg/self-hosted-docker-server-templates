# Riot.im Setup

Before running `docker-compose -f base.yml -f add-ons/riot.yml up -d` to bring up your Riot/Matrix servers, you must first generate their config files by running the following:

```bash
#generate the matrix messenge server config files in volume riot-matrix-server-data or the directory mapped to /data in service riot-matrix-server
docker-compose -f base.yml -f add-ons/riot.yml run --rm riot-matrix-server generate
#download a template config.json file and create a blank conf file for the riot service
docker-compose -f base.yml -f add-ons/riot.yml run --rm riot wget -O /data/config.json https://riot.im/develop/config.json
docker-compose -f base.yml -f add-ons/riot.yml run --rm riot touch /data/riot.im.conf
```

Now, you must configure the options in each of these files.  Using your preferred text editor (if you used bind mounts instead of docker volumes for these services), or [vi](https://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/) via the following commands:

```bash
docker-compose -f base.yml -f add-ons/riot.yml run --rm riot-matrix-server vi /data/homeserver.yml
docker-compose -f base.yml -f add-ons/riot.yml run --rm riot vi /data/config.json
docker-compose -f base.yml -f add-ons/riot.yml run --rm riot vi /data/riot.im.conf
```

At the very minimum, you must change some options to match your config in your [.env](../template.env) file.

```yaml
#homeserver.yml.  This is not the complete file, just the minimum edits you will need to make
server_name: "riotdomain.example.com" #change to match RIOT_DOMAIN
listeners:
  - port: 8008
    tls: false
    bind_addresses: ['0.0.0.0'] #changed from default
    type: http
    x_forwarded: true

    resources:
      - names: [client, federation]
        compress: false
# Database configuration
database:
  name: "psycopg2" #change from default
  args: #delete all the default args and add the args below
    database: synapse
    user: YourDBuser #change to match RIOT_MATRIX_DB_USER
    password: YourPassword #change to match RIOT_MATRIX_DB_PASSWORD
    host: matrix-db
enable_registration: True #changed from default
email: #this section is optional, you can leave it commented out in the generated file
   enable_notifs: true #changed from default
   smtp_host: "mail-relay" #changed to the mail-relay service of the template, though any smtp can be used
   smtp_port: 25
   smtp_user: ""
   smtp_pass: ""
   require_transport_security: True
   notif_from: "Your Friendly %(app)s Home Server <noreply@example.com>" #change to match
   app_name: Riot #changed to whatever your want
   # if template_dir is unset, uses the example templates that are part of
   # the Synapse distribution.
   #template_dir: res/templates
   notif_template_html: notif_mail.html
   notif_template_text: notif_mail.txt
   notif_for_new_users: True
   riot_base_url: "https://riotdomain.example.com" #change to match RIOT_DOMAIN
```

Similarly, you must make edits in the config.json file.  Below are the minimum sections you will need to update.  For the full documentation of this file, see [this guide](https://github.com/vector-im/riot-web/blob/master/README.md#configjson)

```json
{
    "default_hs_url": "https://matrix.example.com",
    "brand": "Custom Brand",
    "roomDirectory": {
        "servers": [
            "matrix.example.com",
            "matrix.org"
        ]
    }
}
```

Finally, riot.im.conf.  The author of the container image [did not document this at all](https://github.com/AVENTER-UG/docker-matrix-riot#example-riotimconf), but it seems to work as long as the file exists but is blank, so go figure!

Once you have fully configured your server by editing these files, you can bring it up with  `docker-compose -f base.yml -f ./add-ons/riot.yml up -d`
