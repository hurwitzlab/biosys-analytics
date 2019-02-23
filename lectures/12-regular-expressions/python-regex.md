# Regular Expressions

The term "regular expression" is a formal, linguistic term that describes the ability to desc you might be interested to read about (https://en.wikipedia.org/wiki/Regular_language). For our purposes, regular expressions (AKA "regexes" or a "regex") is a way to formally describe some string that we want to find. Regexes are a DSL (domain-specific language) that we use inside Python, just like in the previous chapter we use SQL statements to communite with SQLite. We can `import re` to use the Python regular expression module and use it to search text.

# ENA Metadata

Let's examine the ENA metadata from the XML parsing example:

````
$ ./xml_ena.py *.xml | grep lat | awk '{print $1 "\t" $3}'
attr.lat_lon	27.83387,-65.4906
attr.lat_lon	25.00025,-62.4971
attr.lat_lon	29.3
attr.lat_lon	28.56_-88.70377
attr.isolate	environmental
attr.lat_lon	78
attr.lat_lon	11.46'45.7"
````

We see there are many ways to 
