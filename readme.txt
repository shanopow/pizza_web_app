Some points for further explanation:

1. Sessions are used as cheap way to auth user and also to get the pizza we created on the index view. Cheap way of doing it but nice enough
2. I only have two routes to keep it simple and asl oto reduce need for authing the user using the session. Keeps it very eleegnat in routes then.
3. I make my own ModelChoiceField to use when displaying my forms. This lets me display them a bit nicer in the form output on a get request.