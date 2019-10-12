# Using Mastdon

## Setup

If you are adding Mastodon to your stack, you must run the following commands to prepare your Mastodon instance:

```bash
docker-compose -f base.yml -f add-ons/mastodon.yml up mastodon-db mastodon-redis
docker-compose run --rm mastodon-web bundle exec rake secret
#copy the output into configs/mastodon.env for the value of SECRET_KEY_BASE
docker-compose run --rm mastodon-web bundle exec rake secret
#copy the output into configs/mastodon.env for the value of OTP_SECRET
docker-compose -f base.yml -f add-ons/mastodon.yml run --rm mastodon-web bundle exec rake mastodon:webpush:generate_vapid_key
#copy the output into configs/mastodon.env for the values of VAPID_PRIVATE_KEY and VAPID_PUBLIC_KEY
docker-compose -f base.yml -f add-ons/mastodon.yml run --rm mastodon-web bundle exec rake db:migrate
docker-compose -f base.yml -f add-ons/mastodon.yml run --rm mastodon-web bin/tootctl accounts create yourusername --email=youremail@example.com
docker-compose -f base.yml -f add-ons/mastodon.yml run --rm mastodon-web bin/tootctl accounts modify yourusername --confirm --approve --enable --role=admin
###after running all of the above commands, you can now bring your entire stack up with the up -d command.  Make sure to -f all of your compose files!
docker-compose -f base.yml -f add-ons/mastodon.yml up -d
```

## Upgrading Mastodon

To update mastodon, change the version in the image: clause of mastodon-web, mastodon-streaming, and mastodon-sidekiq (e.g. image: tootsuite/mastodon:v2.3.3), then run the following commands:

```bash
docker-compose -f base.yml -f add-ons/mastodon.yml stop mastodon-web mastodon-streaming mastodon-sidekiq
docker-compose -f base.yml -f add-ons/mastodon.yml run --rm mastodon-web bundle exec rake db:migrate
###after running all of the above commands, you can now bring your entire stack up with the up -d command.  Make sure to -f all of your compose files!
docker-compose -f base.yml -f add-ons/mastodon.yml up -d
```

This updates the database to be compatible with the new version and builds any new assets.

## Upgrading PostgreSQL Database

Before you update the version of the mastodon-db service, you must first run the following:

```bash
docker-compose -f base.yml -f add-ons/mastodon.yml stop mastodon-web mastodon-streaming mastodon-sidekiq
docker-compose -f base.yml -f add-ons/mastodon.yml exec -u postgres mastodon-db /bin/bash -c "/usr/local/bin/pg_dumpall > /var/lib/postgresql/upgrade/mastodon && rm -Rf /var/lib/postgresql/data/*"
```

This makes a backup of the database and removes the database data so that it can be reinitiallized before restoring the data from the backup.  After doing this, set MASTODON_DB_VERSION in your .env file to your desired version then run:

```bash
docker-compose -f base.yml -f add-ons/mastodon.yml mastodon-db up -d
docker-compose -f base.yml -f add-ons/mastodon.yml exec -u postgres mastodon-db /bin/bash -c "/usr/local/bin/psql -d postgres -f /var/lib/postgresql/upgrade/mastodon"
docker-compose -f base.yml -f add-ons/mastodon.yml up -d mastodon-web mastodon-streaming mastodon-sidekiq
```

This reinitializes the database for the new PostgreSQL version, then restores the data from the backup and bringing Mastodon back up

## Other administrative tasks

For a list of more rake commands, run `docker-compose -f base.yml -f add-ons/mastodon.yml exec mastodon-web bundle exec rake -T`.
For a list of administrative actions that can be run from the command line, run `docker-compose -f base.yml -f add-ons/mastodon.yml exec mastodon-web bin/tootctl help`.
