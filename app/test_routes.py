import pytest # type: ignore
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True  
    client = app.test_client()   
    yield client  

# tesing get * animals
def test_get_animals(client):
    response = client.get('/api/animals')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# testing get animal by id
def test_get_animal(client):
    response = client.get('/api/animals/view/1')
    assert response.status_code == 200
    assert response.json['name'] == "Lion"

# testing get animal if not found
def test_get_animal_not_found(client):
    response = client.get('/api/animals/view/999')
    assert response.status_code == 404
    assert response.json['message'] == "animal not found"

# testing create animal
def test_create_animal(client):
    new_animal = {
        "name": "Cow",
        "habitat": 'grass, savana',
        "weight": "500",
        "height": "90",
        "diet": "herbivor",
    }
    response = client.post("/api/animals/create", json = new_animal)
    assert response.status_code == 201
    assert response.json['name'] == "Cow"

# testing update animal
def test_update_animal(client):
    updated_data = {
        "name": "Bear",
        "habitat": 'forest',
        "weight": "200",
        "height": "150",
        "diet": "carnivor",
    }
    response = client.put('/api/animals/update/1', json = updated_data)
    assert response.status_code == 200
    assert response.json['name'] == "Bear"

# testing delete animal
def test_delete_animal(client):
    response = client.delete('api/animals/delete/3')
    assert response.status_code == 200

# tesing get * employee
def test_get_employee(client):
    response = client.get('/api/employees')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# testing get employee by id
def test_get_employee(client):
    response = client.get('/api/employees/view/1')
    assert response.status_code == 200
    assert response.json['name'] == "adam"

# testing get employee if not found
def test_get_employee_not_found(client):
    response = client.get('/api/employees/view/999')
    assert response.status_code == 404
    assert response.json['message'] == "employee not found"

# testing create employee
def test_create_employee(client):
    new_employee = {
        "name": "Sarah",
        "role": 'zoo kepper',
    }
    response = client.post("/api/employees/create", json = new_employee)
    assert response.status_code == 201
    assert response.json['name'] == "Sarah"

# testing update Employee
def test_update_employee(client):
    updated_data = {
        "name": "Doni",
        "role": 'supervisor',
    }
    response = client.put('/api/employees/update/2', json = updated_data)
    assert response.status_code == 200
    assert response.json['name'] == "Doni"

# testing delete employee
def test_delete_employee(client):
    response = client.delete('api/employees/delete/2')
    assert response.status_code == 200