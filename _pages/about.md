---
permalink: /
title: "Hi there, I am Yuvraj!"  

author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

- Everything transformers!; love to re-implement classic and seminal AI/ML papers from in a clean, beginner-friendly manner. 
- Focus areas: Distributed Systems for large scale training/inference alongwith RL for pre/post training paradigms
- Looking for: Research (academia / industrial) positions in my areas of interest.
- Community: Mentor newcomers and collaborate on open-source projects. Built educational libraries demystifying core AI/ML concepts for all people.

## Professional Experience

<div class="experience-list">
  <ul>
    <li>
      <strong>alphaXiv — Research Intern</strong> <small>· Oct 2025 – April 2026</small>
      <ul>
        <li>Reimplemented and reproduced results from seminal and recent ML papers (e.g., Attention Is Not All You Need, TRM/HRM) from scratch in PyTorch under the <a href="https://github.com/alphaXiv/paper-implementations/tree/raj-es" target="_blank">alphaXiv paper-implementations repository</a>.</li>
        <li>Co-authored an article on applying <a href="https://www.alphaxiv.org/blog/es-for-fine-tuning-llms" target="_blank">Evolutionary Strategies for fine-tuning LLMs</a>.</li>
        <li>Built evaluation pipelines and benchmarking infrastructure for LLM/VLM systems; evaluated models such as DeepSeek-OCR and OlmOCR2 on OmniDocBench and related OCR benchmarks.</li>
        <li>Deployed large models (e.g., DeepSeek-OCR, OCR2, LLMs like Ouro) using vLLM and Modal/Baseten, and generated a 100k-document OCR dataset from arXiv PDFs for large-scale document understanding research.</li>
      </ul>
    </li>
    <li>
      <strong>IISER, Kolkata — Summer Research Intern</strong> <small>· May 2024 – May 2025</small>
      <ul>
        <li>Co-authored (first author) with Prof. Kripabandhu Ghosh, for creating a dataset of 40k scraped YouTube comments, humanely-verified, stance-analysed famous sports controversies (cricket and football) with applied stance detection.</li>
        <li>Utilized LLMs like Llama-3.1/3.2, Mistral-7b, Qwen-2.5 under zero/few-shot prompt to create the dataset. Benchmarked and fine-tuned existing open-sourced LLMs Reasoning (distilled) and Non-Reasoning LLMs on the humanely verified dataset. Submitted to COLM 2025.</li>
      </ul>
    </li>
    <li>
      <strong>University of Maryland — Research Intern</strong> <small>· Dec 2024 – Feb 2025</small>
      <ul>
        <li>Worked on UI/UX2Code generation with primary focus on creation of a robust dataset for the VLM models to be fine-tuned upon.</li>
        <li>Scraped 100+ websites of static web pages and collected their commit history and corresponding webpage layouts to create a dataset of 200+ records.</li>
      </ul>
    </li>

  </ul>
</div>


## Projects

{% assign sorted_talks = site.projects | sort: 'date_iso' | reverse %}
{% assign sorted_by_stars = sorted_talks | sort: 'stars' | reverse %}
<ul class="content-list">
{% for post in sorted_by_stars %}
  <li class="list-item" data-slug="{{ post.title | split: '|' | first | strip | slugify }}">
    <div class="list-item__body">
      <div class="list-item__title">
        <a href="{{ post.website_url | default: post.url | relative_url }}" class="model-card__title">{{ post.title | split: '|' | first | strip }}</a>
        {% if post.type %}<span class="list-item__tag">{{ post.type }}</span>{% endif %}
      </div>
      {% if post.excerpt %}
      <div class="list-item__excerpt">{{ post.excerpt | strip_html | truncatewords: 22 }}</div>
      {% elsif post.title contains '|' %}
      <div class="list-item__excerpt">{{ post.title | split: '|' | last | strip }}</div>
      {% endif %}
      {% if post.github_url %}
      <div class="list-item__actions">
        <a href="{{ post.github_url }}" target="_blank" rel="noopener"><i class="fab fa-github"></i> GitHub</a>
      </div>
      {% endif %}
    </div>
    <div class="list-item__metrics">
      {% if post.stars %}
      <div class="metric">
        <span class="metric-icon">★</span>
        <span class="metric-count">{{ post.stars }}</span>
      </div>
      {% endif %}
      <div class="metric">
        <span class="metric-icon">◉</span>
        <span class="metric-count views-counter">—</span>
      </div>
    </div>
  </li>
{% endfor %}
</ul>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var els = document.querySelectorAll('.views-counter');
  var slugs = [];
  els.forEach(function(el) {
    var s = el.closest('.list-item') && el.closest('.list-item').dataset.slug;
    if (s) slugs.push(s);
  });
  if (!slugs.length) return;
  fetch('/api/views?slugs=' + slugs.map(encodeURIComponent).join(','))
    .then(function(r) { return r.json(); })
    .then(function(data) {
      els.forEach(function(el) {
        var s = el.closest('.list-item') && el.closest('.list-item').dataset.slug;
        if (s && data[s] != null) el.textContent = Number(data[s]).toLocaleString();
      });
    })
    .catch(function() {});
});
</script>


## Education

<div class="education-list">
  <ul>
    <li>
      <strong>International Institute of Information Technology, Bhubaneswar</strong> <small>· 2023–2027</small>
      <ul>
        <li>BTech, Computer Science Engineering</li>
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
