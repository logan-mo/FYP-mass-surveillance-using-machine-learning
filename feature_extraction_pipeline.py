def get_car_detector():
    ...


def get_number_plate_recognizer():
    ...


def get_car_color_classifier():
    ...


def get_number_plate_parser():
    ...

def connect_to_sql():
    ...

car_detector = get_car_detector()
number_plate_recognizer = get_number_plate_recognizer()
car_color_classifier = get_car_color_classifier()
number_plate_parser = get_number_plate_parser()

database_connection = connect_to_sql()

def process(image, time_stamp, camera_id):
    detections = car_detector(image)
    for car in detections:
        car_type = car.label
        number_plate = number_plate_recognizer(car)[0]
        license_number = number_plate_parser(number_plate)
        car_color = car_color_classifier(car)
        
        car_id = database_connection.query(f"SELECT car_id FROM db.data WHERE license_plate_number = \"{license_number}\"")
        if car_id is not None:
            database_connection['db.data'].insert(car_id, car_type, car_color license_number,time_stamp)
            database_connection['db.data'].insert(camera_id, time_stamp, car.id), 
        
        else:
            database_connection['db.data'].insert(car_type, car_color license_number,time_stamp)
            database_connection['db.data'].insert(camera_id, time_stamp, car.id), 
            
def process(video, camera_id):
    for frame, time_stamp in video:
        process(frame, time_stamp, camera_id)     
# Database Scheme

"""
db.data(
    car_id, #incremental, optional
    car_type,
    car_color,
    license_plate_number
)

db.detections(
    detection_id, # incremental
    camera_id,
    datatime,
    car_id
)

"""
