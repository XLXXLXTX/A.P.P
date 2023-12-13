# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Categories - will contain a collection of all categories we enter. 
Examples of categories: Amplifiers, Receivers, Speakers,  Turntables and so on
"""

from typing import List

from json import JSONDecodeError, loads, dump

from classes.category import Category, CategoryDecoder, CategoryEncoder

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

#Define Categories class
class Categories:
    """ holds a list with all Category objects """

    categories = []

    @classmethod
    def load_categories(cls) -> List[Category]:
        logging.debug(f'Categories.load_categories() ...')

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
    def add_category(cls, category :Category) -> bool:
        logging.debug(f'Categories.add_category(category : {category.get_details}) ...')

        """ Adds a new category in the categories collection. We need to save the
            new category on the disk too, so we have to call teh Encoder class to
            transform teh Python object in a JSON representation
        """

        # fill the memory list with the categories from the file
        cls.load_categories()
        
        # check if it exists in the list and remove it
        if category not in cls.categories:
            cls.categories.append(category)
            # overwrite the file with the new memory list
            with open("categories.txt", 'a') as f:
                ce = CategoryEncoder()
                encoded_category = ce.encode(category)
                dump(encoded_category, f)
                f.write("\n")
            return True
        
        return False

    @classmethod
    def remove_category(cls, category :Category) -> bool:
        logging.debug(f'Categories.remove_category(category : {category.get_details}) ...')

        """ Removes a category from the categories collection. We pass the category
            to be removed as a parameter to teh function and then, as a first step
            we remove it from the class variable 'categories'. Then, in a second step
            we iterate that collection and we serialize element by element
        """
        # fill the memory list with the categories from the file
        cls.load_categories()

        # check if it exists in the list and remove it
        if category in cls.categories:
            cls.categories.remove(category)
            # overwrite the file with the new memory list
            with open("categories.txt", 'w') as f:
                for cat in cls.categories:
                    ce = CategoryEncoder()
                    encoded_category = ce.encode(cat)
                    dump(encoded_category, f)
                    f.write("\n")
            return True
        
        return False

    @classmethod
    def list_categories(cls) -> None:
        logging.debug(f'Categories.list_categories() ...')

        """
        First we read the file categories.txt and we deserialize the collection
        of categories. Then we iterate the collection and we print each category
        """
        
        cls.categories = cls.load_categories()

        if len(cls.categories) == 0:
            print(f'\tNo categories to show, Add some categories first!')
            return

        print(f'\nCategories list:\n')

        for c in cls.categories:
            print(f'\t-{c.name}')

        print(f'\n')