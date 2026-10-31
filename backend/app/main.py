# from fastapi import FastAPI, status, HTTPException, Path, Query
# import json

# app = FastAPI(title="Project101 API")

# # helper function
# def load_data():
#     with open("students.json", "r") as file:
#         return json.load(file)
        
# @app.get("/student")
# def get_all_student() -> dict:
#     return load_data()

# #path parameter
# @app.get("/student/{student_id}")
# def get_student(
#     student_id : str = Path(
#     ...,
#     description="The Id of the student",
#     examples=["S003"]
#     )
#     ) -> dict:
#     data = load_data()
    
#     if student_id not in data:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"No student with {student_id}"
#         )
    
#     return data[student_id]

# # Query Parameter
# @app.get("/filter")
# def filter_student(course : str = Query(None)):
#     data = load_data()
    
#     if course is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="not found"
#         )
        
#     filtered = {}
#     for student_id, info in data.items():
#         if info["course"].lower() == course.lower():
#             filtered[student_id] = info
            
#     return filtered

# """
# Sorting
# """

# sort_fields = ["marks", "age", "name"]
# order_by = ["asc", "desc"]
# # sorting 
# @app.get("/sort")
# def sort(
#     sort_by : str,
#     order : str
# ):
#     data = load_data()
    
#     if sort_by not in sort_fields:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Invalid sort field"
#         )
        
#     if order not in order_by:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Invalid order"
#         )
        
#     student = []
#     for student_id, info in data.items():
#         info["id"] = student_id
#         student.append(info)
        
#     reverse = (order=="desc")
#     sorted_list = sorted(
#         student,
#         key=lambda student: student[sort_by],
#         reverse=reverse
#     )
    
#     return sorted_list

# """
# Pagination
# """
# @app.get("/paginate")
# def pagination(page : int = Query(1, ge=1), limit : int = Query(2, ge=1, le=100)):
#     data = load_data()
    
#     students = []
    
#     for student_id, info in data.items():
#         info["id"] = student_id
#         students.append(info)
        
#     start = (page - 1) * limit
#     end = start + limit
    
#     page_students = students[start : end]
    
#     total_students = len(students)
    
#     return {
#         "page" : page,
#         "limit" : limit,
#         "total_students" : total_students,
#         "students" : page_students
#     }

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI!",
        "status": "success"
    }

# Write your /health endpoint below
@app.get("/health")
def health_check():
    return {
  "status": "healthy",
  "application": "FastAPI Learning Project"
}