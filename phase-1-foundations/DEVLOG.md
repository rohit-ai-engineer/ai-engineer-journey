# 📓 Devlog — AI Engineer Journey

> An honest, weekly log of my learning. The wins, the confusion, the breakthroughs.  
> Updated every Saturday.

---

## How I Use This Log

Every Saturday I answer these 5 questions:
1. What did I actually learn this week (not just watch)?
2. What was the hardest thing?
3. What am I most proud of building?
4. How many hours did I put in?
5. What's my plan for next week?

---

## 🗓️ Phase 1 · Foundations

---

### Block 1 — Entry 1 | Week 1 | March 2-3, 2026

**Theme:** Python fundamentals — accelerated track  
**Hours logged:** ~6 hours across 3 days

**What I actually learned:**
- Variables, print(), input() — the basics
- Working with the datetime module (strptime, strftime)
- How to format time strings properly
- CSV parsing with csv.DictReader
- **XML parsing with ElementTree** — tags vs attributes, finding elements
- The importance of actually saving files before running them (lol)
- f-strings for cleaner output
- try/except for error handling
- File paths and working directories in terminal

**The hardest thing this week:**
> Understanding XML structure — especially the difference between tags and attributes. At first I thought `announcedTime` was a tag, but it's actually an attribute on the `<slot>` tag. Also caught a bug in the validator where it was checking for date on every slot when date is actually stored once at the `<schedule>` level. Used my domain knowledge from Nielsen and Simply.TV to spot that!

**What I built:**
- `calculator.py` — basic calculator with 4 operations (addition, subtraction, multiplication, division)
- `epg_time_calculator.py` — calculates show end time from start time + duration (actually useful for my job!)
- `metadata_validator.py` — validates CSV metadata, checks for missing fields and invalid values
- `epg_flexible_validator.py` — **validates real real life EPG XML feeds** — this is production-level stuff! Checks 137+ programs for missing announcedTime, date, and title

**Moment I'm most proud of:**
> Building the XML EPG validator. It works on REAL provider feeds — the exact kind of data I work with at Simply.TV. When it validated all 137 programs successfully, that felt incredible. First time I built something that could legitimately be used in my actual job.

**Honest self-assessment:**
> Variables: 9/10, print/input: 9/10, datetime: 7/10, CSV parsing: 8/10, XML parsing: 6/10 (still learning), error handling: 7/10, control flow (loops/conditions): 8/10

**Plan for next week:**
- Start Week 2: OOP (classes, objects, methods)
- Build the Streaming Catalog Manager using proper OOP
- Maybe tackle the optional Content Duration Aggregator if time allows

**Week 1 complete? Almost — 4 out of 5 projects done. Moving to Week 2.**

---

### Block 1 — Week 2 — Entry 2 | March 3-4, 2026

**Theme:** OOP, File I/O & Error Handling  
**Hours logged:** ~5 hours across 2 days

**What I actually learned:**
- Classes vs objects — the blueprint vs the actual thing built from it
- `__init__` method — the constructor that runs when you create an object
- `self` — refers to the specific instance (THIS object)
- Methods — functions that belong to a class
- When to put code in Content class vs Catalog class (single item vs collection)
- JSON persistence — saving/loading data so it survives between runs
- Dictionary counting pattern — checking if key exists, then add 1 or create new
- `**kwargs` — passing flexible named arguments to functions
- try/except for handling missing files gracefully

**The hardest thing this week:**
> Understanding WHERE code should go. I tried to put a counting method in the Content class when it should've been in Catalog. It clicked when I realized: Content = ONE show, Catalog = MANY shows. Also struggled with the genre counting logic at first — had to really think through the if/else pattern for dictionaries. But once I got it, it made total sense.

**What I built:**
- `content.py` — Content class with is_movie(), matches_genre(), get_type() methods
- `catalog.py` — Catalog class that manages a collection of Content objects
- Features: add, remove, search (with multiple filters), save to JSON, load from JSON, duplicate prevention, statistics dashboard
- The stats dashboard was mostly me — wrote the movie/episode counting and genre dict logic myself with guidance

