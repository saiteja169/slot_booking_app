from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    slots = db.query(models.Slot).all()
    bookings = (
        db.query(models.Booking, models.Slot)
        .join(models.Slot, models.Booking.slot_id == models.Slot.id)
        .all()
    )
    return templates.TemplateResponse("index.html", {
        "request": request,
        "slots": slots,
        "bookings": bookings
    })

@app.post("/book")
def book_slot(
    slot_id: int = Form(...),
    user_name: str = Form(...),
    user_email: str = Form(...),
    db: Session = Depends(get_db)
):
    slot = db.query(models.Slot).filter(models.Slot.id == slot_id).first()
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")
    if slot.is_booked:
        raise HTTPException(status_code=400, detail="Slot already booked")

    booking = models.Booking(slot_id=slot_id, user_name=user_name, user_email=user_email)
    slot.is_booked = True
    db.add(booking)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/cancel/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    slot = db.query(models.Slot).filter(models.Slot.id == booking.slot_id).first()
    if slot:
        slot.is_booked = False

    db.delete(booking)
    db.commit()
    return RedirectResponse(url="/", status_code=303)