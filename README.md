# project4

Group Members: Eduardo Barretto, Nick Binetti, Gabriella Burns, Reid Erwin and Michael Raines

For this project we analyzed four years of consumer loan information to create a machine learning model to predict loan approval based on a combination of nine factors. After cleaning we stored our 15+ Million rows of data in a SQL database hsoted ???   After creating our model we deployed it with a flask server hosted on Heroku. From our bootstrap based webpage we collect user data, send it to our flask server run it through the model and return a prediction of success or failure for loan approval.  Additinally our webpage queries the database and returns comparison results based on the users input comparable to the hsitorical data.

Initial CSV files downloaded from the [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/data-research/hmda/historic-data/?geo=nationwide&records=all-records&field_descriptions=labels)

- [2017](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2017_nationwide_all-records_codes.zip)
- [2016](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2016_nationwide_all-records_codes.zip)
- [2015](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2015_nationwide_all-records_codes.zip)
- [2014](https://files.consumerfinance.gov/hmda-historic-loan-data/hmda_2014_nationwide_all-records_codes.zip)


