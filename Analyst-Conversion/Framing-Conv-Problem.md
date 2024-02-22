## Sales Conversion at the Google Merch Store

### Business Context

The Google Merch Shop is Google's ecommerce site offering branded merchandise across various product categories such as apparel, lifestyle, and stationery. 

Google’s primary business is not selling merchandise.

_“While we sell things like Pixel phones, apps on the Play Store, YouTube subscriptions, and tools for businesses, we make the vast majority of our money from advertising.”_

So, what is the function of the Google Merch Store? 

Companies large and small sell merchandise as a branding activity. Uptake of merchandise helps raise brand awareness – or in Google’s case – maintain brand ubiquity, as well as fostering brand affiliation. 

### Why Conversion? 
With the merchandise store primarily serving a brand affiliation objective for Google, conversion is a key indicator to understand and optimize. The quantity of products sold maps more directly to branding goals, while profit margins come secondarily – ensuring they are maintained to a level that supports the ongoing operation of the store. 

### Objectives of the Data Science Initiative
**Determine which users to target for conversion nudges** 

Calculate probabilities of conversion by user to determine users to prioritize for nudges via targeted advertising. To minimize the marketing cost associated with boosting conversion*, care should be taken to target those for whom the nudge would be most effective. That is, customers showing high enough likelihood of converting for a nudge to have an effect, but not so much that the nudge would be unnecessary. In either case, the cost of that targeted ad would be wasted. 

For the purposes of this experiment*, we define this range of persuadable users as those with a 60%* to 90%* probability of converting. 
[REWORK]

The supervised prediction model should output the expected probability, which should then be used for categorization as “persuadable”. The users within this category can then be prioritized for automated ad bidding.  

The model should be trained and maintained via offline batch learning as this option is more cost effective and fitting for an initiative that is geared toward marketing cost optimization.  

**Increase understanding of the user journey for customers who convert**
As a secondary objective: findings from explainable prediction models over the data science journey towards the conversion prediction model should be collated to help drive prioritization across investments in marketing channels as well as site UX improvements by device. These findings may also be used to drive further data science initiatives (**may take this sentence out**). 

### Measuring Performance of Predictive Model 
The performance of the classification model should be measured by F1 score followed by Brier score [IF POSSIBLE*]. 

F1 score is selected over accuracy given the imbalanced classes and the positive class, conversion, being more important to ascertain. In line with the aim of this initiative to minimize ad spend while driving conversions, the harmonic mean of precision and recall is preferrable to assigning greater weight to either. 

To select between models demonstrating similar F1 scores, Brier scores should be used to distinguish which of them predicts more confidently. Given the imbalanced dataset, Brier score is more suitable for assessing this confidence level than log loss. 

For inclusion in the consideration set, the model should achieve an F1 score 20* percentage points higher than the current rule-based targeting derived from descriptive statistics specified below

* Subcontinent = North America

* Device = Desktop

* Page views on first session >= 16 (median)


For the initiative to have met the business objective, **(WIP – ROI measurement)**









