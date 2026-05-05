import re
from playwright.sync_api import Page, expect
from app import app

test_app = app.test_client()


def test_home_page_is_reachable():
    response = test_app.get('/')
    assert response.status_code is 200
    assert "Duty 1" in response.text 

# def test_home_page_is_reachable(page:Page):
#     page.goto("localhost:5000/")
#     expect(page).to_have_title(re.compile("Index"))
#     expect(page.locator("header")).to_be_visible()
#     expect(page.get_by_text("Duty 1")).to_be_visible()

  