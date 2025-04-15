from datetime import datetime, timedelta, timezone

ACCES_TOKEN_EXPIRE_MINUTES = 5

acces_token_expires = datetime.now(timezone.utc) + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)

print(acces_token_expires)
