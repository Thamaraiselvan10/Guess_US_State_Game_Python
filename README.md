# 🇺🇸 U.S. States Game

> **Test your geography knowledge with this interactive U.S. States guessing game!**

Have you ever wondered how many of the 50 U.S. states you can name from memory? This Python-based game challenges you to do just that. Utilizing the `turtle` graphics library for an interactive map and `pandas` for data management, this game provides a fun and educational way to learn U.S. geography.

---

## 🎮 Demo

![Game Demo](./demo.gif)

---

## ✨ Features

- **Interactive Map**: Visualize the U.S. map and watch states populate as you guess them correctly.
- **Real-time Tracking**: Keep track of your score (e.g., 12/50) directly in the game window title.
- **Smart Feedback**: The game ignores casing, so "new york" calculates as "New York".
- **Learn from Mistakes**: Type `Exit` to end the game early and generate a `states_to_learn.csv` file containing all the states you missed, making it easy to study for next time!
- **Data-Driven**: Powered by `pandas` for efficient CSV reading and data manipulation.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have Python installed. You will also need the `pandas` library.

```bash
pip install pandas
```

### 🛠️ Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Thamaraiselvan10/Guess_US_State_Game_Python.git
    cd Guess_US_State_Game_Python
    ```

2.  **Run the Game**
    Execute the main script to start the application:
    ```bash
    python main.py
    ```

3.  **How to Play**
    - A window will appear with a blank map of the U.S.
    - A prompt will ask you to enter a state name.
    - Type a state name and hit **Enter**.
    - If correct, the state name appears on the map.
    - If you want to give up or save your progress for study, type **Exit**.

## 📂 Project Structure

- `main.py`: The main game logic and entry point.
- `50_states.csv`: Data file containing state names and their (x, y) coordinates.
- `blank_states_img.gif`: The background map image.
- `demo.gif`: Gameplay demonstration.
- `states_to_learn.csv`: Generated file containing missed states (created after playing).

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or new feature ideas.

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
