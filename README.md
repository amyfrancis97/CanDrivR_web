# Sample Flask app

This is a very simple flask app for demonstration purposes.

To run this you will need pipenv installed (ideally). You can then run

```pipenv install```

in this directory to install dependencies. After that, you can run:

```pipenv run python app.py```

Once the server is running you will be able to access it at [http://127.0.0.1:8080](http://127.0.0.1:8080). Because it is in debug=True mode, any changes will be implemented immediately (refresh browser to see the change happen live).

I have configured this to use the popular Bootstrap ([https://getbootstrap.com/docs/5.2/getting-started/introduction/](https://getbootstrap.com/docs/5.2/getting-started/introduction/)) framework for styles (see [documentation](https://getbootstrap.com/docs/5.2/getting-started/introduction/)) so it is easy to add buttons, menus, grids/columns, images, forms, module-boxes, etc (a couple of examples are in the templates).

The app.py (and any modules it calls) contains most of the webapps logic. The templates provide the front-end formatting, but can also include basic logic for looping (e.g. to show multiple results as table rows) and conditional statements (e.g. to filter what you return). An endpoint is specified using code like ```@app.route("/")``` in app.py, with the following function defining what that endpoint does. When the page is loaded, that endpoint is called. The endpoint will typically return a template, passing any data you want to that template.