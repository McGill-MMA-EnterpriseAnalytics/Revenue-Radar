## Sales Conversion at the Google Merch Store

### Business Context

The Google Merch Shop is Google's ecommerce site offering branded merchandise across various product categories such as apparel, lifestyle, and stationery. 

Google’s primary business is not selling merchandise. So, what is the function of the Google Merch Store? 

Companies large and small sell merchandise as a branding activity. Uptake of merchandise helps raise brand awareness – or in Google’s case – maintain brand ubiquity, as well as fostering brand affiliation. 

### Why Conversion? 
With the merchandise store primarily serving a brand affiliation objective for Google, conversion is a key indicator to understand and optimize. The number of people purchasing and sporting their merchandise maps more directly to branding goals, while profit margins come secondarily – ensuring they are maintained to a level that supports the ongoing operation of the store. 

### Objectives of the Data Science Initiative
**Determine which users to target for conversion nudges** 

Leverage predictive classification to determine which users to prioritize for nudges via targeted advertising. A sufficiently performant model would be piloted for automated ad bidding.  

**Increase understanding of the user journey for customers who convert**

As a secondary objective, findings from explainable prediction models over the data science journey towards the conversion prediction model should be collated to help drive prioritization of operational budget across marketing channels and UX improvement work. 

### Measuring Performance of Predictive Model 
The performance of the classification model should be measured by F1 score. 

F1 score is selected over accuracy given the imbalanced classes and the positive class, conversion, being more important to ascertain. In line with the aim of this initiative to minimize ad spend while driving conversions, the harmonic mean of precision and recall is preferrable to assigning greater weight to either. 

For inclusion in the consideration set, a model must achieve an F1 score surpassing the current rule-based targeting derived from descriptive statistics specified below

* Subcontinent = North America

* Device = Desktop

* Page views on first session >= 16 (median)

### Deployment Considerations 
The selected model should be trained and maintained via offline batch learning over a pilot period. This option is more cost effective and fitting for an initiative geared toward marketing cost optimization. Following the pilot period, the option of an online solution may be assessed. 





