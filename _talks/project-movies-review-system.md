---
title: "Movies Review System  | Spoiler-Free Sentiment-Analysis based Movies Review System)"
collection: talks
type: "POC"
permalink: 
excerpt: "Introducing the Movie Review System, where AI meets movie magic to revolutionize how viewers experience films. This project goal is to provide an interface for spoiler-free reviews and sentiment analysis, enhancing the viewing journey. With advanced models like Voting Classifier and Bi-LSTMs powered by Keras and TensorFlow, we achieve impressive metrics—a 91% accuracy, 91% precision, and 90% recall that understands and enhances the users' with the respective movies' plot from a bird's eye view."
venue: "IIIT"
date: September '23
location: "Bhubaneswar"
date_iso: 2023-09-01
github_url: https://github.com/YuvrajSingh-mist/Movie_Review_System
---

<div class="project-links" style="display:flex; gap:10px; flex-wrap:wrap; margin: 8px 0 24px;">
  <a href="https://github.com/YuvrajSingh-mist/Movie_Review_System" target="_blank" rel="noopener" class="model-details-btn" style="background: #ffffff; color: #2c3e50; border: 1px solid #d0d0d0; box-shadow: 0 1px 3px rgba(0,0,0,0.08); padding: 8px 12px; border-radius: 8px; text-decoration: none;">
    🐙 GitHub
  </a>
</div>

# Movie Review System


# Movie Review System

* This project is about a Review System designed specifically for people who like to take a hint about the movie plot and if it's worth to watch it or not through reviews.

* This system provides a surface where they can do so by organising their reviews into spoiler and non-spoiler along with a touch of Sentimntal Analysis-whether a given review is positive or negative.



## Tech Stack

**Backend:** Tensorflow, Keras, scikit-learn, Word2Vec, Pickle,, Render (Deployment)

**Frontend:** Streamlit (Build)

**Other:** Git and Github


## Features

- Segregation of reviews of a movie into Spoiler and Non-Spoiler Reviews
- Sentiment-Analysed Reviews (positive-negative)
- Can access the movie's details (TMDB) for the which the reviews is being searched
- Light/dark mode toggle


## Run Locally

- (REQUIRED) Download Microsoft Edge and it's compatible Selenium driver 

Clone the project

```bash
  git clone [https://github.com/YuvrajSingh-mist/Movie_Review_System.git]
```

Go to the project directory

```bash
  cd Movie_Review_System
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the Web-App

```bash
  streamlit run Home.py
```


## Authors

- [@Yuvraj-Singh](https://www.github.com/YuvrajSingh-mist)








