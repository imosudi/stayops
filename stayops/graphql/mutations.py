# stayops/graphql/mutations.py
"""type StayOpsMutation {
  confirmCheckout(input: ConfirmCheckoutInput!): BookingPayload
  createTask(input: TaskInput!): TaskPayload
  assignTask(taskId: ID!): TaskPayload

  reportIncident(input: IncidentInput!): IncidentPayload
  updateInventory(input: InventoryUpdateInput!): InventoryPayload
}"""

import graphene

class Mutation(graphene.ObjectType):
    """
    Root mutation object.
    Mutations are added incrementally.
    """
    _placeholder = graphene.Boolean()
