# A mi részünkről most a lényeg itt történik
# A set_keyboard_input-al készítünk egy tömböt, ami sorban tartalmazza a kívánt inputokat
# A get_display_output-al pedig ki tudjuk szedni a tényleges outputokat
# Onnantól meg assert és megvan a teszt

from mocking import set_keyboard_input, get_display_output
from dummy_function import dummy_function

def test_dummy_function():
    set_keyboard_input(["abc"])

    dummy_function()

    output = get_display_output()

    assert output == ['>',3,4,5]
