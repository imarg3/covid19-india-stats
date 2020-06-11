# Covid-19 Cases in India
 
This source code contains script which displays current Covid-19 cases in India. This script displays all the details in tabular form based on MoHFW website.

## Directly run script
This script can be run directly using Python 3.
- python3 covid19.py (Linux / Mac)
- python covid19.py (Windows)

Please note before installing this script, ensure that you have downloaded following python modules :

- requests
- bs4
- tabulet
- numpy
- matplotlib (optional, if you like to plot graphs)

## Using Dockerfile
If you have docker installed in your machine, you need to pull the image from dockerhub :
- docker pull admincoder/covid19-india
- docker run --rm admincoder/covid19-india

NOTE : admincoder is the name of my DockerHub repository
