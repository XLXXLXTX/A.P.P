"""
Categories - will contain a collection of all categories we enter. 
Examples of categories: Amplifiers, Receivers, Speakers,  Turntables and so on
"""

from json import JSONEncoder, JSONDecodeError, loads, dump
from classes.category import Category, CategoryDecoder, CategoryEncoder

class CategoriesEncoder(JSONEncoder):
    """ From Python object to json representation """

    def default(self, o :Category):
        return o.__dict__

#Define Categories class
class Categories:
    """ holds a list with all Category objects """

    categories = []

    @classmethod
    def load_categories(cls):
        """ reads the categories.txt file and re-compose the Python objects
            from the json representation of categories. The content of the
            categories.txt file should look something like:

            "{\"name\": \"Amplifiers\"}"
            "{\"name\": \"Receivers\"}"

            Basically, we read the file line by line and from those lines we
            recreate the Pyhton objects.

            Also we take care to not multiply the elements in the categories
            list. We have avoided this by overloading the __eq__() operator in
            Category class. More on this during the lectures.
        """
        dc = CategoryDecoder()

        try:
            with open("categories.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_category = dc.decode(data)
                    if decoded_category not in cls.categories:
                        cls.categories.append(decoded_category)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.categories = []
        return cls.categories
    

    @classmethod
    def remove_category(cls, category :Category) -> None:
        """ Removes a category from the categories collection. We pass the category
            to be removed as a parameter to teh function and then, as a first step
            we remove it from the class variable 'categories'. Then, in a second step
            we iterate that collection and we serialize element by element
        """
        #IMPORTANT ----------
        cls.load_categories()
        #IMPORTANT ----------

        if category in cls.categories:
            cls.categories.remove(category)
            with open("categories.txt", 'w') as f:
                for cat in cls.categories:
                    ce = CategoryEncoder()
                    encoded_category = ce.encode(cat)
                    dump(encoded_category, f)
                    f.write("\n")
    
    @classmethod
    def add_category(cls, category :Category) -> None:
        """ Adds a new category in the categories collection. We need to save the
            new category on the disk too, so we have to call teh Encoder class to
            transform teh Python object in a JSON representation
        """

        #IMPORTANT ----------
        cls.load_categories()
        #IMPORTANT ----------

        if category not in cls.categories:
            cls.categories.append(category)
            with open("categories.txt", 'a') as f:
                ce = CategoryEncoder()
                encoded_category = ce.encode(category)
                dump(encoded_category, f)
                f.write("\n")

    @classmethod
    def list_categories(cls) -> None:
        """
        First we read the file categories.txt and we deserialize the collection
        of categories. Then we iterate the collection and we print each category
        """
        
        #IMPORTANT ----------
        cls.load_categories()
        #IMPORTANT ----------

        for c in cls.categories:
            print(c.get_details())