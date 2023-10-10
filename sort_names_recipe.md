# Sort Names Route Design Recipe

Test-drive a new route POST /sort-names which receives a list of names (as a comma-separated string) and return the same list, sorted in alphabetical order.

Here's a description of the expected behaviour:

    # Request:
    POST http://localhost:5001/sort-names

    # With body parameters:
    names=Joe,Alice,Zoe,Julia,Kieran

    # Expected response (sorted list of names):
    Alice,Joe,Julia,Kieran,Zoe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /sort_names
  name: a string of comma seperated names (no spaces)



```

## 2. Create Examples as Tests

```python
# POST /sort-names
# With names=Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK)
"""
Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
# With names=Aaaaaa,Aaaaaz,Aaaaab
# Expected response (200 OK)
"""
Aaaaaa,Aaaaab,Aaaaaz
"""

# POST /sort-names
# With no names
# Expected response Invalid Request code
"""
You didn't submit any names!
"""


```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
