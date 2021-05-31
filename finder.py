#Finds music from musicbrainz based on what the user entered

import os
import musicbrainzngs


musicbrainzngs.set_useragent(os, "0.7.1") #Creates useragent

abbreviations = {"Afghanistan": "AF", "Albania": "AL", "Algeria": "DZ", "Angola": "AO", "Argentina": "AR", 
"Armenia": "AM", "Australia": "AU", "Austria": "AT", "Azerbaijan": "AZ", "Bahamas": "BS", 
"Bahrain": "BH", "Bangladesh": "BD", "Barbados": "BB", "Belarus": "BY", "Belgium": "BE", 
"Belize": "BZ", "Benin": "BJ", "Bhutan": "BT", "Bolivia": "BO", "Bosnia": "BA", "Brazil": "BR", 
"Bulgaria": "BG", "Cambodia": "KH", "Cameroon": "CM", "Canada": "CA","Chad": "TD", 
"Chile": "CL", "China": "CN", "Colombia": "CO", "Congo": "CG", "Costa Rica": "CR", 
"Croatia": "HR", "Cuba": "CU", "Czech Republic": "CZ", "Czechoslovakia": "XC", "Denmark": "DK",  
"Dominican Republic": "DO", "Ecuador": "EC", "Egypt": "EG", "El Salvador": "SV", 
"Equatorial Guinea": "GQ", "Estonia": "EE", "Ethiopia": "ET", "Finland": "FI", "France": "FR", 
"Gabon": "GA", "Gambia": "GM", "Georgia": "GE", "Germany": "DE", "West Germany": "DE", 
"East Germany": "XG", "Ghana": "GH", "Greece": "GR", "Guatemala": "GT", "Guyana": "GY", 
"Haiti": "HT", "Honduras": "HN", "Hungary": "HU", "Iceland": "IS", "India": "IN", 
"Indonesia": "ID", "Iran": "IR", "Iraq": "IQ", "Ireland": "IE", "Israel": "IL", "Italy": "IT",
"Ivory Coast": "CI", "Jamaica": "JM", "Japan": "JP", "Jordan": "JO", "Lithuania": "LT", 
"Madagascar": "MG", "Malaysia": "MY", "Malta": "MT", "Mexico": "MX", "Moldova": "MD", 
"Mongolia": "MN", "Morocco": "MA", "Myanmar": "MM", "Nepal": "NP", "Netherlands": "NL", 
"New Zealand": "NZ", "Nicaragua": "NI", "Niger": "NE", "Nigeria": "NG", "Norway": "NO", 
"Pakistan": "PK", "Panama": "PA", "Paraguay": "PY", "Peru": "PE", "Philippines": "PH", 
"Poland": "PL", "Portugal": "PT", "Romania": "RO", "Russia": "RU", "Rwanda": "RW", 
"Saudi Arabia": "SA", "Senegal": "SN", "Serbia": "RS", "Singapore": "SG", "Slovakia": "SK", 
"Slovenia": "SI", "Somalia": "SO", "South Africa": "ZA", "Soviet Union": "SU", "Spain": "ES",  
"Sri Lanka": "LK", "Sudan": "SD", "Suriname": "SR", "Swaziland": "SZ", "Sweden": "SE", 
"Switzerland": "CH", "Syria": "SY", "Taiwan": "TW", "Tajikistan": "TJ", "Tanzania": "TZ", 
"Thailand": "TH", "Trinidad and Tobago": "TT", "Tunisia": "TN", "Turkey": "TR", 
"Turkmenistan": "TM", "Uganda": "UG", "Ukraine": "UA", "UAE": "AE", "United Kingdom": "GB", 
"United States": "US", "Uruguay": "UY", "Uzbekistan": "UZ", "Venezuela": "VE", "Vietnam": "VN", 
"Yugoslavia": "YU", "Zimbabwe": "ZW"}


def findSongs(country, year): #Finds songs on musicbrainz
    songs = musicbrainzngs.search_releases(country = abbreviations[country], date = year)
    return songs

def queue(songs): #Prints out queue of songs and info about each that will be stored in a dictionary
    pass 
