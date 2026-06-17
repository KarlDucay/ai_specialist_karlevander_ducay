## Recording

https://drive.google.com/file/d/1kHyppdpFNYZFDMWEmA1z3oXhpGdD-gTz/view?usp=sharing

### Prerequisites

#### Install Git

**Windows:**

1. Download the installer from https://git-scm.com/download/win
2. Run the `.exe` and follow the setup wizard (keep default options)
3. During install, select **"Git from the command line and also from 3rd-party software"** when prompted about PATH

**macOS:**

```bash
brew install git
```

> If you don't have Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

**Linux (Ubuntu/Debian):**

```bash
sudo apt update && sudo apt install git -y
```

---

#### Add Git to PATH (Windows only)

If Git isn't recognized after install, add it manually:

1. Search **"Environment Variables"** in the Start menu
2. Click **"Environment Variables..."**
3. Under **System Variables**, find and select **`Path`** → click **Edit**
4. Click **New** and add:

```
   C:\Program Files\Git\cmd
```

5. Click **OK** on all dialogs
6. Open a new terminal and verify:

```bash
   git --version
```

---

### Cloning

Once Git is installed, clone the repository:

```bash
git clone https://github.com/KarlDucay/ai_specialist_karlevander_ducay.git
```

Then navigate into the project folder:

```bash
cd ai_specialist_karlevander_ducay
```

## Repo setups

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate Environment

**Windows:**

```bash
.\venv\Scripts\Activate.ps1
```

> **First-time setup — PowerShell Execution Policy**
>
> On first run, you may see this error:
>
> ```
> .\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is
> disabled on this system.
> ```
>
> Fix it by running this **once** in PowerShell as Administrator:
>
> ```bash
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
>
> Then re-run the activate command above.

**macOS/Linux:**

```bash
source venv/bin/activate
```

> ✅ You should see `(venv)` prepended to your terminal prompt once activated.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## MODEL USED (OLLAMA LLM)

install ollama first

- Go to CMD , run `curl -L -o OllamaSetup.exe https://ollama.com`
- run `ollama serve`

Install models :

Embedding Model :

    - nomic-embed-text

    run `ollama pull nomic-embed-text`

LLM Model :

- llama3.2:3b

- run `ollama pull llama3.2:3b`

### Run

```powershel/bash
uvicorn src.orchestrator:app  -reload
```

OR

```powershel/bash
uvicorn src.orchestrator:app  -reload
```

or

```powershel/bash
python -m uvicorn src.orchestrator:app
```

### Test API GET using POSTMAN

install Postman for windows/what your OS is .
verb : GET
params : key = question : value

```
http://127.0.0.1:8000/ask?question={}
```

- Verfiy the results .

### Design decisions

- added venv so that packages installed in global python library wont conflict with th packages for the project.
- used python since its what im currently mostly working with .
- dropped the use of API key based models , vector store since it will add more dependency .
- since no use of API key and outside vector stores , upserting is called upon starting of server since it will only be leaving inside ram and can be accessible during runtime only .
- used llama3.2:3b instead of mistral since its more lightweight sand my laptop can handle it more .
- By giving the command to the LLM using the system prompts , i can put constraint on it ,and make it return a specific phrase which then I based from to create a value for the groounding. grounding is first set to true then , if the response contains the phrase , then grounding will be false.

## Evaluation —

- out of 10 questions , only 1 question has got the wrong answer , overall all 9 question asked has been asnwered correctly and if not included in the corpus , says there is no mention of , and the grounding becomes false . in the 1 question that has been wrong , it consists of a more complex questions not focusing on 1 sentence as its asnwer which adds more complexity for the LLM to process. thus even though the answer for it exists , LLM states it as non exsitent . the system needs more proccesing pwower and improve chunking methods , improve upserting method , and retrieval .

## AI tools used

- used chatgpt for syntax and questions to enhance developments speed.
- used claude to convert the made json question/answers and make a template for evals result .
- used for set up of needed packages .

## With more time

- I will think more about how to properly chunk in contrast to the documents provided .
- I will test this thouroughly and add more system prompts to enhance the behaviour and response credibility .
- properly modularize the code then avoid hardcoding stuffs like the model .
- add more helper fuctions to help with matching/retrieval like using regex , input validations , etc....
