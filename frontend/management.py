import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Menu
from tkinter.ttk import Notebook, Treeview
from api_client import APIClient


class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("1000x600")
        self.window.config(bg="white")

        # Menu bar
        self.create_menu()

        # Tab control
        self.tab_control = Notebook(self.window)
        self.tab_control.pack(expand=1, fill='both')

        # Tabs
        self.create_student_tab()
        self.create_class_tab()
        self.create_subject_tab()
        self.create_enrollment_tab()

    def create_menu(self):
        menu_bar = Menu(self.window)
        self.window.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.window.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
            "About", "Student Management System v1.0"))
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def create_student_tab(self):
        # Tạo tab Student
        student_tab = tk.Frame(self.tab_control, bg="white")
        self.tab_control.add(student_tab, text="Students")

        tk.Label(student_tab, text="Student Management", font=(
            "Helvetica", 16, "bold"), bg="white").pack(pady=10)

        # Frame chứa các trường nhập liệu
        form_frame = tk.Frame(student_tab, bg="white")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="First Name", bg="white").grid(
            row=0, column=0, padx=5, pady=5)
        self.f_name_entry = tk.Entry(form_frame)
        self.f_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Last Name", bg="white").grid(
            row=1, column=0, padx=5, pady=5)
        self.l_name_entry = tk.Entry(form_frame)
        self.l_name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Sử dụng Combobox cho trường class_name
        tk.Label(form_frame, text="Class", bg="white").grid(
            row=2, column=0, padx=5, pady=5)
        self.class_combobox = ttk.Combobox(form_frame, state="readonly")
        self.class_combobox.grid(row=2, column=1, padx=5, pady=5)

        # Load danh sách lớp học vào Combobox
        self.load_classes()

        tk.Label(form_frame, text="Year", bg="white").grid(
            row=3, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(form_frame)
        self.year_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Age", bg="white").grid(
            row=4, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(form_frame)
        self.age_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Gender", bg="white").grid(
            row=0, column=2, padx=5, pady=5)
        self.gender_entry = tk.Entry(form_frame)
        self.gender_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Birth Date (YYYY-MM-DD)",
                 bg="white").grid(row=1, column=2, padx=5, pady=5)
        self.birth_entry = tk.Entry(form_frame)
        self.birth_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Contact", bg="white").grid(
            row=2, column=2, padx=5, pady=5)
        self.contact_entry = tk.Entry(form_frame)
        self.contact_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Email", bg="white").grid(
            row=3, column=2, padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=3, column=3, padx=5, pady=5)

        # Frame chứa các nút thao tác
        button_frame = tk.Frame(student_tab, bg="white")
        button_frame.pack(pady=10)

        self.add_button = tk.Button(
            button_frame, text="Add Student", command=self.add_student, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        tk.Button(button_frame, text="Update Student", command=self.update_student,
                  bg="#FF9800", fg="white").grid(row=0, column=1, padx=10, pady=5)

        tk.Button(button_frame, text="Delete Student", command=self.delete_student,
                  bg="#F44336", fg="white").grid(row=0, column=2, padx=10, pady=5)

        tk.Button(button_frame, text="Reset", command=self.reset_form,
                  bg="#607D8B", fg="white").grid(row=0, column=3, padx=10, pady=5)

        # Treeview để hiển thị danh sách sinh viên
        self.student_tree = ttk.Treeview(
            student_tab,
            columns=("id", "f_name", "l_name", "class_name", "year",
                     "age", "gender", "birth", "contact", "email"),
            show="headings"
        )
        self.student_tree.heading("id", text="ID")
        self.student_tree.heading("f_name", text="First Name")
        self.student_tree.heading("l_name", text="Last Name")
        self.student_tree.heading("class_name", text="Class")
        self.student_tree.heading("year", text="Year")
        self.student_tree.heading("age", text="Age")
        self.student_tree.heading("gender", text="Gender")
        self.student_tree.heading("birth", text="Birth Date")
        self.student_tree.heading("contact", text="Contact")
        self.student_tree.heading("email", text="Email")
        self.student_tree.pack(fill="both", expand=True)

        # Gắn sự kiện chọn sinh viên
        self.student_tree.bind("<<TreeviewSelect>>", self.on_student_select)

        # Làm mới Treeview với danh sách sinh viên hiện có
        self.refresh_student_treeview()

    def create_class_tab(self):
        # Tạo tab Class
        class_tab = tk.Frame(self.tab_control, bg="white")
        self.tab_control.add(class_tab, text="Classes")

        tk.Label(class_tab, text="Class Management", font=(
            "Helvetica", 16, "bold"), bg="white").pack(pady=10)

        # Form inputs for adding/updating class
        form_frame = tk.Frame(class_tab, bg="white")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Class Name", bg="white").grid(
            row=0, column=0, padx=5, pady=5)
        self.class_name_entry = tk.Entry(form_frame)
        self.class_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Faculty", bg="white").grid(
            row=1, column=0, padx=5, pady=5)
        self.class_faculty_entry = tk.Entry(form_frame)
        self.class_faculty_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons for CRUD actions
        button_frame = tk.Frame(class_tab, bg="white")
        button_frame.pack(pady=10)

        self.add_class_button = tk.Button(
            button_frame, text="Add Student", command=self.add_student, bg="#4CAF50", fg="white")
        self.add_class_button.grid(row=0, column=0, padx=10, pady=5)

        # self.add_class_button = tk.Button(button_frame, text="Add Class", command=self.add_class,
        #                                   bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Update Class", command=self.update_class,
                  bg="#FF9800", fg="white").grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Delete Class", command=self.delete_class,
                  bg="#F44336", fg="white").grid(row=0, column=2, padx=10, pady=5)

        # Treeview for displaying classes
        self.class_tree = Treeview(class_tab, columns=(
            "id", "name", "faculty"), show="headings")
        self.class_tree.heading("id", text="ID")
        self.class_tree.heading("name", text="Class Name")
        self.class_tree.heading("faculty", text="Faculty")
        self.class_tree.pack(fill="both", expand=True)

        self.class_tree.bind("<<TreeviewSelect>>", self.on_class_select)

        # Refresh the treeview with class data
        self.refresh_class_treeview()

    def create_subject_tab(self):
        # Tạo tab Subject
        subject_tab = tk.Frame(self.tab_control, bg="white")
        self.tab_control.add(subject_tab, text="Subjects")

        tk.Label(subject_tab, text="Subject Management", font=(
            "Helvetica", 16, "bold"), bg="white").pack(pady=10)

        # Form inputs for adding/updating subjects
        form_frame = tk.Frame(subject_tab, bg="white")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Subject Name", bg="white").grid(
            row=0, column=0, padx=5, pady=5)
        self.subject_name_entry = tk.Entry(form_frame)
        self.subject_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Credits", bg="white").grid(
            row=1, column=0, padx=5, pady=5)
        self.subject_credits_entry = tk.Entry(form_frame)
        self.subject_credits_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons for CRUD actions
        button_frame = tk.Frame(subject_tab, bg="white")
        button_frame.pack(pady=10)

        self.add_subject_button = tk.Button(
            button_frame, text="Add Student", command=self.add_subject, bg="#4CAF50", fg="white")
        self.add_subject_button.grid(row=0, column=0, padx=10, pady=5)

        tk.Button(button_frame, text="Update Subject", command=self.update_subject,
                  bg="#FF9800", fg="white").grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Delete Subject", command=self.delete_subject,
                  bg="#F44336", fg="white").grid(row=0, column=2, padx=10, pady=5)
        tk.Button(button_frame, text="Reset", command=self.reset_subject_form,
                  bg="#607D8B", fg="white").grid(row=0, column=3, padx=10, pady=5)

        # Treeview for displaying subjects
        self.subject_tree = ttk.Treeview(subject_tab, columns=(
            "id", "name", "credits"), show="headings")
        self.subject_tree.heading("id", text="ID")
        self.subject_tree.heading("name", text="Subject Name")
        self.subject_tree.heading("credits", text="Credits")
        self.subject_tree.column("id", width=50)
        self.subject_tree.column("name", width=200)
        self.subject_tree.column("credits", width=100)
        self.subject_tree.pack(fill="both", expand=True)

        # Gắn sự kiện chọn môn học
        self.subject_tree.bind("<<TreeviewSelect>>", self.on_subject_select)

        # Làm mới Treeview với dữ liệu môn học
        self.refresh_subject_treeview()

    def create_enrollment_tab(self):
        # Tạo tab Enrollment
        enrollment_tab = tk.Frame(self.tab_control, bg="white")
        self.tab_control.add(enrollment_tab, text="Enrollments")

        tk.Label(enrollment_tab, text="Enrollment Management", font=(
            "Helvetica", 16, "bold"), bg="white").pack(pady=10)

        # Form inputs for adding/updating enrollments
        form_frame = tk.Frame(enrollment_tab, bg="white")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Student ID", bg="white").grid(
            row=0, column=0, padx=5, pady=5)
        self.enrollment_student_id_entry = tk.Entry(form_frame)
        self.enrollment_student_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Subject ID", bg="white").grid(
            row=1, column=0, padx=5, pady=5)
        self.enrollment_subject_id_entry = tk.Entry(form_frame)
        self.enrollment_subject_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Semester", bg="white").grid(
            row=2, column=0, padx=5, pady=5)
        self.enrollment_semester_entry = tk.Entry(form_frame)
        self.enrollment_semester_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Year", bg="white").grid(
            row=3, column=0, padx=5, pady=5)
        self.enrollment_year_entry = tk.Entry(form_frame)
        self.enrollment_year_entry.grid(row=3, column=1, padx=5, pady=5)

        # # Thêm ô nhập liệu cho Grade
        # tk.Label(form_frame, text="Grade", bg="white").grid(
        #     row=4, column=0, padx=5, pady=5)
        # self.enrollment_grade_entry = tk.Entry(form_frame)
        # self.enrollment_grade_entry.grid(row=4, column=1, padx=5, pady=5)

        # Buttons for CRUD actions
        button_frame = tk.Frame(enrollment_tab, bg="white")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Enroll", command=self.add_enrollment,
                  bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Update Enrollment", command=self.update_enrollment,
                  bg="#FF9800", fg="white").grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Cancel Enrollment", command=self.delete_enrollment,
                  bg="#F44336", fg="white").grid(row=0, column=2, padx=10, pady=5)

        # Treeview for displaying enrollments
        self.enrollment_tree = Treeview(enrollment_tab, columns=(
            "id", "student_id", "subject_id", "semester", "year", "grade"), show="headings")
        self.enrollment_tree.heading("id", text="ID")
        self.enrollment_tree.heading("student_id", text="Student ID")
        self.enrollment_tree.heading("subject_id", text="Subject ID")
        self.enrollment_tree.heading("semester", text="Semester")
        self.enrollment_tree.heading("year", text="Year")
        # self.enrollment_tree.heading("grade", text="Grade")
        self.enrollment_tree.pack(fill="both", expand=True)

        self.enrollment_tree.bind(
            "<<TreeviewSelect>>", self.on_enrollment_select)

        # Refresh the treeview with enrollment data for a specific student
        self.refresh_enrollment_treeview()  # You can pass a student_id here if needed

    def refresh_student_treeview(self):
        # Xóa tất cả các mục hiện có trong Treeview
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        try:
            # Gọi API để lấy danh sách sinh viên
            students = APIClient.get_students()

            # Kiểm tra lỗi trong phản hồi từ API
            if "error" in students:
                messagebox.showerror("Error", f"Lỗi khi tải danh sách sinh viên: {
                    students['error']}")
                return

            # Duyệt qua danh sách sinh viên và chèn vào Treeview
            for student in students:
                self.student_tree.insert('', 'end', values=(
                    student.get('id'),
                    student.get('f_name'),
                    student.get('l_name'),
                    student.get('class_name'),
                    student.get('year'),
                    student.get('age'),
                    student.get('gender'),
                    student.get('birth'),
                    student.get('contact'),
                    student.get('email')
                ))
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi làm mới danh sách sinh viên: {str(e)}")

    def add_student(self):
        # Lấy class_id từ class_name trong Combobox
        class_name = self.class_combobox.get()
        class_id = self.class_dict.get(class_name)

        if not class_id:
            messagebox.showerror("Error", "Please select a valid class.")
            return

        data = {
            "f_name": self.f_name_entry.get(),
            "l_name": self.l_name_entry.get(),
            "class_id": class_id,  # Gửi class_id thay vì class_name
            "year": int(self.year_entry.get()) if self.year_entry.get() else None,
            "age": int(self.age_entry.get()) if self.age_entry.get() else None,
            "gender": self.gender_entry.get(),
            "birth": self.birth_entry.get(),
            "contact": self.contact_entry.get(),
            "email": self.email_entry.get()
        }

        try:
            response = APIClient.add_student(data)

            if "error" in response:
                messagebox.showerror("Error", f"Lỗi khi thêm sinh viên: {
                    response['error']}")
            else:
                messagebox.showinfo("Success", response.get(
                    "message", "Thêm sinh viên thành công"))
                self.refresh_student_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi thêm sinh viên: {str(e)}")

    def update_student(self):
        if not hasattr(self, 'selected_student_id'):
            messagebox.showerror("Error", "Please select a student to update.")
            return

        class_name = self.class_combobox.get()
        class_id = self.class_dict.get(class_name)

        if not class_id:
            messagebox.showerror("Error", "Please select a valid class.")
            return

        data = {
            "f_name": self.f_name_entry.get(),
            "l_name": self.l_name_entry.get(),
            "class_id": class_id,
            "year": int(self.year_entry.get()) if self.year_entry.get() else None,
            "age": int(self.age_entry.get()) if self.age_entry.get() else None,
            "gender": self.gender_entry.get(),
            "birth": self.birth_entry.get(),
            "contact": self.contact_entry.get(),
            "email": self.email_entry.get()
        }

        try:
            response = APIClient.update_student(self.selected_student_id, data)

            if "error" in response:
                messagebox.showerror("Error", f"Lỗi khi cập nhật sinh viên: {
                    response['error']}")
            else:
                messagebox.showinfo("Success", response.get(
                    "message", "Cập nhật sinh viên thành công"))
                self.refresh_student_treeview()
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi cập nhật sinh viên: {str(e)}")

    def delete_student(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Vui lòng chọn sinh viên để xóa!")
            return

        student_id = self.student_tree.item(selected_item)["values"][0]
        try:
            response = APIClient.delete_student(student_id)
            messagebox.showinfo("Success", response.get(
                "message", "Xóa sinh viên thành công"))
            self.refresh_student_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi xóa sinh viên: {str(e)}")

    def refresh_class_treeview(self):
        # Xóa dữ liệu hiện có trong Treeview
        for i in self.class_tree.get_children():
            self.class_tree.delete(i)

        # Lấy danh sách lớp học từ API và hiển thị
        try:
            classes = APIClient.get_classes()
            for class_data in classes:
                self.class_tree.insert('', 'end', values=(
                    class_data['id'], class_data['name'], class_data['faculty']
                ))
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi tải danh sách lớp: {str(e)}")

    def add_class(self):
        data = {
            "name": self.class_name_entry.get(),
            "faculty": self.class_faculty_entry.get()
        }
        try:
            response = APIClient.add_class(data)
            messagebox.showinfo("Success", response.get(
                "message", "Thêm lớp học thành công"))
            self.load_classes()
            self.refresh_class_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi thêm lớp học: {str(e)}")

    def update_class(self):
        # Lấy ID của lớp học được chọn trong Treeview
        selected_item = self.class_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Vui lòng chọn lớp học để cập nhật!")
            return

        class_id = self.class_tree.item(selected_item)["values"][0]
        data = {
            "name": self.class_name_entry.get(),
            "faculty": self.class_faculty_entry.get()
        }
        try:
            response = APIClient.update_class(class_id, data)
            messagebox.showinfo("Success", response.get(
                "message", "Cập nhật lớp học thành công"))
            self.load_classes()
            self.refresh_class_treeview()
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi cập nhật lớp học: {str(e)}")

    def delete_class(self):
        # Lấy ID của lớp học được chọn trong Treeview
        selected_item = self.class_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Vui lòng chọn lớp học để xóa!")
            return

        class_id = self.class_tree.item(selected_item)["values"][0]
        try:
            response = APIClient.delete_class(class_id)
            messagebox.showinfo("Success", response.get(
                "message", "Xóa lớp học thành công"))
            self.load_classes()
            self.refresh_class_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi xóa lớp học: {str(e)}")

    def refresh_subject_treeview(self):
        # Xóa tất cả các mục hiện có trong Treeview
        for item in self.subject_tree.get_children():
            self.subject_tree.delete(item)

        try:
            # Gọi API để lấy danh sách môn học
            subjects = APIClient.get_subjects()

            # Kiểm tra lỗi trong phản hồi từ API
            if "error" in subjects:
                messagebox.showerror("Error", f"Lỗi khi tải danh sách môn học: {
                    subjects['error']}")
                return

            # Duyệt qua danh sách môn học và chèn vào Treeview
            for subject in subjects:
                self.subject_tree.insert('', 'end', values=(
                    subject.get('id'),
                    subject.get('name'),
                    subject.get('credits')
                ))
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi làm mới danh sách môn học: {str(e)}")

    def add_subject(self):
        data = {
            "name": self.subject_name_entry.get(),
            "credits": int(self.subject_credits_entry.get()) if self.subject_credits_entry.get() else 0
        }

        try:
            response = APIClient.add_subject(data)

            if "error" in response:
                messagebox.showerror("Error", f"Lỗi khi thêm môn học: {
                    response['error']}")
            else:
                messagebox.showinfo("Success", response.get(
                    "message", "Thêm môn học thành công"))
                self.refresh_subject_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi thêm môn học: {str(e)}")

    def update_subject(self):
        if not hasattr(self, 'selected_subject_id'):
            messagebox.showerror("Error", "Vui lòng chọn môn học để cập nhật.")
            return

        data = {
            "name": self.subject_name_entry.get(),
            "credits": int(self.subject_credits_entry.get()) if self.subject_credits_entry.get() else 0
        }

        try:
            response = APIClient.update_subject(self.selected_subject_id, data)

            if "error" in response:
                messagebox.showerror("Error", f"Lỗi khi cập nhật môn học: {
                    response['error']}")
            else:
                messagebox.showinfo("Success", response.get(
                    "message", "Cập nhật môn học thành công"))
                self.refresh_subject_treeview()
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi cập nhật môn học: {str(e)}")

    def delete_subject(self):
        selected_item = self.subject_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Vui lòng chọn môn học để xóa!")
            return

        subject_id = self.subject_tree.item(selected_item[0])["values"][0]
        try:
            response = APIClient.delete_subject(subject_id)

            if "error" in response:
                messagebox.showerror("Error", f"Lỗi khi xóa môn học: {
                    response['error']}")
            else:
                messagebox.showinfo("Success", response.get(
                    "message", "Xóa môn học thành công"))
                self.refresh_subject_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi xóa môn học: {str(e)}")

    def refresh_enrollment_treeview(self, student_id=None):
        # Xóa dữ liệu hiện có trong Treeview
        for i in self.enrollment_tree.get_children():
            self.enrollment_tree.delete(i)

        try:
            enrollments = APIClient.get_enrollments(student_id)

            # Kiểm tra lỗi trong phản hồi
            if "error" in enrollments:
                messagebox.showerror("Error", f"Lỗi khi tải danh sách đăng ký môn học: {
                    enrollments['error']}")
                return

            for enrollment in enrollments:
                self.enrollment_tree.insert('', 'end', values=(
                    enrollment['id'], enrollment['student_id'], enrollment['subject_id'],
                    enrollment['semester'], enrollment['year']
                    # , enrollment.get('grade', '')
                ))
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi tải danh sách đăng ký môn học: {str(e)}")

    def add_enrollment(self):
        data = {
            "student_id": int(self.enrollment_student_id_entry.get()) if self.enrollment_student_id_entry.get() else None,
            "subject_id": int(self.enrollment_subject_id_entry.get()) if self.enrollment_subject_id_entry.get() else None,
            "semester": self.enrollment_semester_entry.get(),
            "year": int(self.enrollment_year_entry.get()) if self.enrollment_year_entry.get() else None
        }
        try:
            response = APIClient.add_enrollment(data)
            messagebox.showinfo("Success", response.get(
                "message", "Đăng ký môn học thành công"))
            self.refresh_enrollment_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi đăng ký môn học: {str(e)}")

    def update_enrollment(self):
        # Lấy ID của đăng ký môn học được chọn trong Treeview
        selected_item = self.enrollment_tree.selection()
        if not selected_item:
            messagebox.showerror(
                "Error", "Vui lòng chọn đăng ký môn học để cập nhật!")
            return

        enrollment_id = self.enrollment_tree.item(selected_item)["values"][0]
        data = {
            "student_id": int(self.enrollment_student_id_entry.get()) if self.enrollment_student_id_entry.get() else None,
            "subject_id": int(self.enrollment_subject_id_entry.get()) if self.enrollment_subject_id_entry.get() else None,
            "semester": self.enrollment_semester_entry.get(),
            "year": int(self.enrollment_year_entry.get()) if self.enrollment_year_entry.get() else None
        }
        try:
            response = APIClient.update_enrollment(enrollment_id, data)
            messagebox.showinfo("Success", response.get(
                "message", "Cập nhật đăng ký môn học thành công"))
            self.refresh_enrollment_treeview()
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi cập nhật đăng ký môn học: {str(e)}")

    def delete_enrollment(self):
        # Lấy ID của đăng ký môn học được chọn trong Treeview
        selected_item = self.enrollment_tree.selection()
        if not selected_item:
            messagebox.showerror(
                "Error", "Vui lòng chọn đăng ký môn học để hủy!")
            return

        enrollment_id = self.enrollment_tree.item(selected_item)["values"][0]
        try:
            response = APIClient.delete_enrollment(enrollment_id)
            messagebox.showinfo("Success", response.get(
                "message", "Hủy đăng ký môn học thành công"))
            self.refresh_enrollment_treeview()
        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi hủy đăng ký môn học: {str(e)}")

    def on_student_select(self, event):
        # Lấy hàng được chọn
        selected_item = self.student_tree.selection()
        if not selected_item:
            return  # Không có hàng nào được chọn

        # Lấy thông tin từ hàng được chọn
        student_info = self.student_tree.item(selected_item[0], "values")

        # Đưa dữ liệu lên form
        self.f_name_entry.delete(0, tk.END)
        self.f_name_entry.insert(0, student_info[1])

        self.l_name_entry.delete(0, tk.END)
        self.l_name_entry.insert(0, student_info[2])

        # self.course_entry.delete(0, tk.END)
        self.class_combobox.set(student_info[3])

        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, student_info[4])

        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, student_info[5])

        self.gender_entry.delete(0, tk.END)
        self.gender_entry.insert(0, student_info[6])

        self.birth_entry.delete(0, tk.END)
        self.birth_entry.insert(0, student_info[7])

        self.contact_entry.delete(0, tk.END)
        self.contact_entry.insert(0, student_info[8])

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, student_info[9])

        # Lưu ID của sinh viên hiện tại để có thể cập nhật sau này
        self.selected_student_id = student_info[0]

        # Vô hiệu hóa nút "Add Student"
        self.add_button.config(state=tk.DISABLED)

    def on_class_select(self, event):
        # Lấy hàng được chọn trong class_tree
        selected_item = self.class_tree.selection()
        if not selected_item:
            return  # Không có hàng nào được chọn

        # Lấy thông tin từ hàng được chọn
        class_info = self.class_tree.item(selected_item[0], "values")

        # Đưa dữ liệu lên form
        self.class_name_entry.delete(0, tk.END)
        self.class_name_entry.insert(0, class_info[1])

        self.class_faculty_entry.delete(0, tk.END)
        self.class_faculty_entry.insert(0, class_info[2])

        # Lưu ID của lớp học hiện tại để có thể cập nhật sau này
        self.selected_class_id = class_info[0]

        # Vô hiệu hóa nút "Add Class" (nếu có)
        self.add_class_button.config(state=tk.DISABLED)

    def on_subject_select(self, event):
        # Lấy hàng được chọn
        selected_item = self.subject_tree.selection()
        if not selected_item:
            return  # Không có hàng nào được chọn

        # Lấy thông tin từ hàng được chọn
        subject_info = self.subject_tree.item(selected_item[0], "values")

        # Đưa dữ liệu lên form
        self.subject_name_entry.delete(0, tk.END)
        self.subject_name_entry.insert(0, subject_info[1])

        self.subject_credits_entry.delete(0, tk.END)
        self.subject_credits_entry.insert(0, subject_info[2])

        # Lưu ID của môn học hiện tại để có thể cập nhật hoặc xóa sau này
        self.selected_subject_id = subject_info[0]

        # Vô hiệu hóa nút "Add Subject" (nếu có)
        self.add_subject_button.config(state=tk.DISABLED)

    def on_enrollment_select(self, event):
        # Lấy hàng được chọn trong Treeview
        selected_item = self.enrollment_tree.selection()
        if not selected_item:
            return  # Không có hàng nào được chọn

        # Lấy thông tin từ hàng được chọn
        enrollment_info = self.enrollment_tree.item(selected_item[0], "values")

        # Đưa dữ liệu lên form
        self.enrollment_student_id_entry.delete(0, tk.END)
        self.enrollment_student_id_entry.insert(
            0, enrollment_info[1])  # ID sinh viên

        self.enrollment_subject_id_entry.delete(0, tk.END)
        self.enrollment_subject_id_entry.insert(
            0, enrollment_info[2])  # ID môn học

        self.enrollment_semester_entry.delete(0, tk.END)
        self.enrollment_semester_entry.insert(0, enrollment_info[3])  # Kỳ học

        self.enrollment_year_entry.delete(0, tk.END)
        self.enrollment_year_entry.insert(0, enrollment_info[4])  # Năm học

        # self.grade_entry.delete(0, tk.END)
        # self.grade_entry.insert(0, enrollment_info[5])  # Điểm số

        # Lưu ID của bản ghi hiện tại để có thể cập nhật hoặc xóa sau này
        self.selected_enrollment_id = enrollment_info[0]

    def reset_form(self):
        # Xóa tất cả các trường nhập liệu
        self.f_name_entry.delete(0, tk.END)
        self.l_name_entry.delete(0, tk.END)
        # Đặt lại giá trị của Combobox cho class_name
        self.class_combobox.set("")
        self.year_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.birth_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

        # Bật lại nút "Add Student"
        self.add_button.config(state=tk.NORMAL)

        # Xóa selected_student_id để ngăn ngừa cập nhật không mong muốn
        if hasattr(self, 'selected_student_id'):
            del self.selected_student_id

    def reset_class_form(self):
        # Xóa tất cả các trường nhập liệu của lớp học
        self.class_name_entry.delete(0, tk.END)
        self.class_year_entry.delete(0, tk.END)
        self.class_teacher_entry.delete(0, tk.END)

        # Bật lại nút "Add Class"
        self.add_class_button.config(state=tk.NORMAL)

        # Xóa selected_class_id để ngăn ngừa cập nhật không mong muốn
        if hasattr(self, 'selected_class_id'):
            del self.selected_class_id

    def reset_subject_form(self):
        # Xóa tất cả các trường nhập liệu của môn học
        self.subject_name_entry.delete(0, tk.END)
        self.subject_code_entry.delete(0, tk.END)
        self.subject_credit_entry.delete(0, tk.END)

        # Bật lại nút "Add Subject"
        self.add_subject_button.config(state=tk.NORMAL)

        # Xóa selected_subject_id để ngăn ngừa cập nhật không mong muốn
        if hasattr(self, 'selected_subject_id'):
            del self.selected_subject_id

    def load_classes(self):
        try:
            # Gọi API để lấy danh sách lớp học
            classes = APIClient.get_classes()

            # Kiểm tra lỗi trong phản hồi từ API
            if "error" in classes:
                messagebox.showerror("Error", f"Lỗi khi tải danh sách lớp học: {
                    classes['error']}")
                return

            # Tạo dictionary để ánh xạ class_name với class_id
            self.class_dict = {cls['name']: cls['id'] for cls in classes}

            # Nạp tên các lớp vào Combobox
            self.class_combobox['values'] = list(self.class_dict.keys())

        except Exception as e:
            messagebox.showerror(
                "Error", f"Lỗi khi tải danh sách lớp học: {str(e)}")

    def reset_subject_form(self):
        # Xóa nội dung các trường nhập liệu
        self.subject_name_entry.delete(0, tk.END)
        self.subject_credits_entry.delete(0, tk.END)

        # Bật lại nút "Add Subject" nếu nó bị vô hiệu hóa
        self.add_subject_button.config(state=tk.NORMAL)

        # Xóa selected_subject_id để ngăn ngừa cập nhật hoặc xóa không mong muốn
        if hasattr(self, 'selected_subject_id'):
            del self.selected_subject_id
