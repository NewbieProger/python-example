from colorama import Fore, Style, init

from engine.engine import Engine2D, Circle, Triangle, Rectangle

init(autoreset=True)


def test_add_shape():
    engine = Engine2D()
    circle = Circle((0, 1), 5)
    engine.add_shape(circle)
    assert len(engine.canvas) == 1
    assert engine.canvas[0] == circle


def test_set_color():
    engine = Engine2D()
    engine.set_color(Fore.RED)
    assert engine.current_color == Fore.RED


def test_draw_with_color(capsys):
    engine = Engine2D()
    engine.set_color(Fore.BLUE)
    circle = Circle((0, 1), 5)
    engine.add_shape(circle)

    engine.draw()
    captured = capsys.readouterr()
    assert "Drawing Circle: (0, 1) with radius 5" in captured.out
    assert Fore.BLUE in captured.out


def test_draw_without_color(capsys):
    engine = Engine2D()
    circle = Circle((0, 1), 5)
    engine.add_shape(circle)

    engine.draw()
    captured = capsys.readouterr()
    assert "Drawing Circle: (0, 1) with radius 5" in captured.out
    assert Fore.WHITE in captured.out


def test_set_color_and_draw_with_color(capsys):
    engine = Engine2D()
    engine.set_color(Fore.RED)
    circle = Circle((0, 1), 5)
    engine.add_shape(circle)

    engine.set_color(Fore.GREEN)
    engine.draw()

    captured = capsys.readouterr()
    assert "Drawing Circle: (0, 1) with radius 5" in captured.out
    assert Fore.GREEN in captured.out


def test_draw_multiple_shapes(capsys):
    engine = Engine2D()
    engine.set_color(Fore.RED)
    circle = Circle((0, 1), 5)
    triangle = Triangle([(0, 0), (1, 0), (0, 1)])
    rectangle = Rectangle((1, 1), 3, 2)
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)

    engine.draw()

    captured = capsys.readouterr()
    assert "Drawing Circle: (0, 1) with radius 5" in captured.out
    assert "Drawing Triangle: [(0, 0), (1, 0), (0, 1)]" in captured.out
    assert "Drawing Rectangle: (1, 1), width 3, height 2" in captured.out


def test_draw_with_color_change(capsys):
    engine = Engine2D()
    engine.set_color(Fore.RED)
    circle = Circle((0, 1), 5)
    engine.add_shape(circle)

    engine.set_color(Fore.GREEN)
    engine.draw()

    engine.set_color(Fore.BLUE)
    engine.draw()

    captured = capsys.readouterr()
    expected_output = "Drawing Circle: (0, 1) with radius 5"
    actual_output = captured.out.strip().replace('\x1b[32m', '').replace('\x1b[34m', '')
    assert expected_output == actual_output


def test_draw_with_color_reset(capsys):
    engine = Engine2D()
    engine.set_color(Fore.RED)
    circle = Circle((0, 1), 5)
    engine.add_shape(circle)

    engine.set_color(Style.RESET_ALL)
    engine.draw()

    captured = capsys.readouterr()
    expected_output = f'{Style.RESET_ALL}Drawing Circle: (0, 1) with radius 5'
    assert expected_output in captured.out


