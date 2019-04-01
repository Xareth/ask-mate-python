import connection
import uuid
import time
import util
import os


def delete_element(element_type, element_id):

    # delete file if exists
    data = connection.read_file(f'{element_type}.csv')
    try:
        deleted_element_img_path = [element['image'] for element in data if element['id'] == element_id][0]
        file_name = deleted_element_img_path.split("/")[1]
        if file_name:
            os.remove(f"static/images/{file_name}")
    except IndexError:
        pass

    # delete element
    updated_data = [data_element for data_element in data if data_element['id'] != element_id]
    connection.write_file(updated_data, f'{element_type}.csv')

    # if question is deleted - also delete corresponding answers
    if element_type == "questions":
        answers = connection.read_file('answers.csv')

        # delete answer's image
        img_paths_of_deleted_answers = [answer['image'] for answer in answers if answer['question_id'] == element_id]
        for img_path in img_paths_of_deleted_answers:
            try:
                file_name = img_path.split("/")[1]
                if file_name:
                    os.remove(f"static/images/{file_name}")
            except IndexError:
                pass
            
        # delete answer
        updated_answers = [answer for answer in answers if answer['question_id'] != element_id]
        connection.write_file(updated_answers, 'answers.csv')


def update_image(file_type, filename, id):
    data = connection.read_file(f"{file_type}.csv")
    for element in data:
        if element['id'] == id:
            element['image'] = 'images/' + filename
    connection.write_file(data, f"{file_type}.csv")


def change_vote(file_type, id, change_step):
    data = connection.read_file(f"{file_type}.csv")
    for element in data:
        if element['id'] == id:
            element['vote_number'] = str(int(element['vote_number']) + change_step)
    connection.write_file(data, f"{file_type}.csv")







