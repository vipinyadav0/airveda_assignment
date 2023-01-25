# airveda_assignment
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/vipinyadav0/airveda_assignment.git
$ cd airveda_assignment
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Then run migarte to create database:
```sh
(env)$ python manage.py migrate
```
Then run the server using:
```sh
(env)$ python manage.py runserver
```


<img width="700" alt="Screenshot 2023-01-25 at 6 31 37 PM" src="https://user-images.githubusercontent.com/30477321/214575687-f0ec2d76-7361-4336-a225-abbc227ed18c.png">
<img width="700" alt="Screenshot 2023-01-25 at 6 32 29 PM" src="https://user-images.githubusercontent.com/30477321/214575703-b8c3cbf3-ecfe-4244-a8ae-1f297ebcf42b.png">
<img width="700" alt="Screenshot 2023-01-25 at 6 32 39 PM" src="https://user-images.githubusercontent.com/30477321/214575726-5be798a8-ba47-491b-8f21-a079ecac6536.png">
<img width="700" alt="Screenshot 2023-01-25 at 6 32 46 PM" src="https://user-images.githubusercontent.com/30477321/214575744-7bb653aa-67a7-47ee-ba3c-c5988bb7e523.png">
<img width="700" alt="Screenshot 2023-01-25 at 6 33 01 PM" src="https://user-images.githubusercontent.com/30477321/214575758-8e2c775b-8f91-4e8f-8c64-e5718a3750a1.png">
