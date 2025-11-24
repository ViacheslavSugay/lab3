import signal
import sys

from call_logic import pars

def signal_handler(sig: int, frame) -> None:
    """Обработчик сигналов для Ctrl+C и Ctrl+f2"""
    if sig == signal.SIGINT:
        print("\nПользователь завершил программу")
        sys.exit(0)


def main() -> None:
    print('math_func:\n'
          ' factorial\n'
          ' factorial_recursive\n'
          ' fibo\n'
          ' fibo_recursive\n')
    print('sorts_func:\n'
          ' bubble\n'
          ' quick\n'
          ' counting\n'
          ' radix\n'
          ' bucket\n'
          ' heap\n')
    print('Stack_method:\n'
          'pop\n'
          'push\n'
          'peek\n'
          'is_empty\n'
          'len\n'
          'min\n')
    print('Queue_method:\n'
          'enqueue\n'
          'dequeue\n'
          'is_empty\n'
          'front\n'
          'len\n')

    print(
        'Введите через пробел тип функций(math или sorts), название функции, для sorts введите список чисел в квадратных скобках через запятую, '
        'для math просто число\n')

    print('Для структур данных введите тип структуры (stack иди queue), название метода и значание, если оно нужно для метода\n')
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            n = input()
            print(pars(n))
        except KeyboardInterrupt:
            break
        except EOFError:
            print("\nКонец файла")
            break
        except Exception as e:
            print(f"Ошибка: {e}")
            continue

if __name__ == "__main__":
    main()
