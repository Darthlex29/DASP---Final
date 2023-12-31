from ..Models import Hosting
from app import db

class HostingDAO():

    @classmethod
    def createHosting(self, data):
        try:
            nuevoHosting = Hosting(**data)

            db.session.add(nuevoHosting)
            db.session.commit()
            return nuevoHosting
        except Exception as ex:
            print("error")
            return Exception(ex)
    
    @classmethod
    def getHostings(self):
        try:
            allHostings = Hosting.query.all()
            return allHostings
        except Exception as ex:
            print("error")
            raise Exception(ex)

    @classmethod
    def getHostingById(self, id):
        try:
            hosting = Hosting.query.filter_by(id=id).first()
            if hosting is not None:
                #hostingJson = hosting.to_JSON()
                return hosting
            else:
                return None
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
    
    @classmethod
    def updateHosting(self, id, data):
        try:
            hosting = Hosting.query.filter_by(id=id).first()
            if hosting is not None:
                hosting.from_JSON(data)
                db.session.commit()
                hosting_json = hosting.to_JSON()
                return hosting_json
            else:
                return False
        except Exception as ex:
            print("error 404")
            raise Exception(ex)
        
    @classmethod
    def deleteHosting(self, id):
        try:
            hosting = Hosting.query.filter_by(id=id).first()
            db.session.delete(hosting)
            db.session.commit()
            return hosting
        except Exception as ex:
            print("error")
            return Exception(ex)

    @classmethod
    def getHostingPlan(self, hosting):
        return hosting.plan