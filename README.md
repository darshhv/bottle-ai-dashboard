# AI-Based Bottle Feature Detection Dashboard

This project is a web-based AI-integrated dashboard designed to extract and analyze morphological and aesthetic features of bottles using edge detection and image processing techniques.

Built as part of a research internship at IISc, the system allows users to upload images of bottles, extract key design features (e.g., cap, neck, holder, curvature), and interact with a visual dashboard powered by Flask and OpenCV.

## 🔍 Features
- Upload and analyze bottle images
- Perform edge detection to extract morphological traits
- Compare features across different bottle types
- Analyze form factors such as comfort, grip, and design usability
- Web dashboard UI for interactive visual exploration

## 📁 Project Structure
```
/app
├── main.py                 # App entry point
├── routes.py               # Flask routes and views
├── static/                 # Static assets (CSS, JS)
└── templates/              # HTML templates

/models
└── feature_extractor.py    # Core image processing logic (OpenCV, edge detection)

/utils
└── helper_functions.py     # Utility and support functions

README.md
requirements.txt
```

## 🧠 Tech Stack
- Python
- Flask (Web server)
- OpenCV, scikit-image (Image processing)
- HTML/CSS/JS (Frontend)
- Bootstrap (Optional styling)

## 🚀 Getting Started

1. Clone the repo  
```bash
git clone https://github.com/yourusername/bottle-feature-dashboard.git
cd bottle-feature-dashboard
```

2. Install dependencies  
```bash
pip install -r requirements.txt
```

3. Run the app  
```bash
python app/main.py
```

4. Open your browser and go to `http://localhost:5000`

## 🎯 Use Case
This project is useful for industrial product designers and researchers analyzing bottle ergonomics, aesthetics, and usability. It could also be extended to automated quality checks on packaging lines.

## 🧠 What I Learned
- Structuring a full-stack Python Flask app from scratch
- Applying edge detection (Canny, Sobel) to extract image features
- Managing user interactions through a clean web interface
- Organizing modular code with reusable utilities and models
- Collaborating with research mentors to build real-world AI solutions

## 🌐 Live Demo (Optional)
If deployed, link it here.

## 🤝 Contributing
Pull requests are welcome. Feel free to open issues for suggestions and improvements.

## 📄 License
MIT
