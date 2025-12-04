### 1. Project Overview  
We are building a lightweight Arabic conversational assistant that will sit inside an agricultural‑tools shop. The assistant must:

* Understand a farmer’s free‑form request (e.g., “عايز سماد للطماطم وقت التزهير”).  
* Retrieve the most relevant products from the catalog using semantic search (embedding + vector DB).  
* Generate a concise reply in Arabic that lists 2‑3 suitable items, shows price/availability, or provides agricultural advice, and ends with a clear call‑to‑action (CTA) when needed.

The system consists of three major components:

1. **Embedding & Vector Search** – turns queries and product descriptions into dense vectors stored in a vector DB.  
2. **LLM (1 B‑parameter Arabic model)** – receives the structured product context and crafts the final natural‑language response.

### 2. Requirements  

| Category           | Requirement                                                                                                                                                               | Rationale                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Data**           | Product catalogue (id, name, description, price, stock, category); Generated seed conversation set (user + assistant); Intent labels (advice, pest, product_search, faq). | Catalogue feeds the vector search; the seed set trains the LLM’s tone; intents guide whether product retrieval is needed. |
| **Infrastructure** | Multilingual embedding model (BGE‑m3 / e5‑multilingual). Vector DB (Weaviate, Milvus, PGVector). GPU environment (≥ 16 GB VRAM) for fine‑tuning.                          | Enables search and efficient training.                                                                                    |
| **Software**       | Python 3.9+, Hugging Face `transformers` + `peft` for LoRA/QLoRA tuning, simple intent detector (rule‑based or small BERT).                                               | Provides the necessary development environment.                                                                           |

### 3. Explanation of the Components  

**Embedding & Vector Search** – encodes products and queries using multilingual embeddings to find semantically similar items.  
**LLM 1 B** – fine‑tuned on a seed set to generate friendly, grounded replies.  
**Intent Detector** – decides whether to fetch products or only provide general advice.

### 4. The Process

#### **Stage 1: Data Preparation & Product Embedding (تحضير البيانات وتضمين المنتجات)**
1. **Extract the product catalogue:** collect product data (CSV/Excel/JSONL) including `product_id`, `name`, `description`, `price`, `stock_status`, and preferably `category`.  
2. **Clean and normalize data:** verify completeness and consistency.  
3. **Generate embeddings:** use a multilingual embedding model (e.g., BGE‑m3) to convert names and descriptions into numerical vectors.  
4. **Store in a vector database:** load vectors and metadata into PGVector.

#### **Stage 2: Seed‑Set Generation for LLM Training 
Because **no real chat data exists**, synthetic data will be created automatically.  
1. **Gather textual sources:** collect varied agricultural content (articles, videos, FAQs).  
2. **Use a larger LLM (e.g., Llama‑3.1 70B)** to generate question–answer pairs from these texts. Each prompt instructs the model to produce 2‑3 dialogues per text segment, ensuring:  
   * acknowledgment of user need;  
   * 2–3 product suggestions with reasons + prices + CTA;  
   * inclusion of some general agricultural‑advice answers with no products;  
   * topical diversity.  
3. **Quick review:** manually check and fix obvious errors. Target 200–300 high‑quality examples.

#### **Stage 3: Fine‑tuning the LLM 
Apply LoRA/QLoRA instruction‑tuning to the Arabic 3B model using the generated seed set. The model learns both the “shop style” and how to integrate product information or general farming tips into responses.

#### **Stage 4: Intent Detection Setup (إعداد مكتشف النية والكيانات)**  
1. **Define intents:** (`product_search`, `agricultural_advice`, `pest_control`, `faq`, etc.).  
2. **Implement detector:** simple keyword rules or a small classification model trained on labeled examples (which can also be generated via a large LLM). This module drives conditional context retrieval.

---

### 5. Workflow  
**Textual Diagram**

```
User Query
   │
   ▼
Intent Detector
   │─► advice / faq → No product retrieval
   │─► product_search → Retrieve products
   │─► pest → Advice with CTA for products
   │
   ▼ (if retrieval)
Vector Search (top‑k)
   │
   ▼
Build Context block (2‑3 products)
   │
   ▼
Compose Prompt:
   System instruction +
   Context block +
   User question
   │
   ▼
LLM 1 B → Generate answer (with or without CTA)
   │
   ▼
Display answer in chat UI
```

---

### **Workflow : How the System Operates**

This section explains how components interact once a user submits a query.

1. **User Query (استلام استعلام المستخدم):**  
   The farmer enters a question in Arabic (e.g., “عايز سماد ورقي للطماطم يكون سعره مناسب” or “ازاي ازرع الطماطم في الصيف؟”) 
   in the chat widget.

2. **Intent  Detection (اكتشاف النية والكيانات):**  
   * The query passes to the intent/entity detector.  
   * It identifies the user’s intent (e.g., `product_search`, `agricultural_advice`).

3. **Conditional Context Generation (الاسترجاع الشرطي لـ Context):**  
   * **If the intent requires products** (`product_search`, `pest_control`):  
     - Embed the query.  
     - Perform vector search to get top‑k (10–20) products.  
     - Build a Context block including product name, price, availability, and reason for recommendation.  
   * **If the intent does not require products** (`agricultural_advice`, `faq`):  
     - Skip product retrieval.  
     - The Context block remains empty or contains general reference info from a separate knowledge base.

4. **Prompt Construction (بناء الـ Prompt النهائي):**  
   Combine intent, original query, and Context into one prompt sent to the LLM.

   **Prompt Example:**
   ```
   System:
   أنت مساعد زراعي يجيب على أسئلة المزارعين. إذا كان السؤال يحتاج اقتراح منتجات، استخدم المعلومات الموجودة في قسم "Context". 
   إذا لم يكن هناك Context، أجب بنصائح عامة فقط.

   Context:
   {constructed_context_text}  # مثال: - المنتج 1: اسم، سعر، توافر، سبب الاختيار (أو فارغ)

   User: {original_user_query}

   Assistant:
   ```

5. **LLM Response Generation (توليد رد الـ LLM):**  
   * The fine‑tuned LLM produces an Arabic answer based on the prompt.  
   * If a Context with products is present: the response acknowledges the need, lists 2–3 recommended items with justifications (price and fit), mentions stock status and ends with a CTA (“هل أضيفه للسلة؟”).  
   * If the Context is empty: it returns general farming advice or an FAQ answer.

6. **Display to User (عرض الرد للمستخدم):**  
   * The response appears in the chat interface.  
   * If recommendations exist, the UI shows product links or “Add to Cart” buttons for easy purchase.

---

### 6. Timeline & Milestones  

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Data preparation & embedding | 1 week | Product CSV, vector DB ready. |
| Seed‑set generation and review | 5 days | 200–300 synthetic Q&A pairs. |
| Fine‑tuning LLM (LoRA/QLoRA) | 1 week | Fine‑tuned 3 B model checkpoint. |
| Integration & testing | 1 week | Functional pipeline on staging. |
| Deployment & iteration | 2 weeks post‑launch | Improved model + real user data collected. |

### 7. Conclusion  

By combining semantic retrieval and a fine‑tuned 3 B Arabic LLM, this project delivers a smart assistant that answers agricultural questions and optionally recommends products. The process automates seed‑data generation with a larger LLM to overcome the lack of real conversations and keeps the system lightweight, accurate, and easy to update. The bilingual description above ensures parallel understanding for both English‑speaking stakeholders and Arabic‑speaking developers.