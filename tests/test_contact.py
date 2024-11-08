import unittest
from main import ContactCreate, Contact

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    # def create_contact(contact: ContactCreate):
    #     db_contact = Contact.model_validate(contact)
    #     # session.add(db_contact)
    #     # session.commit()
    #     # session.refresh(db_contact)
    #     # return db_contact



if __name__ == '__main__':
    unittest.main()