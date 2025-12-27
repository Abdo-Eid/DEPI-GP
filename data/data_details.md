### 1) Files on disk

```
/data/
  agri_sft.jsonl
  system_prompt.txt
```

### 2) JSONL schema (one training example per line)

```jsonl
{
  "id": "number",
  "source": "egy_topics|youtube|wikipedia",
  "messages": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ]
}
```

* **No system message stored in the dataset.**
* `source` stays for filtering/stratified splits.

---

## Approach A: Custom ChatML template (model-agnostic)

Use this template during preprocessing/tokenization if you want a fixed, custom format across models:

**ChatML-like format**

```
<|system|>
{SYSTEM_PROMPT}
<|user|>
{USER_CONTENT}
<|assistant|>
{ASSISTANT_CONTENT}
```

For multi-turn:

* repeat `<|user|> ... <|assistant|> ...` pairs.
* Keep the assistant response you want to learn as the last assistant turn.


## Approach B: Use the model’s built-in chat template (recommended for Gemma and many HF chat models)

If the model provides its own `chat_template`, inject the system message and format using:

```python
text = tokenizer.apply_chat_template(
    messages_with_system,
    tokenize=False,
    add_generation_prompt=False
)
```

This preserves the model’s expected formatting without forcing a custom ChatML format.


## How to inject the system message

### Prepend system message in-memory before formatting

**Pseudo-logic**

1. Load system prompt from `/data/system_prompt.txt`
2. For each example:

   * create `messages_with_system = [{"role":"system","content": system_prompt}] + example["messages"]`
3. Format using either:

   * **Approach A:** your custom ChatML template, or
   * **Approach B:** the model’s `apply_chat_template(...)`
4. Train


## What the final rendered sample looks like (Approach A)

Given dataset record (no system stored):

```json
{
  "id":"0001",
  "source":"egy_topics",
  "messages":[
    {"role":"user","content":"اشرحلي مرض البياض الدقيقي (أمراض فطرية)"},
    {"role":"assistant","content":"..."}
  ]
}
```

After injection + rendering:

```
<|system|>
...contents of /data/system_prompt.txt...
<|user|>
اشرحلي مرض البياض الدقيقي (أمراض فطرية)
<|assistant|>
...
```
