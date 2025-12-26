import graphene
from stayops.graphql.queries import Query
from stayops.graphql.mutations import Mutation

schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
