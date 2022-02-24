from django.test import TestCase
from .models import Editor, Article, tags

# Create your tests here.
class EditorTestClass(TestCase):
    # set up method
    def setUp(self):
        self.Esther= Editor(first_name='Esther', last_name='Anyona', email='starjonso@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Esther,Editor))

    # Testing save method
    def test_save(self):
        self.Esther.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

    # Testing delete method
    def test_delete(self):
        self.Esther.delete_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)==0)

    # Test for displaying all model objects saved


    # Test for updating single object properties
