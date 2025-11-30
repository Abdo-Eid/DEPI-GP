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

---

## Data Characteristics

### Content Diversity

-   **Theory:** Wikipedia articles provide foundational knowledge
-   **Practice:** Plant Right guides offer step-by-step instructions
-   **Demonstration:** Videos show real-world application by experts
-   **Accessibility:** Mix of formal and informal language styles

### Coverage Areas

1. **Crops:** Grains, vegetables, fruits, herbs
2. **Techniques:** Planting, irrigation, fertilization, harvesting
3. **Pest Management:** Identification, organic control, pesticides
4. **Equipment:** Agricultural machinery and tools
5. **Soil Management:** Preparation, amendments, testing
6. **Seasonal Considerations:** Winter, spring, summer operations

---

## Project Context

This data collection supports the DEPI-GP project's goal to create an **Arabic-Language Agricultural Assistant for an E-commerce Site**. The collected data enables:

-   Intelligent product recommendations
-   Educational content delivery
-   Farmer guidance and support
-   Market-aware agricultural suggestions
-   Community-based knowledge sharing
