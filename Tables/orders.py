class Orders(Statuses, Invoices, BotUsers):
    id: int
    bot_user_id: str
    date_create: int
    status_id: int
    invoice_id: str