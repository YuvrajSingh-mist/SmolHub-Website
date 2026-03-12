---
permalink: /
title: "Hi there, I am Yuvraj!"  

author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

- Build and fine-tune LLMs; re-implement classic AI/ML papers from scratch
- Focus areas: Multimodal LLMs (vision, language and audio) and RL for pre/post training paradigms
- Looking for: Research Internship (academia / industrial) positions in my areas of interest. Open to AI Engineer roles for development of pipelines, RAGs, Fine Tuning and other AI/ML related projects
- Community: Mentor newcomers and collaborate on open-source projects

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
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin: 20px 0;">
  {% assign sorted_talks = site.talks | sort: 'date_iso' | reverse %}
  {% for post in sorted_talks %}
    <div style="background: #ffffff; border: 1px solid #e0e0e0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); transition: all 0.3s ease; display: flex; flex-direction: column;">
      <div style="margin-bottom: 12px;">
        <a href="{{ post.url | relative_url }}" style="font-size: 1.1em; font-weight: 700; color: #2c3e50; text-decoration: none; line-height: 1.3;">{{ post.title | split: '|' | first | strip }}</a>
        {% if post.title contains '|' %}
          <div style="color: #666; font-size: 0.9em; margin-top: 4px;">{{ post.title | split: '|' | last | strip }}</div>
        {% endif %}
      </div>
      
      {% assign meta = '' %}
      {% if post.type %}{% assign meta = meta | append: post.type %}{% endif %}
      {% if post.venue %}{% if meta != '' %}{% assign meta = meta | append: ' · ' %}{% endif %}{% assign meta = meta | append: post.venue %}{% endif %}
      {% if post.location %}{% if meta != '' %}{% assign meta = meta | append: ' · ' %}{% endif %}{% assign meta = meta | append: post.location %}{% endif %}
      {% if meta != '' %}<div style="margin-bottom: 12px;"><small style="color: #666;">{{ meta }}</small></div>{% endif %}
      
      {% assign bullets = post.excerpt | strip_html | strip_newlines | replace: '…', '.' | replace: ' .', '.' | replace: '  ', ' ' | split: '.' %}
      {% assign shown = 0 %}
      <ul style="margin: 0 0 16px 0; padding-left: 20px; flex-grow: 1;">
      {% for item in bullets %}
        {% assign trimmed = item | strip %}
        {% if trimmed != '' and shown < 3 %}
          <li style="margin-bottom: 6px; font-size: 0.9em; color: #555;">{{ trimmed }}.</li>
          {% assign shown = shown | plus: 1 %}
        {% endif %}
      {% endfor %}
      </ul>
      
      {% if post.github_url %}
        <div style="margin-top: auto;">
          <a href="{{ post.github_url }}" target="_blank" rel="noopener" style="background: #ffffff; color: #2c3e50; border: 1px solid #d0d0d0; padding: 8px 16px; border-radius: 6px; font-size: 0.85em; font-weight: 500; text-decoration: none; box-shadow: 0 1px 3px rgba(0,0,0,0.08); transition: all 0.2s ease; display: inline-flex; align-items: center; gap: 8px; width: 100%; justify-content: center;">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" style="flex-shrink: 0;"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
            View on GitHub
          </a>
        </div>
      {% endif %}
    </div>
  {% endfor %}
  </div>
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


<!-- ## Skills

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
</div> -->


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
