read -p "Please make sure you have Python 2 and Pip installed. Enter y or Y if confimed: " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # pip install -r requirements.txt
    python manage.py migrate
    echo "Creating admin user with email admin@example.com, password perseusadmin ..."
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@example.com', 'admin@example.com', 'perseusadmin')"
    echo "Creating and importing demo dataset ..."
    python manage.py shell -c "from app.models import Dataset; dataset = Dataset(title='demo', publicized=True, processed=True); dataset.save()"
    python demo.py
    echo "Launching website... Please login using the admin credentials"
    python manage.py runserver 8001 & (
        sleep 3 
        python -mwebbrowser http://localhost:8001)
    trap "exit" INT TERM
    trap "kill 0" EXIT
    tail -f /dev/null
fi