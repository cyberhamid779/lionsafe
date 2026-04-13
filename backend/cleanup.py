from app.services.database import SessionLocal
from app.models.user import User
from app.models.click import Click

db = SessionLocal()
users = db.query(User).filter(User.is_admin == False).all()
ids = [u.id for u in users]
db.query(Click).filter(Click.user_id.in_(ids)).delete(synchronize_session=False)
for u in users:
    db.delete(u)
db.commit()
print('Təmizləndi')
