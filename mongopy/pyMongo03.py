#!/usr/bin/python3
"""Reading data from MongoDB | RZFeeser@alta3.com"""

from pymongo import MongoClient

def main():
    # Connect to the MongoDB, change the connection string per your MongoDB environment
    client = MongoClient(port=27017)
    
    # Set the db object to point to the business database
    db=client.business
    
    # Showcasing the count() method of find, count the total number of 5 ratings 
    print('The number of 5 star reviews:')
    
    # this returns all reivews that match a 5 star rating
    allmatches = db.reviews.find({"rating": 5})


    total = 0
    # loop across all the matches, counting them as we go
    for fivestar in allmatches:
        total += 1

    print(total)

    # Now let's use the aggregation framework to sum the occurrence of each rating across the entire data set
    print('\nThe sum of each rating occurrence across all data grouped by rating ')
    stargroup=db.reviews.aggregate(
    
    # The Aggregation Pipeline is defined as an array of different operations
    [
    
    # The first stage in this pipe is to group data
    { '$group':
        { '_id': "$rating",
         "count" :
                     { '$sum' :1 }
        }
    },
    
    # The second stage in this pipe is to sort the data
    {"$sort":  { "_id":1}
    }
    # Close the array with the ] tag             
    ] )
    
    # Print the result
    for group in stargroup:
        print(group)
        
if __name__ == "__main__":
    main()

