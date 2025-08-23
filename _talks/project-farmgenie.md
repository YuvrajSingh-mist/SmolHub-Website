---
title: "FarmGenie (GeoHack 2024) | Empowering farmers with real-time insights and expert guidance via AI-driven space"
collection: talks
excerpt: "
Our platform utilizes LLMs and a Mixture of Expert (MoE) approaches to provide precise guidance on
soil management, plant disease identification, and irrigation techniques. Built as a scalable web application with a
Next.js frontend and backend, and supported by a Redis queue and multiple worker nodes, FarmGenie ensures
robust performance. The system’s multilingual support, interactive community forum, and up-to-date knowledge
base facilitate seamless, expert-driven assistance for both new and experienced farmers.
"
type: "Hackathon"
permalink: 
venue: "IIIT-BH"
date: July 19 '24
location: Bhubaneswar
---

<div class="project-links" style="display:flex; gap:10px; flex-wrap:wrap; margin: 8px 0 24px;">
  <a href="https://github.com/YuvrajSingh-mist/FarmGenie/tree/main" target="_blank" rel="noopener" class="model-details-btn" style="background: linear-gradient(135deg, #111827, #374151); padding: 8px 12px; border-radius: 8px; color: #fff; text-decoration: none;">
    🐙 GitHub
  </a>
</div>


* **Role**: Backend (AI/ML Integration)

* **Vision/Goal**: In the ever-evolving agricultural landscape, farmers often face challenges in accessing up-to-date knowledge and resources to improve their farming practices. To address this, we have developed a comprehensive product that leverages the power of LLMs as Experts and Agents to create an interactive platform for farmers.

* **Solution**: Our platform utilizes LLMs and a Mixture of Expert (MoE) approaches to provide precise guidance on soil management, plant disease identification, and irrigation techniques. Built as a scalable web application with a Next.js frontend and backend, and supported by a Redis queue and multiple worker nodes, FarmGenie ensures robust performance. The system’s multilingual support, interactive community forum, and up-to-date knowledge base facilitate seamless, expert-driven assistance for both new and experienced farmers

* **Features** :    

- **Seamless Interface**
  - **Website**:
  - Built with Next.js for both client and backend
  - Uses Redis queue and multiple worker nodes for scalability

- **Dual Marketplace**
  - **Input Marketplace**: For local sellers and dealers
  - **Output Marketplace**: For farmers

- **Conversational AI Framework**
  - **Core Technologies**: Mixture of Experts (MoE), Retrieval-Augmented Generation (RAG), and language translation
  - **MoE Component**: Three fine-tuned small language models for soil management, plant disease identification, and irrigation
  - **Conversation Management**: LLMs handle query classification, conversation flow, and language translation

- **Community Forum**
  - **Website**:
  - Facilitates knowledge sharing and peer learning

- **Marketplace-Chatbot Framework**
  - **Technology**: Combines Gemini and OpenAI GPT-4o
  - **Function**: Replaces traditional search with natural language instructions, enhancing user interaction with local retail shops

- **Agricultural Schemes Platform**
  - **Website**: 
  - **Features**: Comprehensive database of government schemes, user-friendly interface, regular updates, and informative guides

- **Technical Architecture**
  - **Frontend**: Next.js with server-side rendering and static site generation
  - **Backend**: Next.js, handling request processing through Redis queue and multiple worker nodes
  - **Database**: PostgreSQL (Neon DB) for storing user, farmer, and retailer data
  - **Deployment**: Docker containers for consistent deployment
  - **Scalability**: Managed via Redis queue and worker nodes
  - **Security**: SSL/TLS encryption, user authentication, and input validation

* **Tools**: 

**Client:** |  Tailwind CSS, TypeScript, Next.js

**Backend:** | Flask, Python, Langchain, GeminiPro API, peft , bitsandbytes, transformers

**Storage/VectoStore:** | PostgreSQL, FAISS, Pinecone, MySQL

**Other Tools:** | Unsloth, GCP, Docker, Vercel, DigitalOcean


[**Project Link**](https://github.com/YuvrajSingh-mist/FarmGenie/tree/main)
