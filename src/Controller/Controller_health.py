from src.Model.Model_helth import health_check

def health_controller():
    try:
        row = health_check()
        return {"status": "ok", "db": "connected", "row": row}, 200
    except:
        return {"status": "ok", "db": "waking up"}, 200