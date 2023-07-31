from django.test import TestCase
from django.urls import reverse

from catdog.models import AnimalImage


class TestCatDogView(TestCase):


    def test_get(self):
        responce = self.client.get(reverse('catdog'))
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, template_name='catdog.html')


    def test_post_cat(self):
        responce = self.client.post(reverse('catdog'),  {'cat': 'true'})
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, template_name='pet.html')
        self.assertEqual(self.client.session['data_for_session']['species'],'cat')
        self.assertEqual(len(self.client.session['data_for_session']['species'].keys(),3))

    def test_post_error(self):
        with self.assertRaisesMessage(AttributeError, "are you try to hack")
            self.client.post(reverse('catdog'), {'boris': "true"})

    def test_save_catdog(self):
        #self.client.post(reverse('catdog'),  {'cat': 'true'})
        data_for_session = {'url': 'test@url',
                                'species': 'cat',
                                'type': 'jpg'}
        session = self.client.session
        session['data_for_session'] = data_for_session
        session.save()
        responce = self.client.post(reverse('save_catdog'),  {'cat': 'true'})
        self.assertEqual(AnimalImage.objects.count(), 1)
        self.assertTemplateUsed(responce, template_name='petsaved.html')

class TestCatDogView(TestCase):
    fixtures = ['data_for_test.json']

    def setUp(self):
        self.client = Client()
        self.assertEqual(AnimalImage.objects.count(), 25)