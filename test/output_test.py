import pytest

import logic
from entities import Slide, Photo, Orientation
from input_state import InputState
from output_state import OutputState


def make_stupid_slide(id):
    return Slide([make_stupid_photo(id)])


def make_stupid_photo(id):
    return Photo(id, Orientation.HORIZONTAL, [])


def make_vertical_photo(id):
    return Photo(id, Orientation.VERTICAL, [])


def make_stupid_input(size):
    return InputState([make_stupid_photo(id) for id in range(size)])


def test_emptySolutionIsValid():
    input = InputState([])
    output = OutputState([])
    assert logic.validate(input, output)


def test_trivialSolutionIsValid():
    input = InputState([make_stupid_photo(0)])
    output = OutputState([make_stupid_slide(0)])
    assert logic.validate(input, output)


def test_validatorCanRecognizePictureBeingUsedTwice():
    input = InputState([make_stupid_photo(0)])
    output = OutputState([make_stupid_slide(0),
                          make_stupid_slide(0)])
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, output)


def test_validatorCanRecognizePictureNotFromInput():
    input = InputState([make_stupid_photo(0)])
    output = OutputState([make_stupid_slide(0),
                          make_stupid_slide(1)])
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, output)


def test_validatorCanRecognizeInputWithInvalidId():
    input = InputState([make_stupid_photo(1)])
    output = OutputState([make_stupid_slide(0)])
    with pytest.raises(logic.InvalidInput):
        logic.validate(input, output)


def test_validatorCanRecognizeHorizontalPhotoBeingPutWithHorizontalPhotoInSlide():
    input = make_stupid_input(2)
    output = OutputState([Slide([make_stupid_photo(0), make_stupid_photo(1)])])
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, output)


def test_validatorCanRecognizeVerticalPhotoBeingPutWithHorizontalPhotoInSlide():
    vertical_photo = Photo(0, Orientation.VERTICAL, [])
    input = InputState([vertical_photo, make_stupid_photo(1)])
    output = OutputState([Slide([vertical_photo, make_stupid_photo(1)])])
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, output)


def test_validatorCanRecognizeSingleVerticalPhotoAsInvalidSlide():
    vertical_photo = Photo(0, Orientation.VERTICAL, [])
    input = InputState([vertical_photo])
    output = OutputState([Slide([vertical_photo])])
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, output)


def test_validatorCanRecognizeTooManyVerticalPhotosAsInvalidSlide():
    input = InputState([make_vertical_photo(id) for id in range(5)])
    output = OutputState([Slide([make_vertical_photo(id) for id in range(3)])])
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, output)


def test_nonSlideObjectInOutputIsInvalid():
    input = make_stupid_input(5)
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, OutputState([make_stupid_slide(0), "quack"]))
    with pytest.raises(logic.InvalidSolution):
        logic.validate(input, OutputState(
            [make_stupid_slide(0), make_stupid_photo(1)]))
