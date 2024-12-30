import random  

class Car:  
    def __init__(self, car_id, color, capacity, consumption, max_speed, speed_acceleration, break_acceleration, speed_ratio, initial_fuel):  
        self.car_id = car_id  # شماره ماشین  
        self.color = color  # رنگ ماشین  
        self.capacity = capacity  # ظرفیت باک (لیتر)  
        self.consumption = consumption  # مصرف بنزین (لیتر در 100 کیلومتر)  
        self.max_speed = max_speed  # حداکثر سرعت (کیلومتر در ساعت)  
        self.speed_acceleration = speed_acceleration  # شتاب افزاینده  
        self.break_acceleration = break_acceleration  # شتاب کاهنده  
        self.speed_ratio = speed_ratio  # نسبت سرعت به بنزین  
        self.current_fuel = initial_fuel  # سوخت اولیه  
        self.distance_covered = 0  # مسافت طی شده  
        self.stopped_for_refuel = False  # وضعیت سوخت‌گیری  

    def drive(self, time_elapsed):  
        """حرکت خودرو براساس زمان و سوخت باقی‌مانده"""  
        if self.stopped_for_refuel:  
            return  

        # محاسبه سرعت بر اساس نسبت سرعت و بنزین موجود  
        speed = min(self.max_speed, self.speed_ratio * self.current_fuel)  

        # محاسبه مسافت طی شده  
        distance_possible = speed * (time_elapsed / 3600)  # مسافت به کیلومتر  

        # محاسبه سوخت لازم  
        fuel_needed = (self.consumption / 100) * distance_possible  

        if fuel_needed <= self.current_fuel:  
            self.distance_covered += distance_possible  
            self.current_fuel -= fuel_needed  
        else:  
            # اگر سوخت کافی نباشد  
            distance_possible = (self.current_fuel * 100) / self.consumption  
            self.distance_covered += distance_possible  
            self.current_fuel = 0  # تمام سوخت استفاده می‌شود  

    def refuel(self):  
        """عملیات سوخت‌گیری"""  
        refuel_time = random.uniform(2, 5)  # زمان تصادفی سوخت‌گیری بین 2 تا 5 ثانیه  
        self.current_fuel = self.capacity  # پر کردن باک  
        self.stopped_for_refuel = False  # خاتمه عملیات سوخت‌گیری  

def simulate_race(cars, track_length, race_duration):  
    time_elapsed = 0  # زمان شبیه‌سازی  
    interval = 0.01  # زمان بروزرسانی‌ها (کمتر از 1 ثانیه)  

    print(f"Length of the race: {track_length} km")  
    print("The race will start now!\n")  

    # نمایش اطلاعات ماشین‌ها  
    for car in cars:  
        print(f"car_{car.car_id}: ID={car.car_id}, Color={car.color}, Initial Fuel={car.current_fuel:.2f}L, Max Speed={car.max_speed} km/h, Capacity={car.capacity}L, Consumption={car.consumption}L/100km, Speed Acceleration={car.speed_acceleration:.2f} m/s², Break Acceleration={car.break_acceleration:.2f} m/s², Speed Ratio={car.speed_ratio:.2f}")  

    print("\n")  

    # شبیه‌سازی مسابقه تا حداکثر ۲ ثانیه  
    while time_elapsed < race_duration:  
        time_elapsed += interval  
        
        for car in cars:  
            # 30% شانس سوخت‌گیری  
            if car.current_fuel < car.capacity and not car.stopped_for_refuel:  
                if random.random() < 0.3:  # احتمالی برای سوخت‌گیری  
                    car.stopped_for_refuel = True  
                    car.refuel()  # انجام عملیات سوخت‌گیری  

            car.drive(interval)  # به‌روزرسانی وضعیت خودرو  
        
        # پس از ۲ ثانیه، مسابقه را تمام کرده و برنده را مشخص کن  
        if time_elapsed >= race_duration:  
            break  

    # شناسایی برنده  
    winner = max(cars, key=lambda c: c.distance_covered)  # برنده بر اساس بیشترین مسافت طی شده  

    return winner  

# ایجاد ۱۰ خودرو با پارامترهای تصادفی  
cars = []  
for car_id in range(1, 11):  
    color = random.choice(["Red", "Blue", "Green", "Black", "White", "Yellow"])  
    capacity = random.choice([40, 50, 60, 70])  # ظرفیت باک (لیتر)  
    consumption = random.choice([5.0, 6.0, 7.0, 8.0])  # مصرف سوخت   
    max_speed = random.choice([150, 160, 170, 180])  # حداکثر سرعت  
    speed_acceleration = random.uniform(5.0, 10.0)  # شتاب افزاینده  
    break_acceleration = random.uniform(5.0, 10.0)  # شتاب کاهنده  
    speed_ratio = random.uniform(1.0, 2.0)  # نسبت سرعت به بنزین  
    initial_fuel = capacity  # سوخت اولیه  

    # ساخت ماشین  
    cars.append(Car(car_id, color, capacity, consumption, max_speed, speed_acceleration, break_acceleration, speed_ratio, initial_fuel))  

track_length = 100  # طول مسیر (کیلومتر)  
race_duration = 2  # مدت زمان مسابقه (ثانیه)  

# شبیه‌سازی مسابقه و دریافت برنده  
winner = simulate_race(cars, track_length, race_duration)  

# نتیجه نهایی  
if winner:  
    print(f"\nCongratulations! The winner is Car ID: car_{winner.car_id} (Color: {winner.color}) with Distance Covered: {winner.distance_covered:.2f} km and Remaining Fuel: {winner.current_fuel:.2f} L!")  
else:  
    print("No winner could be determined.")