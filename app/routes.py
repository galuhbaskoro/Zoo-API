from flask import jsonify, Blueprint, request

bp = Blueprint('main', __name__)

animals = [
    {
        "id":1, "name":"Lion","habitat":"savana","weight":190, "height":120,"diet":"carnivor" 
    },
    {
        "id":2, "name":"Piranha","habitat":"lake, river","weight":0.50, "height":0.20,"diet":"carnivor" 
    },
]

# base data employees
employees = [
    {
        "id":1, "name": "adam", "role": "supervisor"
    },
    {
        "id":2, "name": "kevin", "role": "zoo keeper" 
    }
]

# route to get data animals
@bp.route('/api/animals', methods=['GET'])
def get_animals():
    return jsonify(animals), 200

# route to get data employees
@bp.route('/api/employees', methods=['GET'])
def get_employees():
    return jsonify(employees), 200

# route to get animals by id
@bp.route('/api/animals/view/<int:animal_id>', methods=["GET"])
def get_animal(animal_id):
    animal = next((animal for animal in animals if animal['id'] == animal_id),None)
    if animal is None:
        return jsonify({'message': 'animal not found'}), 404
    return jsonify(animal), 200

# route to get employees by id
@bp.route('/api/employees/view/<int:employee_id>', methods=["GET"])
def get_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id),None)
    if employee is None:
        return jsonify({'message': 'employee not found'}), 404
    return jsonify(employee), 200

# route to create new animal
@bp.route('/api/animals/create', methods=['POST'])
def create_animal():
    data = request.get_json()
    new_animal = {
        "id": len(animals) + 1,
        "name": data['name'],
        "habitat": data['habitat'],
        "weight": data['weight'],
        "height": data['height'],
        "diet": data['diet'],
    }
    animals.append(new_animal)
    return jsonify(new_animal), 201

# route to create new employee
@bp.route('/api/employees/create', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "role": data["role"],
    }
    employees.append(new_employee)
    return jsonify(new_employee), 201

# route to  update animal
@bp.route('/api/animals/update/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal is None:
        return jsonify({"message": "animal not found"}), 404
    data = request.get_json()
    animal["name"] = data.get("name", animal["name"])
    animal["habitat"] = data.get("habitat", animal["habitat"])
    animal["weight"] = data.get("weight", animal["weight"])
    animal["height"] = data.get("height", animal["weight"])
    animal["diet"] = data.get("diet", animal["weight"])
    return jsonify(animal), 200

# route to update employee
@bp.route('/api/employees/update/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee is None:
        return jsonify({"message": "employee not found"}), 404
    data = request.get_json()
    employee["name"] = data.get("name", employee["name"])
    employee["role"] = data.get("role", employee["role"])
    return jsonify(employee), 200

# route to delete animal
@bp.route('/api/animals/delete/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal is None:
        return jsonify({"message": "animal not found"}), 404
    
    animals.remove(animal)
    return jsonify({"message": "animal deleted"}), 200

# route to delete employee
@bp.route('/api/employees/delete/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee is None:
        return jsonify({"message": "employee not found"}), 404
    
    employees.remove(employee)
    return jsonify({"message": "employee deleted"}), 200
