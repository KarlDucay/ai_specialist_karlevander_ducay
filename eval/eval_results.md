# RAG Evaluation Report

## 📊 Run Info

- Date: 6/18/2026
- Model: llama3.2:3b
- Embeddings: nomic-embed-text

---

## 🧪 Test Cases

### 1. Question

**Q:** What is the capital of France?

\*_Expected Answer:_ Thee is no mention of.... \*
.

**Actual Answer:**

"answer": "There is no mention of the capital of France in the provided context.",
"sources": [
"02-beacon-product-overview.md",
"03-security-data-policy.md",
"06-team-directory.md",
"04-onboarding-faq.md",
"05-expense-travel-policy.md"
],
"grounding": false

**Metrics:**

- ✔ Answer Correctness: (5)
- ✔ Grounding: false
- ✔ Relevance: (0–5)
- ✔ Hallucination: No

---

### 2. Question

**Q:** Who is the president of the United States?

**Expected Answer:**
As of my knowledge cutoff in September 2021, the president of the United States is Joe Biden.

**Actual Answer:**
"answer": "There is no mention of the president of the United States in the provided contexts.",
"sources": [
"03-security-data-policy.md",
"06-team-directory.md",
"02-beacon-product-overview.md",
"04-onboarding-faq.md",
"05-expense-travel-policy.md"
],
"grounding": false

**Metrics:**

- ✔ Answer Correctness: (5)
- ✔ Grounding: false
- ✔ Relevance: (0)
- ✔ Hallucination: No

---

### 3. Question

**Q:** What is the largest mammal?

**Expected Answer:**
The largest mammal is the blue whale.

**Actual Answer:**
"answer": "There is no mention of animals or specific creatures in the provided policies.",
"sources": [
"02-beacon-product-overview.md",
"03-security-data-policy.md",
"06-team-directory.md"
],
"grounding": false

**Metrics:**

- ✔ Answer Correctness: (05)
- ✔ Grounding: false
- ✔ Relevance: (5)
- ✔ Hallucination: No

---

### 4. Question

**Q:** What is Platform Engineering?

**Expected Answer:**
Owns Beacon's backend, retrieval pipeline, and production infrastructure. Owns all production database access.

**Actual Answer:**
"answer": "Platform Engineering owns Beacon's backend, retrieval pipeline, and production infrastructure.",
"sources": [
"03-security-data-policy.md",
"04-onboarding-faq.md",
"05-expense-travel-policy.md"
],
"grounding": true
=

**Metrics:**

- ✔ Answer Correctness: (5)
- ✔ Grounding: true
- ✔ Relevance: (5)
- ✔ Hallucination:No

---

### 5. Question

**Q:** When are flights should be booked at least?

**Expected Answer:**
Flights should be booked at least 14 days in advance when possible.

**Actual Answer:**
"answer": "Flights should be booked at least 14 days in advance when possible.",
"sources": [
"02-beacon-product-overview.md",
"06-team-directory.md",
"05-expense-travel-policy.md",
"04-onboarding-faq.md",
"03-security-data-policy.md"
],
"grounding": true

**Metrics:**

- ✔ Answer Correctness: (5)
- ✔ Grounding: true
- ✔ Relevance: 5
- ✔ Hallucination:NO

---

### 6. Question

**Q:** Starter tier pricing?

**Expected Answer:**
$99/month, up to 1,000 resolved conversations.

**Actual Answer:**
"answer": "The Starter tier of Beacon is $99/month, with a limit of up to 1,000 resolved conversations.",
"sources": [
"04-onboarding-faq.md",
"02-beacon-product-overview.md",
"03-security-data-policy.md"
],
"grounding": true

**Metrics:**

- ✔ Answer Correctness: 5
- ✔ Grounding:true
- ✔ Relevance: 5
- ✔ Hallucination: No

---

### 7. Question

**Q:** Growth tier pricing?

**Expected Answer:**
$499/month, up to 10,000 resolved conversations.

**Actual Answer:**
{
"answer": "The Growth tier pricing is $499/month, with up to 10,000 resolved conversations.",
"sources": [
"04-onboarding-faq.md",
"02-beacon-product-overview.md",
"03-security-data-policy.md"
],
"grounding": true
}

**Metrics:**

- ✔ Answer Correctness: (5)
- ✔ Grounding: true
- ✔ Relevance: (5)
- ✔ Hallucination: No

---

### 8. Question

**Q:** Enterprise tier pricing?

**Expected Answer:**
Custom pricing, unlimited conversations, SSO, and a dedicated success manager.

**Actual Answer:**
{
"answer": "Custom pricing for the Enterprise tier.",
"sources": [
"02-beacon-product-overview.md",
"03-security-data-policy.md",
"04-onboarding-faq.md"
],
"grounding": true
}

**Metrics:**

- ✔ Answer Correctness: (4)
- ✔ Grounding: Yes / No
- ✔ Relevance: (5)
- ✔ Hallucination: No

---

### 9. Question

**Q:** Beacon integrates with which platforms?

**Expected Answer:**
Beacon integrates with Zendesk, Intercom, and Salesforce Service Cloud out of the box.

**Actual Answer:**
{
"answer": "Beacon integrates with Zendesk, Intercom, and Salesforce Service Cloud out of the box.",
"sources": [
"04-onboarding-faq.md",
"03-security-data-policy.md",
"05-expense-travel-policy.md"
],
"grounding": true
}

**Metrics:**

- ✔ Answer Correctness: (5)
- ✔ Grounding: true
- ✔ Relevance: 5
- ✔ Hallucination: No

---

### 10. Question

**Q:** Atlas Labs classifies all data into three levels, what are they?

**Expected Answer:**
Public, Internal, and Confidential.

**Actual Answer:**
{
"answer": "There is no mention of a specific classification system for employee roles in this document.",
"sources": [
"05-expense-travel-policy.md",
"03-security-data-policy.md",
"06-team-directory.md",
"02-beacon-product-overview.md",
"04-onboarding-faq.md"
],
"grounding": false
}

**Metrics:**

- ✔ Answer Correctness: (0)
- ✔ Grounding:false
- ✔ Relevance: (0)
- ✔ Hallucination:YES

---
