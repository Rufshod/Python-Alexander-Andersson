import random


questions = [
    # Existing questions
    {
        "question": "{} - {}",
        "answer": lambda x, y: x - y,
        "numbers": lambda: (random.randint(1, 9999), random.randint(-9999, -2500))
    },
    {
        "question": "{} + {}",
        "answer": lambda x, y: x + y,
        "numbers": lambda: (random.randint(99, 9999), random.randint(-9999, -99))
    },
    {
        "question": "{} * {}",
        "answer": lambda x, y: x * y,
        "numbers": lambda: (random.randint(1, 30), random.randint(1, 399))
    },
    {
        "question": "{} / {}",
        "answer": lambda x, y: x / y,
        "numbers": lambda: (random.randint(1, 99), random.randint(1, 99))
    },    
    {
        "question": "{} // {}",
        "answer": lambda x, y: x // y,
        "numbers": lambda: (random.randint(1, 250), random.randint(1, 25))
    },
    {
        "question": "{} % {}",
        "answer": lambda x, y: x % y,
        "numbers": lambda: (random.randint(1, 100), random.randint(1, 100))
    },
    {
        "question": "{}/4 + {}/6",
        "answer": lambda x, y: x/4 + y/6,
        "numbers": lambda: (random.randint(1, 7), random.randint(1, 7))
    },
    {
        "question": "{} * 1/4",
        "answer": lambda x: x * 1/4,
        "numbers": lambda: (random.randint(1, 4),)
    },
    {
        "question": "{} * {}%",
        "answer": lambda x, y: x * (y / 100),
        "numbers": lambda: (random.randint(1, 450), random.randint(1, 100))
    },
    {
        "question": "{} + 1/8",
        "answer": lambda x: x + 1/8,
        "numbers": lambda: (random.randint(1, 5),)
    },
    {
        "question": "Calculate area of a square, Height: {}, Width: {}",
        "answer": lambda x, y: x * y,
        "numbers": lambda: (random.randint(1, 50), random.randint(1, 50))
    },
    {
        "question": "Calculate area of a triangle, Base: {}, Height: {}",
        "answer": lambda x, y: 0.5 * x * y,
        "numbers": lambda: (random.randint(1, 50), random.randint(1, 50))
    },

    {
        "question": "Calculate volume of a cube, Height: {}, Width: {}, Depth: {}",
        "answer": lambda x, y, z: x * y * z,
        "numbers": lambda: (random.randint(1, 10), random.randint(1, 3), random.randint(1, 3))
    },
]


