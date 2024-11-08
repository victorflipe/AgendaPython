from typing import Union, Annotated
from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select



class ContactBase(SQLModel):
    name: str = Field(index = True)
    nickname: str = Field(index = True)
    number: str = Field(index = True)


class Contact(ContactBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str


class ContactPublic(ContactBase):
    id: int


class ContactCreate(ContactBase):
    secret_name: str


class ContactUpdate(ContactBase):
    name: str | None = None
    nickname: str | None = None
    number: str | None = None
    secret_name: str | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread" : False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/contact", response_model=ContactPublic)
def create_contact(contact: ContactCreate, session: SessionDep):
    db_contact = Contact.model_validate(contact)
    session.add(db_contact)
    session.commit()
    session.refresh(db_contact)
    return db_contact


@app.get("/contacts", response_model=list[ContactPublic])
def get_contacts(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    contacts = session.exec(select(Contact).offset(offset).limit(limit)).all()
    return contacts


@app.get("/contact/{contact_id}", response_model=ContactPublic)
def get_contact(contact_id: int, session: SessionDep):
    contact = session.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@app.patch("/contact/{contact_id}", response_model=ContactPublic)
def update_contact(contact_id: int, contact:ContactUpdate, session:SessionDep):
    contact_db = session.get(Contact, contact_id)
    if not contact_db:
        raise HTTPException(status_code=404, detail="Contact not found!")
    contact_data = contact.model_dump(exclude_unset=True)
    contact_db.sqlmodel_update(contact_data)
    session.add(contact_db)
    session.commit()
    session.refresh(contact_db)
    return contact_db


@app.delete("/contact/{contact_id}")
def delete_contact(contact_id: int, session:SessionDep):
    contact = session.get(Contact, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    session.delete(contact)
    session.commit()
    return {
        "ok": True,
        "result": "Contact delete with success!"
    }

