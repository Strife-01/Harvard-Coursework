# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

Random partitioning is a good enough approach if you don't particularily care about the place where the data ends up and if you will scan all the servers anytime you will access the data. Also, it is easier than to come up with a complex load balancing algorithm. Also all the servers have an even probability of being tasked with storing data.
## Partitioning by Hour

Choosing to partition by hour is great for retrieving data because we know the velocity of incoming requests and at what hours but it might be bad for storage as we will end up hogging some servers while underutilizing others.
## Partitioning by Hash Value

It is better for storing values and for retrieving some specified ones but, in case we need all the data from a timerange we will need to query all the servers.
