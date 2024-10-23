# Rufus: Intelligent Web Data Extraction for RAG Systems

Rufus is an AI-powered tool designed to intelligently crawl websites based on user-defined prompts, extract valuable data, and synthesize it into structured documents ready for use in Retrieval-Augmented Generation (RAG) pipelines. The goal is to streamline the process of preparing web data for downstream use with large language models (LLMs).

## Features

- **Intelligent Web Crawling**: Rufus can handle complex web structures, including nested links and dynamically loaded content.
- **Selective Scraping**: Only extract relevant content based on the user’s prompts.
- **Content Synthesis**: Data is converted into structured formats like JSON or plain text, ready for RAG pipelines.
- **Flexible API**: Simple and intuitive API for easy integration into RAG systems.

## Installation

To install Rufus, first clone the repository:

```bash
git clone https://github.com/niranj-patel/Rufus-web-data-extraction-llm.git
cd rufus
conda create -p env python=3.12.0 -y
source activate ./env
pip install -r requirements.txt
