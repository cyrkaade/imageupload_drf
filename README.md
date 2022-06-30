# imageupload_drf
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/cyrkaade/imageupload_drf.git

```

--> Move into the directory where we have the project files : 
```bash
cd imageupload_drf

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="https://i.imgur.com/CDXYgPe.png">
</td> 
<td width="50%">
<br>
<p align="center">
###  DRF preview
</p>
<img src="https://i.imgur.com/1UqhrSp.png">  
</td>
</table>

You can go to existing images by their pk, for example: http://127.0.0.1:8000/api/imageupload/1
