# Amazon-Scraped-Reviews-and-Analysis

Will be determing the topic a particular review belongs to based on the score given off by LDA. 

Say, there is a topic distribution #1 = 0.25*topic_1 + 0.25*topic_2  + 0.5*topic_3

Now a review has the following weightage across different topic distributions,

REVIEW = 0.2*topic distribution 1 + 0.4*topic distribution 2 + 0.2*topic distribution 3

So, a score for each topic corresponding to that document will be generated as follows:

0.2*0.25 + 0.4*0.1 + 0.2*0.3 = 0.15 and so on for each topic.

Then we can rank each topic for a particular document and say the max likelihood is that this review is talking about this topic.

P.S : Obviously we will have to take care of stopwords and other commonly occuring words which will not hold any significance in the context of the problem. For e.g. : We are analyzing reviews of a mobile 'Nokia S2'. Now each review ill be talking about the mobile only and will be using terms such as Nokia,mobile,S2,mob etc. So we can remove these terms while doing LDA.

