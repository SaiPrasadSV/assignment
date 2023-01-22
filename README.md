# Assignment Teachers Directory

A Teacher Directory in which you can create, update or delete Teachers data and Subjects belogs to that Teacher. We can upload/Import bulk teachers data at single go along with teacher profile pics.
You can also search by Last name of teacher and Subject name which he/she taught. 

+  Create, update or delete Teache and Subjects.
+  Search by Last name and Subject Name.

## Main conditions:
+  Teacher First Name and Last name can be same , but email ID will be unique 
+  Teacher should not have more than 5 subjects 
+  If profile pic not available then default profie pic will be loaded  


### Clone this repository
```
git clone https://github.com/saips90/assignment.git
```

## Run the following commands to get started:

+ ### Install PIP library 
```
python -m pip install --upgrade pip
```

+ ### Install virtualenv using pip
```
pip install virtualenv
```
+ ### Create and Activate a new virtual environment 
```
python -m venv teacher_virtual_env
teacher_virtual_env\Scripts\activate
```
+ ### Install dependencies from requirements.txt
```
pip install -r requirements.txt
```
+ ### RUN DB migrations 
```
python manage.py makemigrations
python manage.py migrate
```
+ ### Create superuser or admin user to login
```
python manage.py createsuperuser
```
<br>

## Please find the below functionality from Teacher directory
+ ### Login Page
![signin_page](https://user-images.githubusercontent.com/68495170/213911552-307ad702-5cb5-4c7e-9cd8-4714332667bf.jpg)

+ ### Main page 
![main_page](https://user-images.githubusercontent.com/68495170/213911019-672dcacc-24de-495c-9c1d-1ee42b9b1faf.jpg)

+ ### View/Edit and delete Teacher details
![view_edit_delete_contact](https://user-images.githubusercontent.com/68495170/213911335-4e919c88-6018-4154-b1df-46c69cf95af7.jpg)

+ ### Add Teacher (if profile pic not uploaded then default image will be taken)
![add_teacher](https://user-images.githubusercontent.com/68495170/213911067-141b70a9-844b-404c-9586-0c845423245d.jpg)

+ ### Update Teacher details
![Upload_teacher](https://user-images.githubusercontent.com/68495170/213911083-b32e9d91-6fe5-4b96-bafd-6a523d903fc6.jpg)

+ ### Upload Teacher bulk details (csv file having teacher details and Images will be in zip folder)
![Upload_teacher](https://user-images.githubusercontent.com/68495170/213911150-982fa248-58b8-41a6-87f3-1ad28e0535bb.jpg)

+ ### Error handling during Teacher bulk details Upload
![csv_error](https://user-images.githubusercontent.com/68495170/213911163-8d75fa4b-16b8-4b6b-9ad7-3e4dab936e40.jpg)
![zip_error](https://user-images.githubusercontent.com/68495170/213911179-7d82a647-8000-43eb-8f41-cddae6ec0baa.jpg)

+ ### Search Teacher details with last name and subject which he/she taught 
![search_by](https://user-images.githubusercontent.com/68495170/213911243-e9719071-127a-4143-b848-7c6e1ebba5d0.jpg)

+ ### Created specific subjects tab and where we can see all subjects along wioth teacher details. We have search option as well there with subject name. Teacher can teach only 5 subjects maximum.
![subjects](https://user-images.githubusercontent.com/68495170/213911399-701898cd-660d-4473-b583-fe1ef78555a7.jpg)

