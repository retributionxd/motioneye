                                                                                
import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO   # Import the GPIO library.                            
import time #                    Import time library^M                          
GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.^M
                          # Can use GPIO.setmode(GPIO.BCM) instead to use ^M    
                          # Broadcom SOC channel names.^M                       
GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 18/board PIN 12 to output mode                      
pwm = GPIO.PWM(12, 1000)   # Initialize PWM on pwmPin 100Hz frequency           
# main loop of program                                                          
#print("\nPress Ctl C to quit \n")      # Print blank line (\n == newline) before
dc=0                                   # set dc variable to 0 (will start PWM at
pwm.start(dc)                          # Start PWM with 0% duty cycle^M  
pwm.ChangeDutyCycle(0);
#pwm.stop()                                                                      
 #GPIO.cleanup() 
'''
while True:                            # Create an infinite loop until Ctl C is 
  for dc in range(0, 100, 20):          # Loop with dc set from 0 to 100 steppin
    pwm.ChangeDutyCycle(dc)                                                     
    time.sleep(2)                   # wait for .05 seconds at current LED bright
    print(dc)                                                                   
  for dc in range(100, 0, -20):          # Loop with dc set from 95 to 5 steppin
    pwm.ChangeDutyCycle(dc)                                                     
    time.sleep(0.05)                   # wait for .05 seconds at current LED bri
    print(dc)                                                                   
pwm.stop()                                                                      
GPIO.cleanup() 
'''

class setpwm(tornado.web.RequestHandler):
    def get(self):
                                                                          
        pwmValue = int(self.get_argument("pwm"))
        pwm.ChangeDutyCycle(pwmValue)                  
        self.write('Setting Pwm value to %s' % `pwmValue`)
        #time.sleep(5);
        #pwm.ChangeDutyCycle(0);   



def make_app():
    return tornado.web.Application([
    (r"/setpwm", setpwm)
])

if __name__ == "__main__":
    app = make_app()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()

