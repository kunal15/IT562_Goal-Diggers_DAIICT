import csv
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()

request_body = {
	    "settings" : {
	        "number_of_shards": 5,
	        "number_of_replicas": 1
	    },

	    'mappings': {
	        'bookmap': {
	            'properties': {
	            	'isbn': {'type': 'text'},
	            	'title': {'type': 'text'},
	            	'original_publication_year': {'type': 'text'},
	                'book_id': {'type': 'text'},
	                'authors': {'type': 'text'},
	                'id': {'type': 'text'}
	            }}}
	}

#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

print("creating 'book_index' index...")
es.indices.create(index = 'book_index7', body = request_body)
es.indices.get_alias("*")
#res = requests.get('http://localhost:9200')
#es.index(index = "book_index", doc_type = "book", id = 5, body = data_dict)
#print(res.content)

with open('books.csv','rU') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='book_index7', doc_type='book')
    
es.search(index="book_index7",body={
        "query" :{
                "match" : {
                        'authors': 'Ann'
                        }
                
                }
        
        })
es.search(index="book_index7",body={
        "query" :{
                "prefix" : {
                        'book_id': '3744'
                        }
                
                }
        
        })
            
es.search(index="book_index7",body={
        "query" :{
                "range" : {
                        'original_publication_year':{ 
                                "gte" : "2001",
                                "lte" : "2003"
                                
                                }
                        }
                
                }
        
        })

es.search(index="book_index7",body={
  "query": { 
    "bool": { 
      "filter": [ 
        { "term":  { "book_id": "37442" }}
      ]
    }
  }
})
            
es.search(index="book_index7",body=
{
    "query": {
        "multi_match" : {
            "query" : "harrry",
            "fields": ["authors", "original_title"],
            "fuzziness": "AUTO"
        }
    },
    "_source": ["authors", "original_title"],
    "size": 50
    
})

request_body_2 = {
	   
	    'mappings': {
	        'bookmap': {
	            'properties': {
	            	'isbn': {'type': 'text'},
	            	'title': {'type': 'text','index_options':'positions'},
	            	'original_publication_year': {'type': 'text','index_options':'freqs'},
	                'book_id': {'type': 'text'},
	                'authors': {'type': 'text'},
	                'id': {'type': 'text'}
	            }}}
	}

        
print("creating 'book_index' index...")
es.indices.create(index = 'book_dataset', body = request_body_2)
es.indices.get_alias("*")
#res = requests.get('http://localhost:9200')
#es.index(index = "book_index", doc_type = "book", id = 5, body = data_dict)
#print(res.content)

with open('books.csv','rU') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='book_dataset', doc_type='book')
    
es.search(index="book_dataset",body={
        "query" :{
                "match" : {
                        'authors': 'Ann'
                        }
                
                }
        
        })
es.search(index="book_dataset",body={
        "query" :{
                "prefix" : {
                        'book_id': '374'
                        }
                
                }
        
        })
            
es.search(index="book_dataset",body={
        "query" :{
                "range" : {
                        'original_publication_year':{ 
                                "gte" : "2004",
                                "lte" : "2006"
                                
                                }
                        }
                
                }
        
        })

es.search(index="book_dataset",body={
  "query": { 
    "bool": { 
      "filter": [ 
        { "term":  { "book_id": "37442" }}
      ]
    }
  }
})
            
es.search(index="book_dataset",body=
{
    "query": {
        "multi_match" : {
            "query" : "hary",
            "fields": ["authors", "original_title"],
            "fuzziness": "AUTO"
        }
    },
    "_source": ["authors", "original_title"],
    "size": 5
    
})
