from django.urls import reverse
from apps.conftest import *

class TestStaticPage:
  about_url = reverse('about')
  privacy_url = reverse('privacy')
  policy_url = reverse('policy')

  def test_about_page(self, client):
    get_res = client.get(self.about_url)

    for template in get_res.templates:
      assert 'pages/about.html' in template.name
    assert get_res.status_code in [200, 302]

  def test_privacy_page(self, client):
    get_res = client.get(self.privacy_url)
    
    for template in get_res.templates:
      assert 'pages/privacy.html' in template.name
    assert get_res.status_code in [200, 302]

  def test_policy_page(self, client):
    get_res = client.get(self.policy_url)
    
    for template in get_res.templates:
      assert 'pages/policy.html' in template.name
    assert get_res.status_code in [200, 302]