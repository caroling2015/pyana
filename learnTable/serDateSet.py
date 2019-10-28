import pandas
#
# airports = pandas.read_csv("airport.csv",header=None,dtype=str)
# airports.columns = ["id","name","city","country","code","icao","latitude","longitude","altitude","offset","dst","timezone"]
# print airports.head()


# airline = pandas.read_csv("airlines.csv",header=None,dtype=str)
# airline.columns = ["id","name","alias","iata","icao","callsign","country","active"]
# print airline.head()


# routes = pandas.read_csv("rounts.csv",header=None,dtype=str)
# routes.columns = ["airline","airline_id","source","source_id","dest","dest_id","codeshare","stops","equipment"]
# routes = routes[routes["dest_id"] != "\\N"]
# print routes.head()

countries = ["USA","CHINA",'FRANCE']
my_data = [10,20,30]

print pandas.Series(my_data,countries)




