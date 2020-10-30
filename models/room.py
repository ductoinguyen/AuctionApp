from datetime import datetime

def getTime():
    now = datetime.now()
    return (now.strftime("%d/%m/%Y"), int(now.strftime("%H")))
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")