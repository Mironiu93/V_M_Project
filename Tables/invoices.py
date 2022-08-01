class Invoices(BotUsers, Statuses):
    id: int
    bot_user_id: str
    date_create: int
    total: int
    status_id: int