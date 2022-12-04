#### Hello ! Welcome to my repo to deploy a Flask App with Deta and add some GA tag !

First, install deta,

For windows users :
```
$ iwr https://get.deta.dev/cli.ps1 -useb | iex
```
For mac/linux users :
```
$ curl -fsSL https://get.deta.dev/cli.sh | sh
```

You need to have a deta account and connect with : 
```
$ deta login
```

Go to main.py and change the GA code with yours.
Then deploy the app with : 
```
$ deta deploy
```
Then, jump to your GA account in the Real Time / Overview section and you will see : 

![image](https://user-images.githubusercontent.com/119404054/205500020-757bc843-fea2-41a2-89df-891f399f23ba.png)


GG ! You have deploy a flask app with deta and sync it with your GA account !
