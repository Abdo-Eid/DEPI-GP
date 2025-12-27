## main Data Files Summary

### 1. **egy_agri_topics_final_sorted.jsonl**

**Schema (one record per line):**

```jsonl
{
    "id": "topic_0001",
    "topic": "مرض البياض الدقيقي",
    "subtopic": "أمراض فطرية",
    "text": "البياض الدقيقي مرض فطري يصيب الأوراق وينتج عنه بقع بيضاء مطوية..."
}
```

* **Use:** Final list of agricultural topics + rich answer text, generated from `egy_agri_topics.json` using an LLM (tone/style configurable). Used in the finetuning by making input/prompt templates like: `("اشرحلي" أو "ما هي" أو "يعني اي") + topic + subtopic` and output/response is `text`.

### 2. **videos_data-annotated.jsonl**

**Schema (one record per line):**

```jsonl
{
    "video_id": "dQw4w9xx",
    "title": "كيفية زراعة البصل من البذور",
    "channel": "بالمختصر المفيد",
    "published_at": "20230601",
    "description": "شرح خطوات تحضير التربة وزراعة البصل...",
    "transcript": "...full transcript text...",
    "word_count": 3240,
    "annotation": {
        "summary": "يوضح الفيديو مراحل زراعة البصل من البذور بدءًا من تجهيز التربة وتحسينها، ثم طريقة الزراعة الصحيحة، وأهم خطوات الري والتسميد والمتابعة حتى مرحلة النمو، مع التركيز على العناية المستمرة لضمان إنتاج جيد.",
        "conversation": [
            {
                "role": "user",
                "content": "متى أزرع البصل من البذور؟"
            },
            {
                "role": "assistant",
                "content": "أفضل وقت لزراعة البصل يكون في الربيع بعد زوال الصقيع، أو حسب منطقتك المناخية، المهم أن تكون درجات الحرارة مستقرة والتربة صالحة للإنبات."
            }
        ]
    }
}
```

* **Use:** Cleaned & annotated video records for conversational fine-tuning, transforming transcripts into structured dialogue (user/assistant turns) with aligned summaries for training.

### 3. **wiki_QA_responses.jsonl**

**Schema (one record per line):**

```jsonl
{
    "article_id": "8773527",
    "chunk_id": 3,
    "question": "ما هو آلية عمل إي بي إن؟",
    "chunk_text": "...نص فقرة من المقال تشرح الآلية...",
    "response": "يُثبط إي بي إن إنزيم الأستيل كولين استراز مما يؤدي إلى تراكم الأستيل كولين..."
}
```

* **Size:** 500 QA pairs the pipeline didn't fully walk on all Wikipedia chunks for API restrictions
* **Use:** Sentence/chunk-level QA pairs for fine-tuning (Arabic)

## rag dataset (unique for e-commercea and not used for finetuning)

### 1. **agricash_rag_dataset.jsonl**

**Schema (one record per line):**

```jsonl
{
    "id": 7759,
    "name": "نيو روش كيلر",
    "url": "https://agricash.app/product/new-rouch-killer/",
    "in_stock": true,
    "category_hierarchy": [{"name": "مستلزمات الإنتاج النباتي", "parent": 0...}],
    "price": "55",
    "short_description": "نيو روش كيلر...",
    "description": "يستخدم لمكافحة الحشرات الزاحفة...",
    "combined_description": "نيو روش كيلر\nيستخدم لمكافحة الحشرات الزاحفة",
    "category_text": "مستلزمات الإنتاج النباتي > المبيدات > مبيدات الصحة العامة",
    "rag_context_text": "اسم المنتج: نيو روش كيلر\nالتصنيف: مستلزمات الإنتاج النباتي > المبيدات > مبيدات الصحة العامة\nالسعر: 55 جنيه\nالحالة: متاح\nالوصف:\nنيو روش كيلر\nيستخدم لمكافحة الحشرات الزاحفة"
}
```

* **Size:** 553 records (Full Catalog)
* **Record Count:** 553 products
* **Fields:** id, name, url, in_stock, category_hierarchy, price, short_description, description, combined_description, category_text, rag_context_text
* **Features:**

  * **Contextual Hierarchy:** Full parent-child category paths mapped for every item.
  * **Cleaned HTML:** Descriptions stripped of tags for better embedding.
  * **Localized RAG Block:** A dedicated `rag_context_text` field formatted in Egyptian Arabic specifically for LLM ingestion.
  * **Inventory Aware:** Includes live stock status.
