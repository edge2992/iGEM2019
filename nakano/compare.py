from nakano import image_processing

def two_list_match_rate(list_1, list_2, threshold=5):
    match_points = 0
    for coordinate in list_1:
        if any( abs(coordinate[0]-point[0]) <= threshold and abs(coordinate[1]-point[1]) <= threshold for point in list_2 ) :
            match_points += 1
    return match_points / len(list_1)


def compare_two_images(img_path_1, img_path_2):
    return True

if __name__ == '__main__':
    print(two_list_match_rate([[10,20],[100,200]], [[10,20],[103,200],[109,200]], threshold=5))
