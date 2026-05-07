import re
from playwright.sync_api import Page, expect
from app import app

test_app = app.test_client()


def test_home_page_is_reachable():
    response = test_app.get('/')
    assert response.status_code is 200

def test_homepage_page_content_contains_automate():
    response = test_app.get('/')
    assert "Automate" in response.text

def test_automate_is_homepage_heading():
    response = test_app.get('/')
    assert "<h1>Automate</h1>" in response.text

def test_home_page_shows_duty_5():
    response = test_app.get("/")
    assert "Duty 5" in response.text

def test_home_page_shows_duty_5_description():
    response = test_app.get('/')
    assert "Build and operate a continuous Integration (CI) capability, employing version control of source code and related artifacts" in response.text

def test_home_page_formats_duty_5_correctly():
    response = test_app.get('/')
    assert "Duty 5 - Build and operate a continuous Integration (CI) capability, employing version control of source code and related artifacts" in response.text

def test_homepage_shows_all_automate_duties():
    response = test_app.get('/')
    assert "Duty 5" in response.text
    assert "Duty 7" in response.text
    assert "Duty 10" in response.text

def test_homepage_shows_correct_duty_descriptions():
    response = test_app.get('/')
    assert "Build and operate a continuous Integration (CI) capability, employing version control of source code and related artifacts" in response.text
    assert "Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)" in response.text
    assert "Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable" in response.text

def test_add_duty_route_exists():
    response = test_app.post("/add-duty", data={})
    assert response.status_code != 404 

def test_add_duty_returns_successful_response():
    response = test_app.post("/add-duty", data={
        "identifier": "11",
        "description": "New duty"
    })
    assert response.status_code == 200

def test_add_duty_returns_identifier_from_form():
    response = test_app.post("/add-duty", data={
        "identifier": "11",
        "description": "New duty"
    })
    assert "11" in response.text 

def test_add_duty_returns_description_from_form():
    response = test_app.post("/add-duty", data={
        "identifier": "11",
        "description": "New duty"
    })
    assert "New duty" in response.text

def test_added_duty_appears_on_homepage():
    test_app.post("/add-duty", data={
        "identifier": 12,
        "description": "Stored duty"
    })
    response = test_app.get("/")
    assert "Stored duty" in response.text

def test_homepage_formats_duty_correctly():
    test_app.post('/add-duty', data={
        "identifier": "12",
        "description": "Stored duty"
    })

    response = test_app.get('/')

    assert "Duty 12 - Stored duty" in response.text

def test_duplicate_duty_identifier_is_not_added():
    test_app.post("/add-duty", data={
        "identifier": "12",
        "description": "First duty"
    })
    test_app.post("/add-duty", data={
        "identifier": "12",
        "description": "Duplicate duty"
    })

    response = test_app.get("/")

    assert response.text.count("Duty 12") == 1

def test_homepage_has_add_duty_form():
    response = test_app.get('/')

    assert "<form" in response.text

# def test_home_page_is_reachable(page:Page):
#     page.goto("localhost:5000/")
#     expect(page).to_have_title(re.compile("Index"))
#     expect(page.locator("header")).to_be_visible()
#     expect(page.get_by_text("Duty 1")).to_be_visible()

  