import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Y3zfcONHo2VXJV_CQbXmR56Kw0YqR296Bvqz_HbcbGU"
}

def get_upcoming(page=1):
    global headers
    url = f"https://api.themoviedb.org/3/movie/upcoming?language=en-US&page={page}"
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data = response.json()
        return data.get("results")
    
    return []

def get_popular(page=1):
    global headers
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data = response.json()
        return data.get("results")
    
    return []

def get_movie_details(id):
    global headers
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data = response.json()
        return data
    
    return {}

def get_similar_movies(id):
    global headers
    url = f"https://api.themoviedb.org/3/movie/{id}/similar?language=en-US&page=1"
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data = response.json()
        return data.get("results")
    
    return []

def get_movie_trailer(id):
    global headers
    url = f"https://api.themoviedb.org/3/movie/{id}/videos?language=en-US"
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data = response.json().get("results")
        return [video for video in data if video.get('type')== 'Trailer']
    
    return []