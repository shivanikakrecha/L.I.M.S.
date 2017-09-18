from . models import Enventory, Product, IssueProduct, Maintenance
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


Product_choice = (
    ('Monitor', 'Monitor'),
    ('Laptop', 'Laptop'),
    ('Switch', 'Switch'),
    ('cable', 'Cable'),
    ('Key-board', 'Key-board')
)
# product_type = models.CharField(max_length=100, choices=Product_choice)

Manufactures = (
    ('HP', 'HP'),
    ('Sisco', 'Sisco'),
    ('Dell', 'Dell')
)

Use_to = (
    ('Employee', 'Employee'),
    ('Customer', 'Customer'),
    ('Technician', 'Technician'),
    ('Company', 'Company')
)

class EnventoryForm(forms.ModelForm):
   # error_css_class = 'error'

    Product_Type = forms.ChoiceField(choices=Product_choice, required=True)
    Manufacture = forms.ChoiceField(choices=Manufactures, required=True)
    Assigned_to = forms.ChoiceField(choices=Use_to, required=True)

    class Meta:
        model = Enventory

        fields = (
            'Product_Type',
            'Manufacture',
            'Serial_no',
            'Mac_ID',
            'Assigned_to',
            'Technician',
            'Purchase_date',
            'Issue_date',
            'Warntee',
            'Maintainance',
            'Location',
            'Comments',
            'Status',
            'Duration',
   )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
             'username',
             'first_name',
             'last_name',
             'email',
             'password1',
             'password2'
         )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = (
            'Products',
            'Manufacture',
            'Serial_nu',
            'Mac_Id',
            'Technician',
            'Assigned_To',
            'Purchase_Date',
            'Warranty_Time',
            'Location'

        )



class IssueForm(forms.ModelForm):

    class Meta:
        model = IssueProduct

        fields = (
            'products',
            'known_issue',
            'status',
            'comments'
        )

class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        fields = (
            'maintain',
            'Action',
            'Post'
        )
