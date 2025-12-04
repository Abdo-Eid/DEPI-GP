## Data Files Summary

### 1. **Final_agriculture_pages_ar.jsonl**

**Schema (one record per line):**

```jsonl
{
    "article_id": "8773527",
    "title": "O-إيثيل O-(4-نتروفينيل) فينيل فوسفونوثيوات",
    "url": "https://ar.wikipedia.org/wiki/...",
    "summary": "مبيد حشري ينتمي إلى فئة الفوسفونوثيوات...",
    "full_text": "O-إيثيل O-(4-نتروفينيل) فينيل الفوسفونوثيوات والذي يُعرف اختصارًا باسم إي بي إن...",
    "word_count": 976
}
```

-   **Size:** 1,288 lines
-   **Record Count:** 1,288 articles
-   **Fields:** article_id, title, url, summary, full_text, word_count
-   **Use:** Complete knowledge base for model training


### 2. **plant_right.jsonl**

**Schema (one record per line):**

```jsonl
{
    "plant_name": "الذرة الشامية والرفعية",
    "source_url": "https://agricash.app/corn-and-sorghum/",
    "markdown_content": "# الذرة الشامية والرفعية\nمحصول غذائي وصناعي...\n## أهم المعاملات الزراعية..."
}
```

-   **Size:** 5+ crop guides
-   **Record Count:** 5 documented crops
-   **Fields:** plant_name, source_url, markdown_content
-   **Content:** Structured markdown guides with:
    -   Land preparation
    -   Seed specifications
    -   Planting methods & timing
    -   Fertilizer schedules
    -   Irrigation guidelines
    -   Pest/disease control
    -   Harvesting procedures
-   **Use:** Practical farmer guidance

### 3. **videos_data.jsonl**

**Schema (one record per line):**

```jsonl
{
    "video_id": "OkstHpVvqPA",
    "title": "زرعة الكسلان @youtubecreators #YuoTubeHighFive",
    "channel": "بالمختصر المفيد - مسعد نصار",
    "published_at": "20251128",
    "description": "",
    "transcript": "اسهل زرعه ممكن تزرعها عندك هي طبعا التين الشوكي...",
    "word_count": 308
}
```

-   **Size:** 51 records
-   **Record Count:** 51 YouTube videos
-   **Fields:** video_id, title, channel, published_at, description, transcript, word_count
-   **Transcript Length:** 300+ to 6,000+ words per video
-   **Topics:** Home gardening, pest control, organic fertilizers, propagation, climate protection
-   **Use:** Conversational training data

### 4. **agricash_rag_dataset.jsonl**

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

-   **Size:** 553 records (Full Catalog)
-   **Record Count:** 553 products
-   **Fields:** id, name, url, in_stock, category_hierarchy, price, short_description, description, combined_description, category_text, rag_context_text
-   **Features:**
    -   **Contextual Hierarchy:** Full parent-child category paths mapped for every item.
    -   **Cleaned HTML:** Descriptions stripped of tags for better embedding.
    -   **Localized RAG Block:** A dedicated `rag_context_text` field formatted in Egyptian Arabic specifically for LLM ingestion.
    -   **Inventory Aware:** Includes live stock status.
-   **Use:** E-commerce agent inventory, product recommendations, and price queries.

---

## Data Collection Methodology

### Sources

1. **Wikipedia (Arabic Edition)**

    - Articles on agriculture, farming, and botany
    - Structured, encyclopedic content
    - High quality, verified information

2. **YouTube Agricultural Channels**

    - Channel: "بالمختصر المفيد" (Condensed Useful Information)
    - Creator: Mesad Nassar
    - Focus: Practical, accessible agriculture guidance in colloquial Arabic

3. **Agricultural Websites**
    - Professional farming guides and documentation
    - Technical specifications and best practices
    - Crop-specific cultivation guidelines

4. **AgriCash E-commerce Store (API)**
    - Source: `https://agricash.app/wp-json/wc/store/v1/products`
    - Method: Advanced API traversal with category mapping
    - Focus: Real-time product inventory, pricing, and hierarchical classification

---

## Data Characteristics

### Content Diversity

-   **Theory:** Wikipedia articles provide foundational knowledge
-   **Practice:** Plant Right guides offer step-by-step instructions
-   **Demonstration:** Videos show real-world application by experts
-   **Accessibility:** Mix of formal and informal language styles
-   **Commercial:** Shop data provides actionable purchasing options (Products, Prices, Availability)

### Coverage Areas

1. **Crops:** Grains, vegetables, fruits, herbs
2. **Techniques:** Planting, irrigation, fertilization, harvesting
3. **Pest Management:** Identification, organic control, pesticides
4. **Equipment:** Agricultural machinery and tools
5. **Soil Management:** Preparation, amendments, testing
6. **Seasonal Considerations:** Winter, spring, summer operations
7. **Marketplace:** Live inventory of fertilizers, pesticides, seeds, and solar systems

---

## Project Context

This data collection supports the DEPI-GP project's goal to create an **Arabic-Language Agricultural Assistant for an E-commerce Site**. The collected data enables:

-   Intelligent product recommendations (Linking problems found in Wikipedia/YouTube to solutions in the Shop)
-   Educational content delivery
-   Farmer guidance and support
-   Market-aware agricultural suggestions
-   Community-based knowledge sharing
-   **Direct Sales:** Converting advice ("You have aphids") into transactions ("Here is `Malathion 57%` for 150 EGP, available now").