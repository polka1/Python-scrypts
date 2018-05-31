# Python-scrypts


# Link path replacer for Django v0.1.1. 

This script will help you integrate any html template to your Django project. 
It instead of you changes the path of the source, which saves a lot of your time

Modify all src links ("*.css", "*.js", and etc) in to the local static src path like:
> "<img class ="img-fluid" src="assets/img/about/img1.jpg" alt=""> " 
to 
> "<img class ="img-fluid" src="{% static 'assets/img/about/img1.jpg' }%" alt="">"

This script can work with pathways like: 
* src="assets/img/about/img1.jpg"
* src="assets/img/blog/img-1.jpg"

### Uses standard libraries. Thus, the script does not need any other manipulations.


# Get started


### Help
Information about available commands.
```
python django-src-replacer.py -h
```
### PATH
For only **single file**.
```
python django-src-replacer.py -f /var/www/path_to_file.html
```

### DIR
To process **multiple files**.
#### WARNING! In the folder should only be html files! The script processes absolutely all files in the directory you specify
#### To use the script safely, use the -f flag to process only one file.
```
python django-src-replacer.py -d /var/www/path_to_dir/templates/
```

### REGEX
You can write **custom regular expression** and add it as a parameter.
Default regex: **'src=+"a+[\w*/]*.\w*.\w*"'**
```
python django-src-replacer.py -r src=+"a+[\w*/]*.[1-5]\w*.\w*"
```

### VARIABLE
You can change the name of the variable specified in the **settings.py**
By default, this is **"static"**
```
python django-src-replacer.py -r 
```

##### Leave comments, criticize and use :)
