from database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

area_sp_table = Table('area_sp', Base.metadata,
    Column('area_id', Integer, ForeignKey('areas.id')),
    Column('sp_id', Integer, ForeignKey('sps.id'))
)

sp_object_table = Table('sp_object', Base.metadata,
    Column('sp_id', Integer, ForeignKey('sps.id')),
    Column('object_id', Integer, ForeignKey('objects.id'))
)

object_document_table = Table('object_document', Base.metadata,
    Column('object_id', Integer, ForeignKey('objects.id')),
    Column('doc_id', Integer, ForeignKey('documents.id'))
)


class Area(Base):
    __tablename__ = 'areas'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    base_url = Column(String(256), unique=False)
    city = Column(String(256), unique=False)
    sp = relationship("Sp", secondary = area_sp_table)

    def __init__(self, name = None, base_url = None, city = None):
        self.name = name
        self.base_url = base_url
        self.city = city

    def __repr__(self):
        return f'<Area: {self.name}>'

class Sp(Base):
    __tablename__ = 'sps'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=False)
    objects = relationship("SpObject", secondary = sp_object_table)

    def __init__(self, name = None):
        self.name = name

    def __repr__(self):
        return f'<Sp: {self.name}>'


class SpObject(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=False)
    square = Column(Integer)
    docs = relationship("Document", secondary = object_document_table)

    def __init__(self, name = None, square = None):
        self.name = name
        self.square = square

    def __repr__(self):
        return f'<Object: {self.name}>'

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=False)
    path = Column(String(256), unique=False)

    def __init__(self, name = None, path = None):
        self.name = name
        self.path = path

    def __repr__(self):
        return f'<Document: {self.name}>'
