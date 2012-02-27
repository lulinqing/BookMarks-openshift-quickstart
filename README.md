Bookmarks App on OpenShift
===================

This sample Bookmarks App show how easy to deploy a typical Django app on OpenShift in a minute.

Before We Start
---------------

### You need an account on OpenShift

You don't have an account yet? Sign-up and create your account for free : http://www.openshift.com

### Some preparations

Then you need to install 'rhc' client tools following the quickstart on OpenShift website.

Also, make sure you have 'git' and 'django' installed on your machine.

The last step, create a namespace within your account:

    $ rhc domain create -n ${your_namespace} -l ${your_account}

Let't Rock
----------

### Create a python application called "bookmarks" first:

    $ rhc app create -a bookmarks -t python-2.6

And let's add files in this repo into your Bookmarks app:

    $ cd bookmarks
    $ git remote add upstream -m master git://github.com/lulinqing/openshift-bookmarks.git
    $ git pull -s recursive -X theirs upstream master

Then we need mysql database support for your app:

    $ rhc app cartridge add -a bookmarks -c mysql-5.1

### Update for mysql database:

    $ cd wsgi/Bookmarks
    $ vi settings.py

Then update following lines:

    DATABASE_NAME = 'bookmarks'        # change it if you used another app name
    DATABASE_PASSWORD = 'xxxxxxxxxx'    # replace it with your password
    DATABASE_HOST = 'xx.xx.xx.xx'       # replace it with IP of your app

Done. Let's make a little save

    $ git commit -a -m 'update settings.py'
    $ git push

Forwarding remote mysql service port to your local machine

    $ rhc-port-forward -a bookmarks

Prepare your mysql database for app, you can create an user now or choose 'no' to do it later.

    $ ./manage.py syncdb


### Enjoy your Bookmarks App at:

    http://bookmarks-${your_namespace}.rhcloud.com

