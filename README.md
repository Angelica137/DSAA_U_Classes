# Exercise 1

Assume that the current month is April, and you want to use a Person class to help make use of information about the friends in your contacts list. In particular, you'd like to increment the age of all of your friends with birthdays in April. You would also like to know who they are, along with their current ages, so you can send them birthday cards. Finally, you would also like to figure out which month has the most friends with birthdays, so you can budget for all of the birthday cards you will need to buy.

In the following exercise, the Person class will be provided for you, and you will be working with a list of instances of the class, representing friends in your contacts. This list is stored in the variable people.

To complete the exercise, you will need to do two things:

Complete the function get_april_birthdays(people). This function should return a dictionary with each name of your friend with an April birthday as a key, and their updated age as the value.
Complete the function get_most_common_month(people). This function should return the name of the month with the most number of birthdays among your friends.
There is some testing code provided in test(), and there are more specific TODO instructions in each of the two functions mentioned.