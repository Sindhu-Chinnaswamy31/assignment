from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    data="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body bgcolor="green">  
        <br>  
        <br>  
        <form>  
        <h1>LOGIN PAGE</h1> 
        Email:  
        <input type="email" id="email" name="email"/> <br>    
        <br> <br>  
        Password:  
        <input type="Password" id="pass" name="pass"> <br>   
        <br> <br>  
        Re-type password:  
        <input type="Password" id="repass" name="repass"> <br> <br>  
        <input type="button" value="Submit"/>  
        </form>  
</body>
</html>
    """
    return HttpResponse(data)