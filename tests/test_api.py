import requests


class TestJSONPlaceholderAPI:
    """
    Test cases for the JSONPlaceHolder API of three scenarios:
    1) Fetching a user (GET /users/1)
    2) Creating a new post (POST /posts)
    3) Handling a non-existent user (GET /users/999)
    """
    def test_fetch_user_successfully(self):
        """
        Tests the '/users/1' endpoint. Validates:
        - 200 status code (OK)
        - Presence of 'id', 'name', and 'email' in the data
        """
        # Send GET request to fetch user data from the API
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")

        # Verify that the response status is 200 (OK),
        # ensure API was successfully retrieved
        assert response.status_code == 200 

        # Parse the JSON response
        user_data = response.json()
        #Check if the following keys exist in the response data
        assert 'id' in user_data 
        assert 'name' in user_data
        assert 'email' in user_data
    
    def test_create_new_post(self):
        """
         Tests the '/posts' endpoint. Validates:
        - 201 status code (Created)
        - Presence of 'id', 'title', 'body', 'userId' in created post. 
        """
        #Prepare data for creating a new post
        post_data = {
            "title": "New Post",
            "body": "This is an example of a new post.",
            "userId": 1
        }

        # Send POST request to create a new post
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)

        # Verify that the response status code is 201 (Created)
        assert response.status_code == 201

        # Parse the JSON response
        post_created = response.json()
        # Check that the return data data contains the expected fields.
        assert 'id' in post_created
        assert post_created["title"] == post_data["title"]
        assert post_created["body"] == post_data["body"]
        assert post_created["userId"] == post_data["userId"]
    
    def test_nonexistent_user(self):
        """
          Tests the '/users/999' endpoint. Validates:
        - 404 status code (Not Found)
        - The response contins an error message.
        """
        # Send GET request to fetch user data for a non-existent user
        response = requests.get("https://jsonplaceholder.typicode.com/users/999")

        # Assert that the response status is 404 (Not Found)
        assert response.status_code == 404

        # Parse the JSON response
        error_response = response.json()

        # Validate that the response is empty
        assert error_response == {}
