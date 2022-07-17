from src.solver import prep_game, solver


def test_can_call_solver():
    solver()


def test_solver_can_prep_a_game():
    game = prep_game()
    assert type(game["center"][0]) is list
