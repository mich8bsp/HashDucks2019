from entities import Orientation, Slide
from input_state import InputState
from output_state import OutputState
import knapsack


def calc_pair_score(slide1, slide2):
    intersections = len(slide1.tags.intersection(slide2.tags))

    if intersections > len(slide1.tags):
        if len(slide1.tags) > len(slide2.tags):
            return len(slide2.tags)
        return len(slide1.tags)
    if intersections > len(slide2.tags):
        return len(slide2.tags)
    return intersections


def calc_score(slides):
    score = 0
    for index, slide in enumerate(slides):
        if index + 1 < len(slides):
            score += calc_pair_score(slide, slides[index + 1])

    return score


def run_logic(input_state):
    images = input_state.images
    if len(images) == 1:
        image = images[0]
        if image.orientation == Orientation.VERTICAL:
            raise Exception("WTF")
        output_state = OutputState([image.id])
    else:
        if images[0].orientation == Orientation.HORIZONTAL:
            output_state = OutputState([Slide([images[0]])])
        elif images[1].orientation == Orientation.HORIZONTAL:
            output_state = OutputState([Slide([images[1]])])
        else:
            output_state = OutputState([Slide([images[0], images[1]])])
    return output_state


def arrange_vertical_images(photos):
    matching_photos = []
    for photo in photos:
        if photo.should_check:
            remaining_photos = photos.copy()
            best_matching_photo = {}
            max_match = -1
            for other_photo in remaining_photos:
                if other_photo.should_check:
                    if photo != other_photo:
                        new_match = len(photo.tags.union(other_photo.tags))
                        if new_match > max_match:
                            best_matching_photo = other_photo
                            max_match = new_match
            if max_match != -1:
                matching_photos.append(Slide([photo, best_matching_photo]))
                best_matching_photo.should_check = False
                photo.should_check = False
    return matching_photos
