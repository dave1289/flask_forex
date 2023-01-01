### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is mostly from back-end purposes while plain javascript is a front-end language.  This can change with any number of frameworks to keep a project in one language.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  ----------------------------------------
dict.get('c', '"c" not found, please check key.')

dict.setdefault('c', '"c" not found, please check key.')



- What is a unit test?
unit testing is running a separate .py file which contains tests to run through the terminal.  Syntax is very important file naming convention is "test_{file name}" and all tested functions within the TestCase() class have to be formatted "test_{function name}".


- What is an integration test?
integration tests are unittests for flask application which test your app's routes via checking html content, status code, and others.


- What is the role of web application framework, like Flask?
flask simplifies the process and allows python syntax for behind the scenes javascript functionality.  This not only allows front and backend to use one language primarily but also shortens code via methods that run extensive javascript for us.


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
If you need to have multiple pieces of information that you need to store a query string is going to be more manageable than a longer route name.


- How do you collect data from a URL placeholder parameter using Flask?
I'm not sure if I understand what we mean by URL placeholder exactly.  **TIMMY** please follow up with me on next call.
request.args.get(Placeholder) <-- this may be it?


- How do you collect data from the query string using Flask?
flask.request.args[DATA]


- How do you collect data from the body of the request using Flask?
flask.request.form[DATA]


- What is a cookie and what kinds of things are they commonly used for?
cookies are browser based storage for things like username, passwords, emails, post ID's, post images, and infintely other options.  Storage size limits use to smaller pieces of data.


- What is the session object in Flask?
session object in flask allows us to access cookies in shortened, encrypted, syntax.


- What does Flask's `jsonify()` do?
jsonify creates a properly formatted json object
