# 🧵 Concurrency Assignment – Python Multithreaded Programming

This repository contains solutions for three multithreaded programming tasks in Python, demonstrating the performance benefits of concurrency using the `threading` module.

---

## 📁 Contents

- `merge_sort_threaded.py` – Multithreaded Merge Sort
- `quicksort_threaded.py` – Multithreaded Quick Sort
- `concurrent_downloader.py` – Concurrent File Downloader
- `urls.txt` – Sample list of file URLs for downloading
- `README.md` – Documentation for setup and usage

---

## 🚀 Task Descriptions

### 1. Multi-threaded Merge Sort

A recursive merge sort that runs left and right half-sorts in parallel threads. Execution time is compared against a standard single-threaded version.

### 2. Multi-threaded Quick Sort

Implements quicksort using multithreading for sub-array sorting. Thread usage is capped using a global thread counter to prevent overload.

### 3. Concurrent File Downloader

Downloads a list of files using either:
- Sequential downloading (one at a time)
- Concurrent downloading (multiple threads)

Execution time is reported for both strategies.

---

## 🛠️ How to Run

Make sure you have Python 3 and `requests` installed:

```bash
pip install requests
