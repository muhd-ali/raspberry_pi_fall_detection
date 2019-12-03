from mpu6050 import mpu6050
import time


class TapTyper:
    mpu = mpu6050(0x68)
    acc_threshold = 50
    count_threshold = 10

    def run(self):
        count = 0
        while (True):
            if count > 5:
            	print("fall detected")
            	count = 0
            try:
                accel_data = self.mpu.get_accel_data()
                gyro_data = self.mpu.get_gyro_data()
                if (abs(gyro_data['x']) > self.acc_threshold or abs(gyro_data['y']) > self.acc_threshold or abs(gyro_data['z']) > self.acc_threshold):
                    # print(f"accl. detected {count}")
                    count+=1
                else:
                    count = 0
            except KeyboardInterrupt:
                break
            time.sleep(0.1)


if __name__ == "__main__":
    program = TapTyper()
    program.run()
