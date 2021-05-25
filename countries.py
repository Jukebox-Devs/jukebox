# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:33:46 2021

@author: helen
"""


def countriesList(year):
    if year == 1900:
        countries = ["Argentina", "Austria", "Belgium", "Bhutan", "Bolivia", "Brazil", "Bulgaria", "Canada", 
                     "Chile", "Colombia", "Costa Rica", "Cuba", "Denmark", "Dominican Republic", "Ecuador", 
                     "El Salvador", "Ethiopia", "France", "Germany", "Greece", "Guatemala", "Haiti", "Honduras",
                     "Hungary", "India", "Italy", "Japan", "Liberia", "Mexico", "Montenegro", "Morocco", "Nepal", 
                     "Netherlands", "New Zealand", "Norway", "Panama", "Paraguay", "Peru", "Philippines", "Portugal",
                     "Romania", "Russia", "Serbia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", 
                     "United States", "Uruguay", "Venezuela"]
    elif year == 1910:
        countries = ["Albania", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", 
                     "Belgium", "Bhutan", "Bolivia", "Canada", "Chile", "China", "Colombia", 
                     "Costa Rica", "Cuba", "Czechoslovakia", "Denmark", "Dominican Republic", "Ecuador",
                     "El Salvador", "Estonia", "Ethiopia", "Finland", "France", "Georgia", "Germany", 
                     "Greece", "Guatemala", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Italy",
                     "Japan", "Latvia", "Liberia", "Lithuania", "Mexico", "Mongolia", "Montenegro", 
                     "Morocco", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Norway", "Panama",
                     "Paraguay", "Peru", "Poland", "Portugal", "Romania", "Russia", "Serbia", "South Africa",
                     "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", "United States",
                     "Uruguay", "Venezuela"]
    elif year == 1920:
        countries = ["Albania", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Belgium", 
                     "Bolivia", "Brazil", "Bulgaria", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", 
                     "Czechoslovakia", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
                     "Estonia", "Ethiopia", "Finland", "France", "Georgia", "Germany", "Greece", "Guatemala", 
                     "Haiti", "Honduras", "Hungary", "Iceland", "India", "Ireland", "Italy", "Japan", "Latvia", 
                     "Liberia", "Lithuania", "Mexico", "Mongolia", "Nepal", "Netherlands", "New Zealand", 
                     "Nicaragua", "Norway", "Panama", "Paraguay", "Peru", "Poland", "Portugal", "Romania", 
                     "Soviet Union", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", 
                     "United States", "Uruguay", "Venezuela", "Yugoslavia"]
    elif year == 1930:
        countries = ["Afghanistan", "Albania", "Argentina", "Australia", "Austria", "Belgium", "Bolivia", 
                     "Brazil", "Bulgaria", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Czechoslovakia", 
                     "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia", 
                     "Finland", "France", "Germany", "Greece", "Guatemala", "Haiti", "Honduras", "Hungary", 
                     "Iceland", "India", "Iran", "Iraq", "Ireland", "Italy", "Japan", "Latvia", "Liberia", 
                     "Lithuania", "Mexico", "Mongolia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
                     "Norway", "Panama", "Paraguay", "Peru", "Poland", "Portugal", "Romania", "Saudi Arabia", 
                     "Soviet Union", "Spain", "Sweden", "Switzerland", "Thailand", "Turkey", "United Kingdom", 
                     "United States", "Uruguay", "Yugoslavia"]
    elif year == 1940:
        countries = ["Afghanistan", "Albania", "Argentina", "Australia", "Belgium", "Bhutan", "Bolivia", 
                     "Brazil", "Bulgaria", "Canada", "China", "Colombia", "Costa Rica", "Cuba", "Czechoslovakia", 
                     "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia", 
                     "Finland", "France", "Germany", "Greece", "Guatemala", "Haiti", "Honduras", "Hungary", 
                     "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Japan", 
                     "North Korea", "South Korea", "Latvia", "Lebanon", "Liberia", "Lithuania", "Mexico", 
                     "Mongolia", "Myanmar", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Norway",
                     "Pakistan", "Panama", "Paraguay", "Peru", "Poland", "Portugal", "Romania", "Saudi Arabia", 
                     "Soviet Union", "Spain", "Sweden", "Switzerland", "Syria", "Taiwan", "Thailand", "Turkey", 
                     "United Kingdom", "United States", "Uruguay", "Venezuela", "Yugoslavia"]
    elif year == 1950:
        countries = ["Afghanistan", "Albania", "Argentina", "Australia", "Austria", "Belgium", "Bhutan", 
                     "Bolivia", "Brazil", "Bulgaria", "Cambodia", "Canada", "Chile", "China", "Colombia", 
                     "Costa Rica", "Cuba", "Czechoslovakia", "Denmark", "Dominican Republic", "Ecuador", "Egypt", 
                     "El Salvador", "Ethiopia", "Finland", "France", "East Germany", "West Germany", "Ghana", 
                     "Greece", "Guatemala", "Guinea", "Haiti", "Honduras", "Hungary", "Iceland", "India", 
                     "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Japan", "Jordan", "North Korea", 
                     "South Korea", "Laos", "Lebanon", "Libya", "Mali", "Mexico", "Mongolia", "Morocco", "Myanmar", 
                     "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Norway", "Pakistan", "Panama", 
                     "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Romania", "Saudi Arabia", 
                     "Soviet Union", "Spain", "Sudan", "Sweden", "Syria", "Taiwan", "Thailand", "Tunisia", 
                     "Turkey", "United Kingdom", "United States", "Uruguay", "Venezuela", "Vietnam", "Yugoslavia"]
    elif year == 1960:
        countries = ["Afghanistan", "Albania", "Algeria", "Argentina", "Australia", "Austria", "Belgium", 
                     "Benin", "Bhutan", "Bolivia", "Brazil", "Bulgaria", "Burundi", "Cambodia", "Cameroon", 
                     "Canada", "Chad", "Chile", "China", "Colombia", "Congo", "Costa Rica", "Cuba", "Czechoslovakia", 
                     "Denmark", "Dominican Republic", "Ecuador", "El Savador", "Equatorial Guinea", "Ethiopia", 
                     "Finland", "France", "Gabon", "Gambia", "East Germany", "West Germany", "Ghana", "Greece", 
                     "Guatemala", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", 
                     "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", 
                     "Kenya", "North Korea", "South Korea", "Kuwait", "Laos", "Lebanon", "Lesotho", "Liberia", 
                     "Libya", "Mali", "Mexico", "Mongolia", "Morocco", "Myanmar", "Nepal", "Netherlands", 
                     "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Pakistan", "Panama", "Paraguay", 
                     "Peru", "Philippines", "Poland", "Portugal", "Romania", "Rwanda", "Saudi Arabia", "Senegal", 
                     "Singapore", "Somalia", "South Africa", "Soviet Union", "Spain", "Sudan", "Sweden", 
                     "Swaziland", "Switzerland", "Syria", "Taiwan", "Thailand", "Trinidad and Tobago", "Tunisia", 
                     "Turkey", "Uganda", "United Kingdom", "United States", "Uruguay", "Venezuela", "Vietnam", 
                     "Yugoslavia"]
    elif year == 1970:
        countries = ["Afghanistan", "Albania", "Algeria", "Angolia", "Argentina", "Australia", "Austria", 
                     "Bahamas", "Bangladesh", "Barbados", "Belgium", "Benin", "Bhutan", "Brazil", "Bolivia", 
                     "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Congo", "Costa Rica", 
                     "Cuba", "Czechoslovakia", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", 
                     "Equatorial Guinea", "Ethiopia", "Finland", "France", "Gabon", "Gambia", "East Germany", 
                     "West Germany", "Ghana", "Greece", "Guatemala", "Guyana", "Haiti", "Honduras", "Hungary", 
                     "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", 
                     "Jamaica", "Japan", "Jordan", "Kenya", "North Korea", "South Korea", "Kuwait", "Laos", 
                     "Lebanon", "Lesotho", "Liberia", "Libya", "Malaysia", "Mali", "Malta", "Mauritania", 
                     "Mexico", "Mongolia", "Myanmar", "Nepal", "Netherlands", "New Zealand", "Niger", "Nigeria", 
                     "Norway", "Oman", "Pakistan", "Panama", "Paraguay", "Peru", "Philippines", "Poland", 
                     "Portugal", "Romania", "Rwanda", "Saudi Arabia", "Sierra Leone", "Singapore" ,"Somalia", 
                     "South Africa", "Soviet Union", "Spain", "Sri Lanka", "Sudan", "Suriname" , "Sweden", 
                     "Swaziland", "Switzerland", "Syria", "Taiwan", "Tanzania", "Trinidad and Tobago", "Tunisia", 
                     "Turkey", "UAE", "United Kingdom", "United States", "Uruguay", "Venezuela", "Vietnam", 
                     "Yugoslavia"]
    elif year == 1980: 
        countries = ["Afghanistan", "Albania", "Algeria", "Angolia", "Argentina", "Australia", "Austria", 
                     "Bahamas", "Bangladesh", "Barbados", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", 
                     "Brazil", "Bulgaria", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Congo", 
                     "Costa Rica", "Cuba", "Czechoslovakia", "Denmark", "Dominican Republic", "Ecuador", 
                     "Egypt", "El Salvador", "Equatorial Guinea", "Ethiopia", "Finland", "France", "Gabon", 
                     "Gambia", "East Germany", "West Germany", "Ghana", "Greece", "Guatemala", "Guyana", 
                     "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", 
                     "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kenya", 
                     "North Korea", "South Korea", "Kuwait", "Laos", "Lebanon", "Liberia", "Libya", "Madagascar", 
                     "Malaysia", "Mali", "Malta", "Mexico", "Mongolia", "Morocco", "Myanmar", "Nepal", 
                     "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Pakistan", 
                     "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Romania", "Rwanda", 
                     "Saudi Arabia", "Senegal", "Singapore", "Somalia", "South Africa", "Soviet Union", 
                     "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", 
                     "Taiwan", "Tanzania", "Thailand", "Trinidad and Tabago", "Tunisia", "Turkey", "Uganda", 
                     "UAE", "United Kingdom", "United States", "Uruguay", "Venezuela", "Vietnam", "Yugoslavia", 
                     "Zimbabwe"]
    elif year == 1990:
        countries = ["Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Armenia", "Australia", 
                     "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium", 
                     "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia", "Brazil", "Bolivia", "Bulgaria", 
                     "Belarus", "Cambodia", "Cameroon", "Chad", "Chile", "China", "Colombia", "Congo", 
                     "Costa Rica", "Croatia", "Cuba", "Czech Republic", "Denmark", "Dominican Republic", 
                     "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Estonia", "Ethiopia", "Finland", 
                     "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", 
                     "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", 
                     "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", 
                     "Kazakhstan", "Kenya", "North Korea", "South Korea", "Kuwait", "Kyrgyzstan", "Laos", 
                     "Latvia", "Lebanon", "Libya", "Lithuania", "Madagascar", "Malaysia", "Malta", "Mexico", 
                     "Moldova", "Mongolia", "Morocco", "Myanmar", "Nepal", "Netherlands", "New Zealand", 
                     "Nicaragua", "Niger", "Nigeria", "Norway", "Pakistan", "Panama", "Paraguay", "Peru", 
                     "Philippines", "Poland", "Portugal", "Romania", "Russia", "Rwanda", "Saudi Arabia", 
                     "Senegal", "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa", "Soviet Union", 
                     "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", 
                     "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Trinidad and Tobago", "Tunisia", "Turkey", 
                     "Turkmenistan", "Uganda", "Ukraine", "UAE", "United Kingdom", "United States", "Uruguay", 
                     "Uzbekistan", "Venezuela", "Vietnam", "Yugoslavia", "Zimbabwe"]
    elif year == 2000 or year == 2010 or year == 2020:
        countries = ["Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Armenia", "Australia", 
                     "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium", 
                     "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia", "Brazil", "Bolivia", "Bulgaria", 
                     "Belarus", "Cambodia", "Cameroon", "Chad", "Chile", "China", "Colombia", "Congo", 
                     "Costa Rica", "Croatia", "Cuba", "Czech Republic", "Denmark", "Dominican Republic", 
                     "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Estonia", "Ethiopia", "Finland", 
                     "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", 
                     "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", 
                     "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", 
                     "Kazakhstan", "Kenya", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", 
                     "Laos", "Latvia", "Lebanon", "Libya", "Lithuania", "Madagascar", "Malaysia", "Malta", 
                     "Mexico", "Moldova", "Mongolia", "Morocco", "Myanmar", "Nepal", "Netherlands", "New Zealand", 
                     "Nicaragua", "Niger", "Nigeria", "Norway", "Pakistan", "Panama", "Paraguay", "Peru", 
                     "Philippines", "Poland", "Portugal", "Romania", "Russia", "Rwanda", "Saudi Arabia", 
                     "Senegal", "Serbia", "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa", 
                     "Soviet Union", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", 
                     "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Trinidad and Tobago", 
                     "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "UAE", "United Kingdom", 
                     "United States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yugoslavia", "Zimbabwe"]
    return countries


def allCountries(year):
    return "\n".join(countriesList(year))

def countryExists(country, year):
    countryList = countriesList(year)
    exist = False
    for item in countryList:
        if item == country:
            exist = True
    return exist
