## Results from Customer Conversion Data Science Initiative
The final model produced by the data science team achieved an 8 percentage-point increase in F1 score over the baseline rule-based targeting system. It is able to better discern users who are likely to convert while still casting a sufficiently wide net. For the GStore, this will mean a reduced cost per conversion - achieving more sales than before for a given ad spend. 


![Conversion Model Results](https://github.com/McGill-MMA-EnterpriseAnalytics/Revenue-Radar/blob/main/Images/Conversion_Model_Results.png)

**Improvement Opportunities - Uplift Modeling**

The probability threshold underlying the classification model means that customers who are highly likely to convert are classified as nudge targets. However, there are users whose likelihood is so high that the marginal cost of nudging them is not necessary as they would have purchased anyway. 

![Uplift Client Types](https://www.uplift-modeling.com/en/latest/_images/ug_clients_types.jpg)

To further optimize marketing spend, a causal inference uplift modeling initiative is recommended. This would allow Gstore to identify the users for whom a nudge would be most effective, the "persuadables". It would also yield valuable insights on the users for which nudging could produce negative outcomes "the do not disturbs", which is also inaccessible for models in the classification or propensity category.

To support such an initiative, a dataset of treatment and control groups for nudges and outcomes over a fixed period would be required. 