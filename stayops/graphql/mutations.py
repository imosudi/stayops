type StayOpsMutation {
  confirmCheckout(input: ConfirmCheckoutInput!): BookingPayload
  createTask(input: TaskInput!): TaskPayload
  assignTask(taskId: ID!): TaskPayload

  reportIncident(input: IncidentInput!): IncidentPayload
  updateInventory(input: InventoryUpdateInput!): InventoryPayload
}
