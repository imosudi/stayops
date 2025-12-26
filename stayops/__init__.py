
# stayops/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_graphql import GraphQLView

from stayops.graphql.schema import schema
from stayops.config.settings import DATABASE_URI

# -------------------------------------------------------------------
# App Initialization (Singleton)
# -------------------------------------------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# -------------------------------------------------------------------
# GraphQL Endpoint
# -------------------------------------------------------------------

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Set to False in production
    )
)

# -------------------------------------------------------------------
# Entrypoint
# -------------------------------------------------------------------


