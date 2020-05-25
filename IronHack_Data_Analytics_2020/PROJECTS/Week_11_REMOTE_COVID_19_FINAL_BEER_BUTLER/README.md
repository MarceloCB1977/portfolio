# Diamonds Predictive Model

Bootcamp's Final Project

## Python libraries imported

For this project i used Pandas, Numpy, Flask, SQLAlchemy, Postgresql, BeautifulSoup and Requests.

### How i did it

I realized that many people never tried Kraft Beer in Brazil, most due to not knowing the styles, what to expect
from those styles as taste and alcohol content, and to the elevated costs.

So i started to research and found a Beer Periodic Table, with all the beer Styles, Famylies and all the
respective features of each style, such as ABV, IBU and SRM.
With BeautifulSoup and resquest trying to web scrap the information.

With that i created a Flask website where the user inputs age, gender and the desired ABV(alcohol content), the IBU(bitternes) and SRM(clarity), using a very popular and common beer as a guideline.
The user get cards with the style name, a beer recommendation(brand and type) from that style and a picture of that beer.
In the back end all the information about the user and the beer recommendation the got, along with the location, it stored into a DataBase.


### Challenges

I shortly found that in Brazil, the websites didn't have all the beer styles, much less all the information
i wanted, harmonization, taste, smell and so on.
I ended up creating a DataFrame by hand, with all the information in the Beer Periodic Table.

### Conclusion

In the near future the plan is to create a Reccomendation Model with Machine Learning, to reccomend beer Styles
by user profile and location, recommending local breweries expading the market.
It's a ever growing market and this innovation it's extremely scalable, prone to great partnerships, sponsorships
and evolution.
