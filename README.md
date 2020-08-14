A program that uses Regex to detect dates from a file and check
if the dates(if found) are valid
Examples:

==> February can have either 28days or 29 days depending if the year is leap or not

==> January, March, May, July, August, October, December have 31 days

==> April, June, September and November have 30 days

==> A year greater than the present year is not accepted as valid

TODO: Day is in range (01 - 31[ depending on the month]), the month(01 - 12) and the year (1000 - 2999)