* **Use:** E-commerce agent inventory, product recommendations, and price queries.

---

## Data Collection Methodology

### Sources

1. **Wikipedia (Arabic Edition)**

   * Articles on agriculture, farming, and botany
   * Structured, encyclopedic content
   * High quality, verified information

2. **YouTube Agricultural Channels**

   * Channel: "بالمختصر المفيد" (Condensed Useful Information)
   * Creator: Mesad Nassar
   * Focus: Practical, accessible agriculture guidance in colloquial Arabic

3. **Agricultural Websites**

   * Professional farming guides and documentation
   * Technical specifications and best practices
   * Crop-specific cultivation guidelines

4. **AgriCash E-commerce Store (API)**

   * Source: `https://agricash.app/wp-json/wc/store/v1/products`
   * Method: Advanced API traversal with category mapping
   * Focus: Real-time product inventory, pricing, and hierarchical classification

---

## Data Characteristics

### Content Diversity

### Coverage Areas

1. **Crops:** Grains, vegetables, fruits, herbs
2. **Techniques:** Planting, irrigation, fertilization, harvesting
3. **Pest Management:** Identification, organic control, pesticides
4. **Equipment:** Agricultural machinery and tools
5. **Soil Management:** Preparation, amendments, testing
6. **Seasonal Considerations:** Winter, spring, summer operations
7. **Marketplace:** Live inventory of fertilizers, pesticides, seeds, and solar systems

## Project Context

This data collection supports the DEPI-GP project's goal to create an **Arabic-Language Agricultural Assistant for an E-commerce Site**. The collected data enables:

* Intelligent product recommendations (Linking problems found in Wikipedia/YouTube to solutions in the Shop)
* Educational content delivery
* Farmer guidance and support
* Market-aware agricultural suggestions
* Community-based knowledge sharing
* Direct Sales: Converting advice ("You have aphids") into transactions ("Here is `Malathion 57%` for 150 EGP, available now").

---

## Intermediate Data (Raw Collection → Processing Artifacts)

**Purpose:** These files represent the **raw collected data and intermediate processing outputs** used to generate the **final datasets for conversational fine-tuning**. They are not directly used as training data (unless explicitly noted), but they are essential for creating the final structured conversations, summaries, and QA pairs.

## Intermediate Files

### `video_urls.txt`

* **Type:** Plain text
* **Contains:** Raw list of scraped YouTube URLs
* **Output Produced:** `videos_data.jsonl`

### `videos_data.jsonl`

* **Type:** JSONL (one video per line)
* **Contains:** Raw scraped video records (video_id, title, channel, transcript, etc.)
* **Next Step:** Cleaned + enriched into `videos_data-annotated.jsonl`
  *(summary + structured conversation pairs for fine-tuning)*

### `agriculture_categories_ar.json`

* **Type:** JSON
* **Contains:** Intermediate Arabic category taxonomy for getting related pages to agriculture topics
* **Used For:** Generating `agriculture_pages_optimized.json`

### `agriculture_pages_optimized.json`

* **Type:** JSON
* **Contains:** Intermediate cleaned page drafts (HTML → text cleanups + canonicalization)
* **Output Produced:** `Final_agriculture_pages_ar.jsonl`

### `egy_agri_topics.json`

* **Type:** JSONL/JSON (raw topics list)
* **Contains:** Raw agricultural topics (topic + subtopic) used as input to topic text generation
* **Output Produced:** `egy_agri_topics_final_sorted.jsonl` (after LLM-generated `text` + sorting)
* **Generation Prompt:** Uses an LLM system prompt to generate long, detailed Arabic text with an Egyptian tone based on (topic, subtopic)

## Processing Notes (How These Fit Together)

* `video_urls.txt` → video scraper → `videos_data.jsonl`
* `videos_data.jsonl` → cleaning + (LLM/manual) annotation → `videos_data-annotated.jsonl` *(fine-tuning-ready)*
* `agriculture_categories_ar.json` → category mapping (used during optimization) → `agriculture_pages_optimized.json`
* `agriculture_pages_optimized.json` → text normalization → `Final_agriculture_pages_ar.jsonl`
* `Final_agriculture_pages_ar.jsonl` / Wikipedia chunks → QA generation → `wiki_QA_responses.jsonl` *(fine-tuning-ready)*
* `egy_agri_topics.json` → LLM long-text generation (SYS_PROMPT tone/style configurable) → `egy_agri_topics_final_sorted.jsonl` *(fine-tuning-ready with template way)*
