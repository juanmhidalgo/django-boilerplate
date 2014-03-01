#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_NAME="{{ project_name }}"

cd $DIR/..
#source $DIR/../env/bin/activate

SETTINGS=dev

if [ -f $PROJECT_NAME/settings/local.py ]; then
	SETTINGS=local
fi

python manage.py runserver --settings=$PROJECT_NAME.settings.$SETTINGS
