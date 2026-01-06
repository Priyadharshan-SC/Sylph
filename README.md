# 🌬️ Sylph

> **Sylph** is a lightweight, rule-driven command-line assistant built in Python, designed to map user input to actions through clean logic instead of messy conditionals.

It is a learning-first project — focused on **thinking clearly, structuring well, and building foundations that scale**.

---

## 📖 Overview

Sylph works as a **CLI virtual assistant** that reads user commands, checks them against predefined rules, and executes mapped actions.

The core idea is simple and traditional:

- **Commands are data**
- **Actions are functions**
- **Mapping is explicit**

No deep magic. Just honest logic.

---

## ✨ Key Features

- 🧠 Rule-based command handling  
- 🔁 Command → Action mapping without `if-else` chains  
- 🗂️ Clean separation of concerns  
- 🖥️ Interactive terminal interface  
- 🌱 Easy to extend with new commands  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Interface:** Command Line (CLI)  
- **Storage:** In-memory (current stage)  
- **Version Control:** Git & GitHub  

Old tools. Timeless ideas.

---

## 📂 Project Structure

```text
Task/
├── __pycache__/        # Python cache files
├── action_map.py       # Maps commands to functions
├── actions.py          # Action logic implementations
├── store.py            # Shared data storage (tasks, memory)
├── rules.json          # Command rules and metadata
├── sylph.py            # Main entry point
└── README.md           # Documentation

