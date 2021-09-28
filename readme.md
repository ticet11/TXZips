# TX Zips

I was recently contributing to a project that needed Texas data, including zip codes, cities, ip addresses, and others. This is a combination of scripts I wrote to retrieve and format the data and write it to JSON files.

## What's included?

1. **count** - counts and prints the number of unique cities and zips in JSON file to make sure data wasn't lost during the conversion.

2. **csvToJSON** - retrieve, format, and write data from csv file to JSON file.

3. **cumulitiveWeights** - retrieves populations for each zip code from JSON file and writes them, as a cum-weight list, to a JSON file.

4. **getZips** - retrieves a random zip code from JSON file and prints a location dict, including city, state, county, and zip code.

5. **mergeData** - retrieves location data and ip addresses from JSON. Writes location data, including location specific ip ranges to a JSON file. If script doesn't find an ip range for a specific zip code, it will include 2 ip ranges from a list of the most common ip ranges in Texas.

## Attribution

Original csv file obtained from [simplemaps](https://simplemaps.com/data/us-zips), which uses a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/). Original csv has not been altered.

This site or product includes IP2Location LITE data available from <http://www.ip2location.com>.
