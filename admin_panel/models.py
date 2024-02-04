from django.db import models

# Create your models here.




class Add_Product(models.Model):
    SIZE_CHOICES = [
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
        ('11', '11'), ('12', '12'), ('13', '13'),
        ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'),
        ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'),
    ]

    MATERIAL_CHOICES = [
        ('cotton', 'Cotton'), ('blend_cotton', 'Blend Cotton'),
        ('mesh', 'Mesh'), ('woolen', 'Woolen'),
        ('rayon', 'Rayon'), ('nylon', 'Nylon'),
        ('sport', 'Sport'), ('gymfit', 'Gymfit'),
    ]

    SUITABLE_FOR_CHOICES = [
        ('Men', 'Men'), ('Women', 'Women'),
    ]

    PATTERN_CHOICES = [
        ('pattern1', 'Pattern 1'), ('pattern2', 'Pattern 2'),
        ('pattern3', 'Pattern 3'),
    ]

    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    colour = models.CharField(max_length=20)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    suitable_for = models.CharField(max_length=10, choices=SUITABLE_FOR_CHOICES)
    pattern = models.CharField(max_length=20, choices=PATTERN_CHOICES)

    def __str__(self):
        return self.product_name
    


