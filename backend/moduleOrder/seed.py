import json
from sqlalchemy.orm import Session

def seedSurcharges(db: Session):
    data = json.load(open('./seedJson/surcharge.json'))
    for item in data: 
        surchargeRequest = SurchargeRequest(**item)
        try:
            _surcharge = createSurchargeModel(db=db, surchargeRequest=surchargeRequest)
        except Exception as exception:
            db.rollback()
            print("Some issues while adding "+surchargeRequest.title)
