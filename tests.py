import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct


# 10 Units tests

def test_create_multiple_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', True)

    assert len(question.choices) == 3
    assert question.choices[0].text == 'a'
    assert not question.choices[0].is_correct
    assert question.choices[1].text == 'b'
    assert question.choices[1].is_correct
    assert question.choices[2].text == 'c'
    assert question.choices[2].is_correct


def test_generate_choice_id():
    question = Question(title='q1')

    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)
    choice3 = question.add_choice('c', True)

    assert choice1.id == 1
    assert choice2.id == 2
    assert choice3.id == 3


def test_set_correct_choice():
    question = Question(title = 'avaliação')
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)
    choice3 = question.add_choice('c', False)
    choice4 = question.add_choice('d', True)
    choice5 = question.add_choice('e', True)

    question.set_correct_choices([choice2.id, choice4.id, choice5.id])

    assert choice1.is_correct == False
    assert choice2.is_correct == True
    assert choice3.is_correct == False
    assert choice4.is_correct == True
    assert choice5.is_correct == True


def test_remove_choice_by_id():
    question = Question(title = 'iza')
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)
    choice3 = question.add_choice('c', False)
    choice4 = question.add_choice('d', True)

    question.remove_choice_by_id(choice1.id)
    question.remove_choice_by_id(choice3.id)

    assert len(question.choices) == 2
    assert question.choices[0].id == choice2.id
    assert question.choices[1].id == choice4.id

def test_size_of_questions():
    question1 = Question(title = 'avaliação')
    question2 = Question(title = 'bia')

    question1.add_choice('a', False)
    question2.add_choice('a', False)
    question2.add_choice('b', True)

    assert len(question1.choices) == 1
    assert len(question2.choices) == 2
 
def test_create_question_with_invalid_points():    
    with pytest.raises(Exception):
        Question(title='avaliação', points=0)

def test_check_valid_choice_id():
    question = Question (title = 'tarken', points = 10)
    choice1 = question.add_choice('a', False)
    
    with pytest.raises(Exception):
        question.remove_choice_by_id(777)

def test_remove_all_choices():
    question = Question (title = 'tarken', points = 10)
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)

    question.remove_all_choices()

    assert len(question.choices) == 0

def test_correct_selected_choices():
    q = Question(title="avaliação", max_selections = 1)
    c1 = q.add_choice("a", True)
    c2 = q.add_choice("b", False)

    with pytest.raises(Exception):
        q.correct_selected_choices([c1.id, c2.id])


def test_correct_selected_empty():
    q = Question(title="avaliação")
    c1 = q.add_choice("a", True)
    c2 = q.add_choice("a", False)

    result = q.correct_selected_choices([])

    assert result == []


# Tests with fixture

@pytest.fixture
def question_with_choices():
    question = Question(title="avaliação", max_selections = 2)
    choice1 = question.add_choice("a", True)
    choice2 = question.add_choice("b", False)
    choice3 = question.add_choice("c", True)
    choice4 = question.add_choice("d", False)

    return question, choice1, choice2, choice3, choice4

def test_changing_the_choice(question_with_choices):
    question, choice1, choice2, choice3, choice4 = question_with_choices

    assert choice1.is_correct == True
    choice1.is_correct = False
    assert choice1.is_correct == False

    assert choice2.is_correct == False
    choice2.is_correct = True
    assert choice2.is_correct == True

def test_changing_the_question_name(question_with_choices):
    question, choice1, choice2, choice3, choice4 = question_with_choices

    assert question.title == "avaliação"
    question.title = "iza"
    assert question.title == "iza"