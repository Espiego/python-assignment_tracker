# assignment_tracker.py

class AssignmentTracker:
    def __init__(self):
        """
        Initialize the tracker with an empty dictionary for student assignments.
        Each student will have a list of assignments with their completion status.
        """
        self.students = {}

    def add_student(self, name):
        """
        Add a new student to the tracker.
        """
        if name not in self.students:
            self.students[name] = {}
        else:
            print(f"{name} is already in the system.")

    def add_assignment(self, student_name, assignment_name):
        """
        Add an assignment to a student's record.
        By default, the assignment is marked as 'pending'.
        """
        if student_name in self.students:
            self.students[student_name][assignment_name] = 'pending'
        else:
            print(f"{student_name} is not in the system. Please add them first.")

    def mark_completed(self, student_name, assignment_name):
        """
        Mark a specific assignment as 'completed' for a student.
        """
        if student_name in self.students and assignment_name in self.students[student_name]:
            self.students[student_name][assignment_name] = 'completed'
        else:
            print(f"Assignment or student not found.")

    def generate_report(self):
        """
        Generate a report showing the assignment completion status for all students.
        """
        for student, assignments in self.students.items():
            print(f"\nReport for {student}:")
            for assignment, status in assignments.items():
                print(f"{assignment}: {status}")

    def pending_assignments(self, student_name):
        """
        List all pending assignments for a specific student.
        """
        if student_name in self.students:
            pending = [a for a, s in self.students[student_name].items() if s == 'pending']
            return pending if pending else "No pending assignments."
        else:
            return f"{student_name} not found."

# Example usage
if __name__ == "__main__":
    tracker = AssignmentTracker()

    # Adding students
    tracker.add_student('Alice')
    tracker.add_student('Bob')

    # Adding assignments
    tracker.add_assignment('Alice', 'Math Homework')
    tracker.add_assignment('Alice', 'Science Project')
    tracker.add_assignment('Bob', 'History Essay')

    # Marking assignments as completed
    tracker.mark_completed('Alice', 'Math Homework')

    # Generating a report for all students
    tracker.generate_report()

    # Checking pending assignments for a specific student
    print("\nPending assignments for Alice:")
    print(tracker.pending_assignments('Alice'))
