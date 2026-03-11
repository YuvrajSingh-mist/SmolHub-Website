---
permalink: /
title: "Hi there, I am Yuvraj!"  

author_profile: true
redirect_from: 
  - /about/
  - /about.html
---



• Build and fine-tune LLMs; re-implement classic AI/ML papers from scratch
• Focus areas: Multimodal LLMs (vision, language and audio) and RL for pre/post treaining paradigms.
• Looking for: Research Internship (academia / industrial) positions in my areas of interest. Open to AI Engineer roles for development of pipelines, RAGs, Fine Tuning and other AI/ML related projects.
• Community: Mentor newcomers and collaborate on open‑source projects


## Professional Experience

<div class="experience-list">
  <ul>
      <li>
      <strong>TurboML— AI Engineer</strong> <small>· May 2025 – June 2025</small>
      <ul>
        <li>Worked on development of various tools for LLM, enhancing tool-calling capabilities.</li>
        <li>Developed pipeline for smooth integration of tools developed for YouTube QnA, summarization of videos and fact check features with the platform.</li>
      </ul>
    </li>
    <li>
      <strong>University of Maryland — Research Intern</strong> <small>· Dec 2024 – Feb 2025</small>
      <ul>
        <li>UI/UX→Code dataset creation for VLM fine‑tuning</li>
        <li>Scraped 100+ static sites; curated 200+ layout/commit records</li>
      </ul>
    </li>
    <li>
      <strong>IISER Kolkata — Summer Research Intern</strong> <small>· May 2024 – May 2025</small>
      <ul>
        <li>Built 40k human‑verified stance‑analysis dataset (sports controversies)</li>
        <li>Labels via Llama‑3.1/3.2, Mistral‑7B, Qwen‑2.5 with human verification</li>
        <li>Fine‑tuned reasoning and non‑reasoning LLMs; ~30% improvement</li>
      </ul>
    </li>
    <li>
      <strong>AIISC — Research Intern</strong> <small>· Mar 2024 – Jul 2024</small>
      <ul>
        <li>Worked with Prof. Amitava Das on hallucination prevention</li>
        <li>Web‑scraped news/posts; generated synthetic data with open‑source LLMs</li>
        <li>Entity tagging using GLiNER and related models</li>
      </ul>
    </li>
    <li>
      <strong>Clinical AI Assistance — Research Intern</strong> <small>· Dec 2023 – Mar 2024</small>
      <ul>
        <li>Dataset creation and model evaluation with HuggingFace‑hosted LLMs</li>
        <li>Data gathering, cleaning, and efficiency analysis</li>
      </ul>
    </li>
  </ul>
</div>


## Projects

<div class="projects-list">
  <ul>
  {% assign sorted_projects = site.talks | sort: 'date_iso' | reverse %}
  {% for post in sorted_projects %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      {% assign meta = '' %}
      {% if post.type %}{% assign meta = meta | append: post.type %}{% endif %}
      {% if post.venue %}{% if meta != '' %}{% assign meta = meta | append: ' · ' %}{% endif %}{% assign meta = meta | append: post.venue %}{% endif %}
      {% if post.location %}{% if meta != '' %}{% assign meta = meta | append: ' · ' %}{% endif %}{% assign meta = meta | append: post.location %}{% endif %}
      {% if post.date %}{% if meta != '' %}{% assign meta = meta | append: ' · ' %}{% endif %}{% assign meta = meta | append: post.date %}{% endif %}
      {% if meta != '' %}<br/><small>{{ meta }}</small>{% endif %}
      {% assign bullets = post.excerpt | strip_html | strip_newlines | replace: '…', '.' | replace: ' .', '.' | replace: '  ', ' ' | split: '.' %}
      {% assign shown = 0 %}
      <ul>
      {% for item in bullets %}
        {% assign trimmed = item | strip %}
        {% if trimmed != '' and shown < 4 %}
          <li>{{ trimmed }}.</li>
          {% assign shown = shown | plus: 1 %}
        {% endif %}
      {% endfor %}
      </ul>
    </li>
  {% endfor %}
  </ul>
</div>


## Education

<div class="education-list">
  <ul>
    <li>
      <strong>International Institute of Information Technology, Bhubaneswar</strong> <small>· 2023–2027</small>
      <ul>
        <li>BTech, Computer Science Engineering</li>
      </ul>
    </li>
    <li>
      <strong>Delhi Public School</strong> <small>· 2022–2023</small>
      <ul>
        <li>CBSE Grade 12 — 91%</li>
      </ul>
    </li>
    <li>
      <strong>Amity International School</strong> <small>· 2021–2022</small>
      <ul>
        <li>CBSE Grade 10 — 96%</li>
      </ul>
    </li>
  </ul>
</div>


## Skills

<div class="skills-list">
  <ul>
    <li>
      <strong>Languages</strong>
      <div class="skill-chips">
        <span class="chip">Python</span>
      </div>
    </li>
    <li>
      <strong>Frameworks</strong>
      <div class="skill-chips">
        <span class="chip">PyTorch</span>
        <span class="chip">Keras</span>
        <span class="chip">Flutter</span>
        <span class="chip">Flask</span>
      </div>
    </li>
    <li>
      <strong>GenAI Tools</strong>
      <div class="skill-chips">
        <span class="chip">LangChain</span>
        <span class="chip">LlamaIndex</span>
        <span class="chip">ChromaDB</span>
        <span class="chip">Pinecone</span>
        <span class="chip">FAISS</span>
        <span class="chip">HuggingFace</span>
      </div>
    </li>
    <li>
      <strong>NLP</strong>
      <div class="skill-chips">
        <span class="chip">GRU</span>
        <span class="chip">RNN</span>
        <span class="chip">LSTM</span>
        <span class="chip">Attention</span>
        <span class="chip">Transformers</span>
        <span class="chip">LLMs</span>
      </div>
    </li>
    <li>
      <strong>Computer Vision</strong>
      <div class="skill-chips">
        <span class="chip">CNN</span>
        <span class="chip">OpenCV</span>
        <span class="chip">YOLOv8</span>
        <span class="chip">GANs</span>
        <span class="chip">Vision‑Language Models</span>
        <span class="chip">Vision Transformers (ViTs)</span>
      </div>
    </li>
    <li>
      <strong>Tools & Platforms</strong>
      <div class="skill-chips">
        <span class="chip">Streamlit</span>
        <span class="chip">Git</span>
        <span class="chip">GitHub</span>
        <span class="chip">Firebase</span>
        <span class="chip">Docker</span>
        <span class="chip">Google Cloud Platform</span>
      </div>
    </li>
  </ul>
</div>


## Achievements

<div class="achievements-list">
  <ul>
    <li>
      <span class="achv-title">GeoHack '24 Finale — 2nd place</span>
      <small>Project: FarmGenie · IEEE GRSS Kolkata and SAADRI · 2024</small>
    </li>
    <li>
      <span class="achv-title">YESIST12 '24 (Special Track) — Finalist</span>
      <small>Project: PlogPayouts · Led the project · 2024</small>
    </li>
    <li>
      <span class="achv-title">Geek‑o‑thon (D3 @ IIIT‑BH) — Winner</span><br/>
      <small>Project: MovieMania · Inter‑college hackathon (AI/ML) · 2023</small>
    </li>
  </ul>
</div>


<!-- A data-driven personal website
======
Like many other Jekyll-based GitHub Pages templates, Academic Pages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
