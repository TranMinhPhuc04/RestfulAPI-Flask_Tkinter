import requests


class APIClient:
    BASE_URL = "http://127.0.0.1:5000/api"

    # --- Student API Methods ---
    @staticmethod
    def get_students():
        response = requests.get(f"{APIClient.BASE_URL}/students")
        return response.json()

    @staticmethod
    def add_student(data):
        response = requests.post(f"{APIClient.BASE_URL}/students", json=data)
        return response.json()

    @staticmethod
    def get_student(student_id):
        response = requests.get(f"{APIClient.BASE_URL}/students/{student_id}")
        return response.json()

    @staticmethod
    def update_student(student_id, data):
        response = requests.put(
            f"{APIClient.BASE_URL}/students/{student_id}", json=data)
        return response.json()

    @staticmethod
    def delete_student(student_id):
        response = requests.delete(
            f"{APIClient.BASE_URL}/students/{student_id}")
        return response.json()

    # --- Class API Methods ---
    @staticmethod
    def get_classes():
        response = requests.get(f"{APIClient.BASE_URL}/classes")
        return response.json()

    @staticmethod
    def add_class(data):
        response = requests.post(f"{APIClient.BASE_URL}/classes", json=data)
        return response.json()

    @staticmethod
    def get_class(class_id):
        response = requests.get(f"{APIClient.BASE_URL}/classes/{class_id}")
        return response.json()

    @staticmethod
    def update_class(class_id, data):
        response = requests.put(
            f"{APIClient.BASE_URL}/classes/{class_id}", json=data)
        return response.json()

    @staticmethod
    def delete_class(class_id):
        response = requests.delete(f"{APIClient.BASE_URL}/classes/{class_id}")
        return response.json()

    # --- Subject API Methods ---
    @staticmethod
    def get_subjects():
        response = requests.get(f"{APIClient.BASE_URL}/subjects")
        return response.json()

    @staticmethod
    def add_subject(data):
        response = requests.post(f"{APIClient.BASE_URL}/subjects", json=data)
        return response.json()

    @staticmethod
    def get_subject(subject_id):
        response = requests.get(f"{APIClient.BASE_URL}/subjects/{subject_id}")
        return response.json()

    @staticmethod
    def update_subject(subject_id, data):
        response = requests.put(
            f"{APIClient.BASE_URL}/subjects/{subject_id}", json=data)
        return response.json()

    @staticmethod
    def delete_subject(subject_id):
        response = requests.delete(
            f"{APIClient.BASE_URL}/subjects/{subject_id}")
        return response.json()

    # --- Enrollment API Methods ---
    @staticmethod
    def add_enrollment(data):
        response = requests.post(
            f"{APIClient.BASE_URL}/enrollments/", json=data)
        return response.json()

    @staticmethod
    def get_enrollments(student_id=None):
        if student_id:
            response = requests.get(
                f"{APIClient.BASE_URL}/enrollments/{student_id}")
        else:
            response = requests.get(f"{APIClient.BASE_URL}/enrollments")

        # Kiểm tra phản hồi để đảm bảo nó hợp lệ và có thể parse thành JSON
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return {"error": "Invalid response format"}
        else:
            return {"error": f"Failed to fetch enrollments. Status code: {response.status_code}"}

    @staticmethod
    def update_enrollment(enrollment_id, data):
        response = requests.put(
            f"{APIClient.BASE_URL}/enrollments/{enrollment_id}", json=data)
        return response.json()

    @staticmethod
    def delete_enrollment(enrollment_id):
        response = requests.delete(
            f"{APIClient.BASE_URL}/enrollments/{enrollment_id}")
        return response.json()
