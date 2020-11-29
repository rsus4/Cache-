# Cache-
Cache simulation in python
Cache Simulator

Cache is a fast and small memory used by systems to run efficiently. When some data is needed, we search the cache (may be multi-level) before checking main memory, which is relatively large and slow.

Cache makes use of two properties- spatial and temporal locality. A program tends to refer to the same pieces of information again and again when it runs (for example, loops). Hence a piece of data that was accesses recently has high probability of being accessed again. This is called temporal locality. It is also noted that when we need a piece of data, it is likely that we will soon access the data around it (due to high usage of contiguous structures like arrays). This is called spatial locality.

A cache can be organized in numerous ways, the ones shown here are:

Fully Associative
Direct Mapping
Set Associative
The common features in implementation of the three are:

The program starts by taking the block size (B) and number of cache lines (CL) as input. In case of set associative mapping, it also takes associativity or the number of blocks in any set (N) as input.

In all of these I maintain a tag array and a data array (as python lists), though these are initialized and modified differently.

After this, an infinite loop runs where the functions of read and write can be executed. The loop gets terminated when the user types ‘exit’.

Read

The user provides the memory address (binary) they want to read. If it is present in cache, its contents are printed, otherwise ‘cache miss’ is printed.

Write
The user provided block address (binary) and a block of memory (using a single address here would be absurd, since the cache functions by loading blocks). The data gets written into data array as per the scheme of organization, and tag gets written into tag array.

Fully Associative

This is the most flexible scheme of organization. In this scheme of organization, FIFO orientation is used for storing the blocks. Any block can be stored anywhere in the cache.

Both the tag and data arrays are initialized as empty lists and are filled dynamically when input is received.

Address is divided into tag+offset

READ FUNCTION

We calculate the tag for the address of an element and check if it is present in the tag array. If it is not, we print ‘cache miss’. If it is, we access that index of the data array, and print the required element from the block using the offset. This is highly power consuming since for each block, we need to check all entries.

WRITE FUNCTION

We enter the data we received from user into tag array and data array. If that tag already exists in tag array, we remove the old element and add the new one. If the cache is full, we remove the oldest element that was added and add the new one. This is managed using a queue like implementation using inbuilt pop and insert functions of python lists.

Direct Mapping

Due to the logic associated with each cell, associatively mapped caches tend to be costly. A directly mapped cache reduces the number of entries being checked for one block. This is done by mapping each block to a location in the cache (using the block address).

Tag and data arrays are initialized to be full of -1s (this denotes a garbage value that was initially stored in cache), since we use replacement operations.

Address is divided into tag+index+offset.

READ FUNCTION

We calculate the tag and the offset. Then we calculate where the element will be mapped to and access that cache location. If the tag does not match we print ‘cache miss’. If it matches, we access data array and print required data from the block using offset calculated.

WRITE FUNCTION

The data received from user is entered into the arrays using simple replacement operations in this case

Set associative

Fully associative cache is very flexible and has a high-hit rate, but it consumes high power and the implementation is inefficient. Direct mapping uses less power and works faster, but the hit-rate is low. Hence, we combine aspects of both in the set associative cache. The cache is divided into sets which contain blocks, Address is used to determine which block goes to which set. Due to this we need to search less entries but maintain flexibility, efficiency and save power.

I have organized the cache as lists within lists. Both tag and data arrays were initialized as lists containing as many empty lists as there are sets in the cache.

Address is divided into tag+set index+block offset

READ FUNCTION

We determine the set to which the tag belongs. If the tag is not present in the set, we print ‘cache miss’. If it present in the set, we print the data associated with the address using the offset.

WRITE FUNCTION

We determine the set to which a block gets mapped. The tag array and data array are rigid, but the lists inside them present as sets follow FIFO policy. If the tag is already present in the set, we remove it and insert the tag into tag array and new data into data array. If the set is full, we pop the last element (the one that was added first).
