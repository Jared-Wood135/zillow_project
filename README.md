<!-- Title -->
<head>
    <h1 align='center'><b><u><i>
        Zillow Project - README
    </i></u></b></h1>
</head>





<!-- Table of Contents -->
<head>
    <h3 align='center'><b><i>
        <a id='tableofcontents'></a>Table of Contents:
    </i></b></h3>
</head>
<h5>
<li><a href='#description'>Project Description</a></li>
<li><a href='#goals'>Project Goals</a></li>
<li><a href='#hypo'>Hypothesis/Questions</a></li>
<li><a href='#datadict'>Data Dictionary</a></li>
<li><a href='#planning'>Planning</a></li>
<li><a href='#instructions'>Instruction To Replicate</a></li>
<li><a href='#takeaways'>Takeaways</a></li>
</h5>
<br><br><br>




<!-- Project Description -->
<head>
    <h3 align='center'><b><i>
        <a id='description'></a>Project Description:
    </i></b></h3>
</head>
<a href='#tableofcontents'>Back to 'Table of Contents'</a>
<br><br>
<h5>
Using the 'zillow' dataset from a SQL database acquire properties that have a transaction date of 2017 and are single family/single family inferred homes in order to best predict the home's value.
</h5>
<br><br><br>





<!-- Project Goals -->
<head>
    <h3 align='center'><b><i>
        <a id='goals'></a>Project Goals:
    </i></b></h3>
</head>
<a href='#tableofcontents'>Back to 'Table of Contents'</a>
<br><br>
<h5>
<li>Implement Data Science Pipeline</li>
<li>Acquire 'zillow' Dataset</li>
<li>Prepare 'zillow' Dataset</li>
<li>Explore 'zillow' Dataset</li>
<li>Model 'zillow' Dataset</li>
<li>Deliver 'zillow' Dataset</li>
</h5>
<br><br><br>





<!-- Hypothesis/Questions -->
<head>
    <h3 align='center'><b><i>
        <a id='hypo'></a>Hypothesis/Questions:
    </i></b></h3>
</head>
<a href='#tableofcontents'>Back to 'Table of Contents'</a>
<br><br>
<h4><b>
Hypothesis:
</b></h4>
<h5>
Given the 'zillow' dataset at hand, I believe that the location of the home, the contents of the home, as well as it's proximity to key features in the area will be a strong determining factor to accurately predict the home's value.
</h5>
<br>
<h4><b>
Questions:
</b></h4>
<h5>
<li>Do values correlate to the location? (State, county, city, neighborhood)</li>
<li>Do values correlate with the amount of bedrooms and bathrooms</li>
<li>Do values correlate with the size of the home and it's overall property</li>
<li>Does the ratio of the home to overall sqft matter</li>
<li>Does proximity to key features like city center, leisure, stores, etc. matter</li>
<li>Does the local crime rate matter</li>
<li>Does the population density matter</li>
<li>Does proximity to job opportunity density matter</li>
<li>Does proximity to major roads matter</li>
</h5>
<br><br><br>






<!-- Data Dictionary -->
<head>
    <h3 align='center'><b><i>
        <a id='datadict'></a>Data Dictionary:
    </i></b></h3>
</head>
<a href='#tableofcontents'>Back to 'Table of Contents'</a>
<br><br>

| Field Name | Data Type | Data Format | Description | Example |
| ----- | ----- | ----- | ----- | ----- |
|  | object | str | Defines gender of customer | 'Male' |
| bedrooms | float | #.# | Defines the number of bedrooms in the home | 3.0 |
| home_sqft | float | #.# | Defines the total square footage of the home | 2444.0 |
| full_bathrooms | int | # | Defines the number of full bathrooms in the home | 3 |
| lotsize_sqft | float | #.# | Defines the total square footage of the lot the home resides on | 10200.0 |
| home_age | int | # | Defines how old the home is from when it was built to 2017 | 76 |
| value | float | #.# | TARGET VALUE - Defines the home's value | 689354.0 |
| home_lot_ratio | float | #.# | Defines the ratio of the home size to the lot size | 0.24 |
| DUMMY COLS | uint | 0, 1 | Binary (True, False) column for specific column name | 0 |

<br><br><br>






<!-- Planning -->
<head>
    <h3 align='center'><b><i>
        <a id='planning'></a>Planning:
    </i></b></h3>
</head>
<a href='#tableofcontents'>Back to 'Table of Contents'</a>
<br><br>
<h4><b>Planning</b></h4>
<li>This good ol’ thingy</li>
<br>
<h4><b>Acquire</b></h4>
<li>env.file</li>
<li>SQL query</li>
<li>acquire.py</li>
<li>acquire.ipynb</li>
<br>
<h4><b>Prepare</b></h4>
<li>Remove unwanted cols</li>
<li>Aggregate cols</li>
<li>Confirm veracity of cols</li>
<li>prepare.py</li>
<li>prepare.ipynb</li>
<br>
<h4><b>Explore</b></h4>
<li>Determine best cols</li>
<li>Visualize regression lines to target variable</li>
<li>explore.py</li>
<li>explore.ipynb</li>
<br>
<h4><b>Modeling</b></h4>
<li>Linear Regression</li>
<li>LassoLars</li>
<li>TweedieRegressor</li>
<li>Polynomial Regression</li>
<li>Top Model</li>
<li>modeling.py</li>
<li>modeling.ipynb</li>
<br>
<h4><b>Delivery</b></h4>
<li>Final notebook (.ipynb)</li>
<li>final.py</li>
<li>Readme.md</li>
<br><br><br>






<!-- Instructions To Replicate -->
<head>
    <h3 align='center'><b><i>
        <a id='instructions'></a>Instructions To Replicate:
    </i></b></h3>
</head>
<a href='#tableofcontents'>Back to 'Table of Contents'</a>
<br><br>

1. Clone this repo
2. Create 'env.py' file that connects to SQL
3. Run desired .ipynb
<br><br><br>





<!-- Takeaways -->
<head>
    <h3 align='center'><b><i>
        <a id='takeaways'></a>Takeaways:
    </i></b></h3>
</head>
<a href='#tableofcontents'>Back to 'Table of Contents'</a>
<br><br>
<h4><b>Key Findings:</b></h4>

- Adds better predictive value to regression model
    - Number of bedrooms
    - Total sq. ft. of home
    - Number of full bathrooms
    - Total sq. ft. of lot the home is on
    - The age of the home
    - The ratio of the home and lot sq. ft.
<br><br>
<h4><b>Recommendations:</b></h4>

- Increases value
    - Number of bedrooms
    - Total sq. ft. of home
    - Number of full bathrooms
    - The ratio of the home and lot sq. ft.
- Decreases value
    - The age of the home
<br><br>
<h4><b>Takeaways:</b></h4>

- Focus for higher value
    - More bedrooms
    - More full bathrooms
    - Larger home
    - Larger home to lot ratio
<br><br>
<h4><b>If I Had More Time:</b></h4>

- Location specific
    - Difference in states
    - Difference in county
    - Difference in city
    - Difference in neighborhood
- Proximity specific
    - Density of schools
    - Density of entertainment/recreation
    - Density of landmarks/parks
    - Density of retail
    - Density of job opportunity
    - Accessibility
- Community specific
    - Density of population
    - Type of religion
    - Type of residents (Young, middle, old)
    - Type of family structures
    - Ethnic distribution
    - Gender distribution
- Hazard specific
    - Natural disaster risk (Tornado, flood, hurricane, etc.)
    - Crime rate density
    - Type of crime
<br><br>