from django.db import models

class Contact(models.Model):
    """
    Represents a contact or customer inquiry with product and payment details.

    Fields:
        name (CharField): The first name of the contact.
        lastname (CharField): The last name of the contact.
        email (EmailField): The contact's email address.
        address (TextField): The full address of the contact.
        product (CharField): The name or description of the product of interest.
        payment_slip (FileField): An optional uploaded file for the payment receipt,
                                  stored in the 'payments/' directory.
    """
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    product = models.CharField(max_length=200)
    payment_slip = models.FileField(upload_to='payments/', blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the contact, showing full name and product.
        """
        return f"{self.name} {self.lastname} – {self.product}"

