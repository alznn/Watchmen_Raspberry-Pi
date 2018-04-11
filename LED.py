import RPi.GPIO as GPIO
import time

LED_R = 11
LED_G = 13
LED_B = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
sql = "SELECT * FROM driver_status WHERE driver_id = 'ZXC123' ORDER BY UNIX_TIMESTAMP(update_time) DESC;"
  # 執行SQL statement
cur = conn.cursor()
conn = pymysql.connect(
    host = "host",
    user = "user",
    passwd = "passwd",
    db = "db"
)
while True:
    results = cur.execute(sql)
    results = cur.fetchone()
    status = results[1]
    date = results[3]

    if status == 1:
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(5)
        GPIO.cleanup(LED_B)
        GPIO.cleanup(LED_G)
        GPIO.cleanup(LED_R)
    elif status == 2:
        GPIO.output(LED_B, GPIO.LOW)
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        time.sleep(5)
        GPIO.cleanup(LED_B)
        GPIO.cleanup(LED_G)
        GPIO.cleanup(LED_R)
    elif status == 3:
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(5)
        GPIO.cleanup(LED_B)
        GPIO.cleanup(LED_G)
        GPIO.cleanup(LED_R)
    else:
        break;

GPIO.cleanup()