# mysql --user=clubayur "-pAXnX4^t123" -e "DROP DATABASE encloud;CREATE DATABASE encloud"
# mysql -u clubayur "-pAXnX4^t123" encloud < encloud.sql
python manage.py collectstatic
rm -rf static/
mv -v gentelella/static/ static/
chmod -R 777 static/
chmod -R 777 media/
service apache2 restart
