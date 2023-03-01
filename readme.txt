Some points for further explanation:

1. Sessions are used as cheap way to auth user and also to get the pizza we created on the index view. Cheap way of doing it but nice enough
2. I only have two routes to keep it simple and asl oto reduce need for authing the user using the session. Keeps it very eleegnat in routes then.
3. I make my own ModelChoiceField to use when displaying my forms. This lets me display them a bit nicer in the form output on a get request.
4. I use charfield for things like names and addresses to ensure that malicious content cannot slow down lookup on our database.
   256 chars is still enough for any user and can still be scaled up.
5. Custom form-validation is not used in the pizza form due to their being no possible user inputs that are not defined by the database.
6. In the customer validation, names and addresses are not validated to allow for fringe cases such as unicode chars and special chars. these could be in a user or address and so I remain non-opinionated.
