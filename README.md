## Web crawling
Je montre dans cet article comment configurer un server pour crawler des sites web en utilisant le framework scrapy. 

### Ma configuration
- OS: Debian wheezy
- CPU: 1
- RAM: 3.75G
- Stockage: 10G

#### On met d'abord à jour notre liste de packages.
```sh
sudo apt-get update
sudo apt-get upgrade
```

#### On ajoute les utilusateurs
```sh
sudo su
adduser abdoul
# su - abdoul # pour se connecter en tant que abdoul
```

#### On installe pip, anaconda (python) and virtualenv 
```sh
sudo apt-get install bzip2
wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-2.0.1-Linux-x86_64.sh
bash Anaconda-2.0.1-Linux-x86_64.sh -b # -b stands for batch install
sudo apt-get install build-essential libxml2-dev libssl-dev libffi-dev python-dev libxslt-dev
```

#### On installe mysql 
```sh
sudo apt-get install mysql-server mysql-client python-MySQLdb # mot de passe 1234
```

#### On test le module mysqldb
```sh
python
```

```python
import MySQLdb
exit
```

#### Configurer une base de données mysql pour stocker les données 
 
```sh
# Connexion à la Mysql
mysql --user=root --password=1234  # On se connecte à la base de données
```
```sql
-- On crée un utilisateur
CREATE USER 'abdoul'@'localhost' IDENTIFIED BY 'abdoul'; # On ajoute l'ulisateur abdoul 

-- On crée une base de données
CREATE DATABASE boursorama_database; # On crée une base de données

-- On crée des tables
CREATE TABLE boursorama_database.cours_action (
	tt_id MEDIUMINT NOT NULL AUTO_INCREMENT
	,date_insert TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	,lien VARCHAR(500)
    ,entreprise VARCHAR(500)
    ,valeur_ouverture VARCHAR(500)
    ,derniere_valeur VARCHAR(500)
    ,maximum VARCHAR(500)
    ,minimum VARCHAR(500)
    ,volume VARCHAR(500)
    ,PRIMARY KEY (tt_id)
) ENGINE = InnoDB CHARSET = utf8;

-- On quitte Mysql
exit # on quitte mysql
```

#### On installe scrapy
```sh
sudo apt-get install pip
sudo pip install scrapy
sudo pip install service_identity
scrapy version
```

#### On cree le projet
```sh
mkdir scrapy
cd scrapy
scrapy startproject boursorama
```

#### Utiliser scrapy en mode shell
```sh
scrapy shell http://www.boursorama.com/bourse/actions/cours_az.phtml
```

#### run scrapy après avoir configuré spider
```sh
cd boursorama
scrapy crawl boursorama
```


	
