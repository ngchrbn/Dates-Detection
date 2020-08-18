# ***Dates Detection***

A program that uses Regex to detect dates from a file and check
if the dates(if found) are valid

Examples:

==> February can have either 28days or 29 days depending if the year is leap or not

==> January, March, May, July, August, October, December have 31 days

==> April, June, September and November have 30 days

==> A year greater than the present year is not accepted as valid

==> A date detected but with missing leading zero either in day or month is updated to add a zero

==> For example: 
    
    Before
    --> 1/4/2000
    After
    --> 01/04/2000 


***TODO: Add beautifulsoup4 and requests support*** 