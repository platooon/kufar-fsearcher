# kufar-searcher
---
I wanted to buy a new GPU but i did`t have enough money to buy it on Onliner. So i decided to buy it on the kufar. Almost all of the variants are overprice but sometimes you can find an extremely attractive offer. Perhaps you will be the first one who notice it but this is usually not the case.

I wrote a code that parses the pages of kufar and sends the necessary ads to my email. I have implemented a verification system so that the mail does not drown in a ton of spam. 
All ads that match the conditions are written to the first and secondary files. If this is not the first launch, then a check occurs with the secondary file where all the ads are stored, if there are matches, then the primary file is cleared, and the message does not come.
