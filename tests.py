from unittest import TestCase, main

from utils import (
    revert_string,
    append_elements_to_array,
    calculate_string_operation,
    copy_dict
)

class MyTestCase(TestCase):

    def test_revert_string(self):
        self.assertEqual(
            revert_string('snake'), 
            'ekans'
        )
  

    # def test_rever_string_invalid_parameter(self):
    #     self.assertEqual(
    #         revert_string(1),
    #         None
    #     )

    def test_append_elements_to_array(self):
        original_array = [1,2,3]
        expected_array_after_func_call = [1,2,3,4,5]
        self.assertEqual(
            append_elements_to_array(original_array, 4, 5),
            expected_array_after_func_call
        )
    
    def test_calculate_string_operation(self):
        operation = '(50 - 10)/2**2'

        self.assertEqual(
            calculate_string_operation(operation),
            10
        )

    # def test_calculate_invalid_string_operation(self):
    #     self.assertEqual(
    #         calculate_string_operation('a'),
    #         None
    #     )

    def test_make_dict_copy(self):
        original_dict = {
            'name': 'Topicos Avançados em Engenharia de Software'
        }
        original_dict_copy = copy_dict(original_dict)
        original_dict_copy['description'] = 'Ter - Qui'

        self.assertNotEqual(
            original_dict,
            original_dict_copy
        )

if __name__ == '__main__':
    main()
