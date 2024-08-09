from persistence.ipersistence_manager import IPersistenceManager
from collections import defaultdict
from flask import Blueprint, request, jsonify
import json
import os
from models.db import db

class DataManager(IPersistenceManager):
    def __init__(self, storage_file="data.json"):
        self.storage_file = storage_file
        if not os.path.exists(storage_file):
            with open(storage_file, "w") as f:
                f.write("{}")

    def save(self, entity):
        db.session.add(entity)
        db.session.commit()
        return "saved"


    def get(self, entity_id, entity_type):
        return jsonify(db.session.query(entity_type).filter_by(id=entity_id).first().to_dict())
    
    def get_all(self, entity_type):
        entities = db.session.query(entity_type).all()
        return jsonify([entity.to_dict() for entity in entities]), 200




 
    def update(self, entity):
        db.session.merge(entity)
        db.session.commit()
        return "changed"


    def delete(self, entity_id, entity_type):
        entity = db.session.query(entity_type).filter_by(id=entity_id).first()
        db.session.delete(entity)
        db.session.commit()
        return "deleted"