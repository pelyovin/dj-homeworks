from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


class Car(models.Model):

    BODY_TYPE_CHOICES = (
        ('sedan', 'Седан'),
        ('hatchback', 'Хэтчбек'),
        ('SUV', 'Внедорожник'),
        ('wagon', 'Универсал'),
        ('minivan', 'Минивэн'),
        ('pickup', 'Пикап'),
        ('coupe', 'Купе'),
        ('cabrio', 'Кабриолет')
    )

    DRIVE_UNIT_CHOICES = (
        ('rear', 'Задний'),
        ('front', 'Передний'),
        ('full', 'Полный')
    )

    GEARBOX_CHOICES = (
        ('manual', 'Механика'),
        ('automatic', 'Автомат'),
        ('вариатор', 'CVT'),
        ('robot', 'Робот')
    )

    FUEL_TYPE_CHOICES = (
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'),
        ('electro', 'Электро')
    )

    model = models.CharField(max_length=70, null=False)
    year = models.IntegerField(null=False)
    color = models.CharField(max_length=70, null=False)
    mileage = models.IntegerField(null=False)
    volume = models.FloatField(null=False)
    body_type = models.CharField(choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField(choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(choices=FUEL_TYPE_CHOICES)
    price = models.FloatField(null=False)
    image = models.ImageField(upload_to='cars_img', null=False)

    def __str__(self):
        return f'{self.model}, год выпуска: {self.year}, пробег: {self.mileage}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales', null=False)
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='sales_car', null=False)
    created_at = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return f'{self.client} купил(а) {self.car}, дата покупки: {self.created_at}'
