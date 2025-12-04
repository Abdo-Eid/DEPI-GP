**Project Documentation — Notebooks & Scripts (Sequential Summary)**

This document records what we have implemented so far in `notebooks-scripts/` and explains the purpose of each file in plain, non-technical language.

-   **`01.MT_en2ar-agriset.ipynb`**: Translation notebook — translates an English agriculture QA dataset into Arabic and prepares a paired dataset for training. Innovation: batched translation with error checks and a path to upload the result to Hugging Face.

-   **`02.1.wiki_scraper.ipynb`**: Wikipedia category walker — explores Arabic Wikipedia agriculture categories and lists pages to collect. Short: gathers candidate article titles for scraping.

-   **`02.2.wiki_scraper_optimized.ipynb`**: Optimized scraper — expands on the previous notebook with better category recursion and filters; saves a cleaned list of pages (`agriculture_pages_optimized.json`). Finding: seed categories and a depth-limited crawl produce a focused list of agriculture pages for our dataset.

-   **`02.3.filter2_pages.ipynb`**: Page downloader & cleaner — downloads each listed Wikipedia page, cleans wiki markup and references, filters out short/noisy pages and writes the cleaned articles to `Final_agriculture_pages_ar.jsonl`. Note: implements content trimming (remove references/sections) to improve quality.

-   **`03.1.channel_video_urls.py`**: YouTube URL extractor — uses `yt-dlp` to collect all video URLs from a channel's /videos page without API keys. Purpose: produce `video_urls.txt` as input for transcript extraction.

-   **`03.2.YT_transicript.ipynb`**: YouTube transcript pipeline — downloads Arabic transcripts (auto or uploaded) for a list of video URLs, cleans text, computes word counts, and writes `videos_data.jsonl`. Innovation: prefers `json3` subtitle format and handles gzip/retries for robustness.

-   **`04.scrape_plant_right.ipynb`**: Plant guide scraper — scrapes crop guides from the Plant-Right (AgriCash) site, converts HTML to Markdown, removes images, and stores crop-specific markdown records in `plant_right.jsonl`. (this data not because it's for the company it's just well written so it's good data)

-   **`05.agricash_shop_scrape_rag.ipynb`**: Shop API to RAG pipeline — connects to the AgriCash WooCommerce Store API, downloads products, builds a category-hierarchy map, cleans descriptions, and prepares `agricash_rag_dataset.jsonl` with `rag_context_text` fields for each product. Finding: using the Store API (instead of HTML scraping) is more robust and returns rich structured data for RAG. (this data is unique to every company, the project itself is related to a domanin "agriculture" but this data and the way you get it is different and not used in every place)

---

How this ties to the proposal:

-   **Done:** Data extraction and cleaning (Wikipedia articles, product catalog RAG context, plant guides, and video transcripts) — these are saved under `raw_outputs/` and exported JSONL files.
-   **Planned next:** Generate embeddings for product and document texts, ingest vectors into a vector DB (e.g., PGVector), build an intent detector, and fine-tune or instruct‑tune an Arabic LLM to answer user queries using the RAG context.

