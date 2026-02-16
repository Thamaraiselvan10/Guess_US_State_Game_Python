<div align="center">

  <h1>🇺🇸 U.S. States Game</h1>

  <p>
    <strong>Test your geography knowledge with this interactive U.S. States guessing game!</strong>
  </p>

  <p>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
    </a>
    <img src="https://img.shields.io/badge/Language-Python%203.x-blue" alt="Python Version">
    <img src="https://img.shields.io/badge/Library-Turtle-green" alt="Turtle Graphics">
    <img src="https://img.shields.io/badge/Data-Pandas-orange" alt="Pandas Library">
  </p>

  <p>
    <a href="#about-the-project">About The Project</a> •
    <a href="#key-features">Key Features</a> •
    <a href="#tech-stack">Tech Stack</a> •
    <a href="#getting-started">Getting Started</a> •
    <a href="#usage">Usage</a>
  </p>

  <br>

![Game Demo](demo.gif)

</div>

<br>

## <a name="about-the-project"></a>About The Project

Have you ever wondered how many of the 50 U.S. states you can name from memory? This Python-based game challenges you to recognize and name all 50 states on an interactive map. It's a fun and educational tool to test your geographical knowledge!

The game tracks your progress in real-time and even generates a list of states you missed so you can study and improve your score next time.

---

## <a name="key-features"></a>✨ Key Features

- 🗺️ **Interactive Map**: Watch the map populate with state names as you guess them correctly.
- 📊 **Real-time Score**: Keep track of your progress (e.g., 12/50) directly in the game window title.
- 🧠 **Smart Input**: The game handles casing automatically (e.g., "new york" works just like "New York").
- 📚 **Learn Mode**: Type `Exit` to surrender and automatically generate a `states_to_learn.csv` file with all the states you missed.
- 💾 **Data-Driven**: Efficiently manages state data and coordinates using the `pandas` library.

---

## <a name="tech-stack"></a>🛠️ Tech Stack

This project is built with:

- **[Python](https://www.python.org/)**: The core programming language.
- **[Turtle Graphics](https://docs.python.org/3/library/turtle.html)**: For rendering the map and state labels.
- **[Pandas](https://pandas.pydata.org/)**: For reading CSV data and handling state information.

---

## <a name="getting-started"></a>🚀 Getting Started

Follow these simple steps to get a local copy up and running.

### Prerequisites

You need Python installed on your system. You will also need to install the `pandas` library if you haven't already.

```bash
pip install pandas
```

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Thamaraiselvan10/Guess_US_State_Game_Python.git
    ```
2.  **Navigate to the project directory**
    ```bash
    cd Guess_US_State_Game_Python
    ```

---

## <a name="usage"></a>🎮 Usage

1.  **Run the Game**
    Execute the main script:
    ```bash
    python main.py
    ```

2.  **How to Play**
    - A window will pop up showing a blank map of the U.S.
    - Type a state name in the dialog box and press **Enter**.
    - Correct guesses will appear on the map.
    - To exit and save your missed states for review, type **Exit**.

---

## <a name="license"></a>📜 License

Distributed under the MIT License. See `LICENSE` for more information.
