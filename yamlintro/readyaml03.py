#!/usr/bin/env python3

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    ## Open a blob of YAML data
    yammyfile = open("myYAML.yml", "r")
    
    ## convert YAML into Python data structures (lists and dictionaries)
    pyyammy = yaml.load(yammyfile, Loader=yaml.FullLoader)
    
    # display our new Python data
    print(pyyammy)
                
main()

