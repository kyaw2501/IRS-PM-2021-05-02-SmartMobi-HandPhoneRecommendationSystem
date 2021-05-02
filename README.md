EXECUTIVE SUMMARY 

Mobile phones have become extensions of ourselves, and living without them is almost unimaginable. Work and home life have also merged, with the office always at one’s fingertips. More and more we rely on the keen intelligence that our mobile phones provide, not only for work but also for family time, networking and entertainment. 

There is major potential for improving and tailoring the experience of choosing one’s next mobile. Most people in Singapore choose a phone according to what comes included with the plans offered at their local Telco (e.g. StarHub) shop. Higher-end customers often choose from the well-known brands such as Apple. 

Now though, customer expectations of mobile phones are becoming more specific and differentiated. Some customers focus on high-end cameras, others focus on size, or value for money; still others look for AR/VR compatibility and gaming options. 

Many younger customers desperately want these features, but they can’t yet access the iPhone or Galaxy with their Junior-sized budgets. Without better guidance, they may sacrifice on features and go for a used iPhone, even though lesser known brands exist that offer all the features they want, for a better price.

There is currently an un-tapped opportunity for increased sales of good quality, lesser-known phone brands. Currently though, in a market dominated by giant companies such as Apple, with gigantic marketing budgets, smaller players can’t compete, unless there is better way to get their great products in front of customers.

There is also an up-tapped opportunity for Telco shops to increase their income via a new revenue stream selling lesser-known brands with more sophisticated features, beyond their existing plans offered, as customers will go for higher ticket options if they know these will better fit their needs for the next 2-3 years. 

For this reason we developed an intelligent system to enhance and improve the decision making process for buying a phone, with a B2B business model focused on improving the customer’s buying experience and increasing the technological edge and attractiveness of their shops to new customers. 

This is of potential benefit for customers, mobile phone companies--especially the lesser known mobile phone brands--and Telco Shops (e.g. StarHub). 

Our initial model crawls publicly available mobile phone data available online from retail sites such as www.iprice.sg. 

We added two lucrative B2B revenue streams to support our product; first, with a product for lesser-known mobile phone companies and, second with a product for Telco retailers to give them a technological and customer support edge.

Future applications of our work could further be integrated into mobile phones themselves, as a stand-alone Smartphone App to analyse phone usage and to recommend the best market option when the time comes to purchase a new phone. 

 
2. PROBLEM STATEMENT 
Customer expectations of mobile phones are becoming more specific and differentiated. Some focus on a high-end camera, others focus on size, or value for money; still others look for AR/VR compatibility and gaming options. 

Many younger customers desperately want these features, but they can’t yet access the iPhone or Galaxy with their Junior-sized budgets. Without better guidance, they may sacrifice on features and go for a used Apple phone, even though lesser known brands exist that offer all the features they want, for a better price.

There is currently an un-tapped opportunity for increased sales of good quality, lesser-known phone brands. Currently though, in a market dominated by giant companies such as Apple, with gigantic marketing budgets, smaller players can’t compete, unless there is another way to get their great products in front of customers.

There is also an up-tapped opportunity for Telco shops to increase their income via a new revenue stream selling lesser-known brands with more sophisticated features, beyond their existing plans offered, as customers will go for higher ticket options if they know these will better fit their needs for the next 2-3 years. 


2.1 PROJECT OBJECTIVE 
We aimed to develop an intelligent system to enhance and improve the decision making process for buying a phone, made profitable via a B2B business model focused on improving the customer’s buying experience and increasing the technological edge and attractiveness of lesser known, high quality mobile brands and the Telco retailers who sell them. 

Best Phone will benefit customers, mobile phone companies, especially the lesser known mobile phone brands, and TelShops (e.g. StarHub, Singtel, M1, Circles.Life)

Our initial model crawls the publicly mobile phone data available online from retail sites e.g., www.iprice.sg. We envision three lucrative B2B revenue streams to support our product; first, as a product for lesser-known mobile phone companies and second, as a product to enhance the experience of shopping at local Singapore Telco shops, giving them a technological and customer support edge.

In future development will include a mobile phone app that uses usage data from one’s own phone to predict the Best Phone match for his next purchase, helping both companies and customers to enhance the retail experience.

3 METHODS
We crawled the computer notebook data from the http://www.iprice.sg. We then developed the Database, Front-end System, and Knowledge Base and Rule Engine to support User decision-making.

Our portal feeds into the system architecture based on three divisions: User Preferences, User Purpose and Hard Requirement. The Hard Requirement pillar establishes whether the User would require 5G capability and Fast Charging capability. The User Purpose pillar establishes User preferences around Video Streaming, Outlook and Gaming. The User Preferences pillar establishes the range of budget possible.
 
Figure 1 - Dependency Diagram 


4 SOLUTION OUTLINE 

                                     
Figure 2 – Solution Diagram 

Our solution is a web based smart questionnaire system which draws data from publicly available online retail sites. The front-end is accessed by the user in-store or from home. The back-end comprises the database, Rule Engine. Knowledge Base (KB) and working memory. 

Sample Results


 
4.1 INSTALLATION GUIDE
Windows User
Step 1
Download Node JS and python installer from below link and install into PC
https://nodejs.org/en/download/
https://www.python.org/downloads/release/python-382/

Frontend webpage 
Step 2
Install the package, open command prompt direct to the frontend file directory
 

Step 3
Run “npm run serve” for debug mode then open your browser, copy value from “Local” as shown in below and paste it to browser, the web page will raise up.
 
 

Step 4
Open another command prompt, direct to backend file directory and install the require package using below commands
“ pip install pandas ”
“ pip install flask ”
“ pip install flask_cors ”
“ pip install numpy ”

Step 5
Run the backend api using “python web-api.py” and the program will start running and you can start using the smartphone recommender
 



 
4.2 FEATURES, FUTURE & VALUE ADDS
Information overload is a big problem, for both buyers and retailers. When a customer experiences ‘analysis paralysis’ then he or she is more likely to walk away and look elsewhere to purchase based on a simpler decision-making process such as buying a big-brand phone, e.g. Apple or Samsung. 

We designed and customized an algorithm to solve this problem by providing a simple and attractive User interface that is easily provided for customers at the shops, or directly from home using any web browser, thereby giving Telco businesses and lesser known mobile brands a strategic advantage in the market.

There are many systems for recommending a mobile phone, but these are brand-specific and do not cut across all brands, including the high quality but lesser known brands. This makes our solution more objective and less biased. 

 

Figure 3. Market share of mobile phone brands in Asia

Future: 
The mobile phone industry is booming in Asia Pacific but there is still plenty of room to grow, as market penetration is still lower in Asia compared to other regions. Asia Pacific’s mobile phone boom is fuelled by rising disposable incomes, urbanisation and rural migration to the cities. Best Phone ties in nicely with this growth market, giving added value to brands that aren’t as visible to customers as market giants Apple and Samsung. In future we would further develop a mobile phone app that will analyse the User’s own phone usage data in order to provide recommendations for the next purchase, as well as the best timing to make that purchase.

 
