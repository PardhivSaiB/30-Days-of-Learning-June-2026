# Day 01 – Building a Local AI Agent (Ollama + Python)

## 🚀 Project Idea

This project is a **local AI agent built from scratch** using Python and Ollama. The goal was to understand how modern AI agents work under the hood instead of just using high-level tools or APIs.

The agent connects a local LLM (Qwen3) with simple tools like:

* A calculator
* A file reader

This creates a basic but real **tool-using AI system**.

---

## 🧠 What I Built

A terminal-based AI agent that can:

* Chat using a local LLM (Qwen3 via Ollama)
* Perform calculations using a Python tool
* Read local text files
* Route user requests using simple logic

---

## 🛠️ Tech Stack

* Python
* Ollama (local LLM runtime)
* Qwen3 model
* Git & GitHub

---

## ⚙️ How It Works

The system follows this flow:

User → Python Agent → Tool (if needed) → Ollama (Qwen3) → Response

Two tools were implemented:

* `calc` → evaluates mathematical expressions
* `read` → reads local files

If no tool is needed, the request goes directly to the LLM.

---

## 🧩 Key Learnings

* How local LLMs run on a machine using Ollama
* How AI agents are just **LLMs + tools + control logic**
* How Python acts as an orchestrator between tools and the model
* How real AI systems are structured in layers

---

## ❌ Mistakes I Made

### 1. Git Confusion (Main Issue)

Initially, I created multiple folders and committed from the wrong directory.

👉 Problem:

* Repo was nested incorrectly
* GitHub didn’t show expected structure

👉 Fix:

* Learned correct repo hierarchy
* Used `git status`, `git add`, `git push` properly
* Understood how Git tracks directories

---

### 2. Missing Git Push

I committed locally but didn’t push to GitHub.

👉 Problem:

* Changes were not visible on GitHub

👉 Fix:

* Used `git push origin main`
* Learned difference between commit vs push

---

### 3. Python Indentation Bug

A small indentation error broke tool routing logic.

👉 Problem:

* File tool never triggered correctly

👉 Fix:

* Understood Python’s indentation-based structure
* Fixed control flow inside the loop

---

### 4. Model Response Confusion

At first, the model tried to answer file-related queries without using tools.

👉 Problem:

* No true tool invocation

👉 Fix:

* Added explicit routing logic in Python

---

## 💡 What I Learned About AI Agents

A real AI agent is not magic.

It is simply:

* A language model (brain)
* Tools (actions)
* A controller (Python logic)

The “intelligence” comes from how these parts are connected.

---

## 📈 What’s Next

* Add automatic tool selection (no manual `calc` / `read`)
* Add memory (agent remembers past interactions)
* Add document understanding (PDFs, larger files)
* Build multi-agent systems

---

## 🔥 Final Thought

This project was not about building a perfect agent.

It was about understanding:

> “How does an AI system actually think, decide, and act?”

And the answer is:
It doesn’t think — it executes a structured loop of reasoning + tools.

---
