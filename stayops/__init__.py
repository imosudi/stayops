
# stayops/__init__.py
from flask import Flask
from flask_graphql import GraphQLView

from stayops.extensions import db, migrate
from stayops.config.settings import DATABASE_URI
from stayops.graphql.schema import schema


# -------------------------------------------------------------------
# App Initialization (Singleton)
# -------------------------------------------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

# -------------------------------------------------------------------
# GraphQL Endpoint
# -------------------------------------------------------------------

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

# -------------------------------------------------------------------
# Entrypoint
# -------------------------------------------------------------------


