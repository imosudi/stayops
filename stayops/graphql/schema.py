# stayops/graphql/schema.py

import graphene

class StayOpsQuery(graphene.ObjectType):
    health = graphene.String(required=True)

    def resolve_health(root, info):
        return "OK"

schema = graphene.Schema(
    query=StayOpsQuery
)

'''# stayops/graphql/schema.py

import graphene

class StayOpsQuery(graphene.ObjectType):
    health = graphene.String()

    def resolve_health(root, info):
        return "OK"

class StayOpsMutation(graphene.ObjectType):
    pass

schema = graphene.Schema(
    query=StayOpsQuery,
    mutation=StayOpsMutation
)
'''