import os
from datetime import datetime, timezone
from typing import Generator

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Query
from kafka import KafkaProducer
from sqlmodel import SQLModel, Session, select

from example import models

POSTS_TOPIC = "posts"
KAFKA_HOSTNAME = os.environ.get("KAFKA_HOSTNAME", "kafka")
KAFKA_PORT = os.environ.get("KAFKA_PORT", "9092")

app = FastAPI()
kafka_producer = KafkaProducer(
    bootstrap_servers=f"{KAFKA_HOSTNAME}:{KAFKA_PORT}")


def get_session() -> Generator[Session, None, None]:
    with Session(models.engine) as session:
        yield session


@app.on_event("startup")
def on_startup() -> None:
    SQLModel.metadata.create_all(bind=models.engine)


@app.post("/users/")
def create_user(
    user: models.UserBase,
    session: Session = Depends(get_session)) -> models.User:
    db_user = models.User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get("/users/")
def read_users(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session),
) -> list[models.User]:
    users = session.exec(select(models.User).offset(offset).limit(limit)).all()
    return users


@app.get("/users/{user_id}")
def read_user(
        user_id: int,
        session: Session = Depends(get_session),
) -> models.User:
    user_db = session.get(models.User, user_id)
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_db


@app.post("/users/{user_id}/posts/")
def create_post_for_user(
    user_id: int,
    post: models.PostBase,
    session: Session = Depends(get_session)) -> models.Post:
    user_db = session.get(models.User, user_id)
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    post_db = models.Post.from_orm(post,
                                   update={
                                       "timestamp":
                                       datetime.now(tz=timezone.utc),
                                       "poster_id": user_id
                                   })
    session.add(post_db)
    session.commit()
    session.refresh(post_db)
    kafka_producer.send(topic=POSTS_TOPIC,
                        value=bytes(post_db.json(), "utf-8"))
    return post_db


@app.get("/posts/")
def read_posts(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session),
) -> list[models.Post]:
    posts = session.exec(select(models.Post).offset(offset).limit(limit)).all()
    return posts


@app.get("/posts/{user_id}")
def read_posts_for_user(
        user_id: int,
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        session: Session = Depends(get_session),
) -> list[models.Post]:
    user_db = session.get(models.User, user_id)
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    posts = session.exec(
        select(models.Post).filter(models.Post.poster_id == user_id).offset(
            offset).limit(limit)).all()
    return posts


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
