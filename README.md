# Algorithm Visualizer

Algorithm Visualizer is a web application built with Flask that allows users to visualize various sorting algorithms. Users can select a sorting algorithm from a form and see the sorting process visualized with both numbers and bars, along with the name of the algorithm, its time complexity, and the number of iterations.

## Features

- Visualize different sorting algorithms
- Display algorithm name, time complexity, and number of iterations
- Interactive UI with buttons to start the sorting process
- Responsive design using Bootstrap

## Sorting Algorithms Implemented

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Radix Sort
- Bucket Sort
- Shell Sort
- Bogo Sort

## Technologies Used

- Flask
- HTML
- CSS (Bootstrap)
- JavaScript

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/algorithm-visualizer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd algorithm-visualizer
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:

    ```bash
    python app.py
    ```

7. Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure


- `app.py`: Main Flask application file.
- `templates/`: Folder containing HTML templates.
  - `form.html`: Template for the form to select the sorting algorithm.
  - `index.html`: Template for the sorting visualization.
- `README.md`: Project documentation.


## Usage

1. Open the form by navigating to the root URL (`/`). Select the sorting algorithm you want to visualize and click "Visualize".
2. The application will redirect to the visualization page, where you can see the sorting process.
3. Click the "Start Sorting" button to begin the visualization.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy visualizing sorting algorithms! If you have any questions or feedback, feel free to contact us at your-email@example.com.
