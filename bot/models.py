from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, BigInteger


metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("phone_number",BigInteger,nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("bot_status",Boolean, default=False),
    Column("tg_name", String, nullable=True, default=None),
    Column("verify_tg", Boolean, default=False)
    )


