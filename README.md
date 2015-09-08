##3 Apriori
Create a python script that implements Agrawal's and Srikan's [A Priori](https://en.wikipedia.org/wiki/Apriori_algorithm) for frequent item set mining and association rule learning over transactional databases. Input would be given in CSV files with the following format:
```
item_11, item_12, ..., item_1n
item_21, item_22, ..., item_2n
...
```
Output should be given in also in CSV files with the following format:
`itemset_1:support;itemset_2:support;...itemset_n:support`
The script should handle the following arguments:
* `-n`:optional. Input items should be handled as numeric instead of strings.
* `-p`:optional. Support should be considered as a percentage of given baskets.
* `-o`:optional. Output should be saved in a separate file. Otherwise, it should be printed.