**Moment I'm most proud of:**
> Writing the genre counting logic myself. Even though I referenced the explanation, I understood WHY each line worked. When I saw the output with the genre breakdown, that felt like a real accomplishment. Also realizing I had built something that actually persists data — that's not a toy anymore.

**Honest self-assessment:**
> OOP concepts: 6/10 (understand basics but still building intuition), loops: 8/10, dictionaries: 7/10, file I/O: 8/10, knowing where code belongs: 5/10 (need more practice)

**Brutal honesty moment:**
> Realized halfway through that I'm doing OOP without solid fundamentals. It's like learning Formula 1 racing before learning to drive. I can follow along and build things with guidance, but I couldn't write this from scratch yet. Need to go back and drill the basics more.

**Plan for this week:**
- Do fundamentals practice exercises (loops, dicts, functions — no OOP)
- Solidify the concepts before Week 3
- Make sure I can write basic programs WITHOUT looking anything up
- Then start Week 3: APIs & Data Pipelines

**Week 2 complete? (Y/N):** Y — but with the understanding that I need fundamentals practice before moving forward

---

### Block 1 — Entry 3 | Week 3 | [DATE]

**Theme:** Functions & data structures  
**Hours logged:** ___ hours

**What I actually learned:**
- 

**The hardest thing:**
> 

**Block 1 Capstone — Contact Book:**
> [Describe your contact book app. What does it do? What was tricky to build?]

**Block 1 complete? (Y/N):** 

---

### Block 2 — Entry 4 | Week 4 | [DATE]

**Theme:** Object-Oriented Programming  
**Hours logged:** ___ hours

**The OOP click moment:**
> [OOP always has a "click moment." Describe when it clicked for you.]

**What I built:**
- 

---

### Block 2 — Entry 5 | Week 5 | [DATE]

**Theme:** Files, errors & modules  
**Hours logged:** ___ hours

---

### Block 2 — Entry 6 | Week 6 | [DATE]

**Theme:** Advanced Python + Git  
**Hours logged:** ___ hours

**Block 2 Capstone — Finance CLI:**
> [Describe your finance CLI app.]

**Block 2 complete? (Y/N):** 

---

### Block 3 — Entry 7 | Week 7 | [DATE]

**Theme:** Linear Algebra  
**Hours logged:** ___ hours

**3Blue1Brown moment that blew my mind:**
> [What visual explanation made things click?]

---

### Block 3 — Entry 8 | Week 8 | [DATE]

**Theme:** Calculus & Gradient Descent  
**Hours logged:** ___ hours

**Linear Regression from scratch — status:**
> [Describe where you are with this project. What was the hardest part of implementing gradient descent?]

---

### Block 3 — Entry 9 | Week 9 | [DATE]

**Theme:** Statistics & Probability  
**Hours logged:** ___ hours

**Bayes' theorem in my own words:**
> [Explain it like you'd explain it to a friend over coffee.]

**Block 3 complete? (Y/N):** 

---

### Block 4 — Entry 10 | Week 10 | [DATE]

**Theme:** Pandas  
**Hours logged:** ___ hours

**Most useful Pandas operation I learned:**
> 

---

### Block 4 — Entry 11 | Week 11 | [DATE]

**Theme:** Visualization + SQL  
**Hours logged:** ___ hours

---

### Block 4 — Entry 12 | Week 12 | [DATE] 🎉

**Theme:** Phase 1 Capstone — EDA Project  
**Hours logged:** ___ hours

**My EDA Project:**
- Dataset chosen: 
- Key findings: 
- Visualizations created: 
- GitHub link: 

**Phase 1 complete reflection:**
> [This is your most important devlog entry. Look back at Week 1 you. What changed? What do you know now that seemed impossible 12 weeks ago? Write freely — minimum 100 words.]

**Phase 1 complete? (Y/N):** 

**Ready for Phase 2? (Y/N):** 

---

## 📊 Phase 1 Stats Summary

| Metric | Value |
|--------|-------|
| Total weeks | 12 |
| Total hours logged | ___ |
| Projects built | ___ |
| GitHub commits | ___ |
| Toughest concept | ___ |
| Most fun project | ___ |

---

*Phase 2 — Machine Learning devlog will start in `../phase-2-machine-learning/DEVLOG.md`*
