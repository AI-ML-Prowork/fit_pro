echo " BUILD START"
python3.9 -m pip install -r requirements.txt

python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

python3.9 manage.py createsuperuser --noinput \
    --username admin \
    --password admin@123
    
python3.9 manage.py collectstatic --noinput --clear
