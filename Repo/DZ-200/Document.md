# Azure Data Engineering
## CosmoDB
  ### What is CosmoDB?
       CosmoDB is globally distributed and multi model database.  
	   It scales for high volume and velocity.It handles high throughput and low latency.
	   Logical flow would be create database, container and insert values.
	   CosmoDB automatically indexing on all the fields.
  
  ### Two things to consider when creating cosmodb
      * scalability (for handling high volume)
	  * throughput (for meeting demands)
	  
  #### Scalablity
        Scalablity (scale out/horizontal scaling) can be achieved by choosing right partitioning.
		Partion key should consider when we build container.
        For instance,if we build online retailer,you can choose either customerid or productid.
        If customer do transaction,to know personalize settings then that thier request should be treated separately in order to reduce latency.
        so data in this case should be distributed based on customerid.
        IF cusotmer are searching inventory then productid would be the right choice.
        There is a limit in physical parttion 10 GB,so we need to consider composite fields to create a partition key.(Customerid and date)
		
  ### Throughput (Request Unit).
      Request unit defines how the data transfer happens.Basically throughput.
	  Request unit needs to be defined when container/ database created. This can be scaled up/down based on thier demands later.
	  Determine the request unit:
	    1. Amount of data transfer.
		2. kind of operations performed(GET/PUT/POST/DELETE).
		3. Indexing property(In order to reduce usage of request unit, choose the required fields for indexing)
		4. Item property count.
  ### Rate-limit
       If your application requests meets the provisioned request unit,then rate-limit blocks the further transaction,retry based on the time specified in the 
       application.From customer view,likely be high latency.	   
		
	  
  
