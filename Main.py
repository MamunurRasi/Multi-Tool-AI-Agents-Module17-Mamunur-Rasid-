# Day2
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from gmail_builder import get_gmail_service
from googleapiclient.discovery import build
from openai import OpenAI
load_dotenv()
# ----- 21. Define Specialized Agents ----

# Email agent
email_agent = Agent(
    role="Email Management Agent",
    goal="Read and summarize emails, identifying key actions or insights.",
    backstory=(
        "An assistant that processes incoming emails, extracts essential details, "
        "and recommends next steps for each email."
    ),
    verbose=True
)

# Report agent
report_agent = Agent(
    role="Report Generation Agent",
    goal="Create daily reports based on email summaries and business updates.",
    backstory=(
        "An analyst agent who compiles summarized insights into professional reports "
        "for management review."
    ),
    verbose=True
)

# Alert agent
alert_agent = Agent(
    role="Alert System Agent",
    goal="Detect urgent issues and send alerts to the operations manager.",
    backstory=(
        "A monitoring agent that ensures critical events or customer issues are "
        "immediately communicated to the right person."
    ),
    verbose=True
)

#  ---- 2. Example Input (Simulated) -----
service = get_gmail_service()

# Get last 5 emails
results = service.users().messages().list(userId="me", q="newer_than:1d").execute()
messages = results.get("messages", [])

emails = []
for msg in messages:
    full_msg = service.users().messages().get(
        userId="me", id=msg["id"],
        format="metadata", metadataHeaders=["From", "Subject"]
    ).execute()

    headers = full_msg["payload"]["headers"]
    subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)")
    sender = next((h["value"] for h in headers if h["name"] == "From"), "(Unknown Sender)")
    snippet = full_msg.get("snippet", "")
    emails.append({
        "from": sender,
        "subject": subject,
        "body": snippet
    })


# ----3. Define Tasks ----


# Task 1: Summarize emails
summarize_emails = Task(
    description=f"Analyze and summarize these emails:\n{emails}\nIdentify actions needed.",
    expected_output="Summaries of each email and action recommendations.",
    agent=email_agent,
)

# Task 2: Generate daily report
generate_report = Task(
    description="Based on the email summaries, create a professional daily report.",
    expected_output="A report including performance updates and any pending issues.",
    agent=report_agent,
)

# Task 3: Detect urgent issues and alert
send_alerts = Task(
    description="If any email mentions urgent issues, generate an alert message for the manager.",
    expected_output="An alert text summarizing the urgent issue.",
    agent=alert_agent,
)

# ---- 4. Build Crew (Pipeline) ----
crew = Crew(
    agents=[email_agent, report_agent, alert_agent],
    tasks=[summarize_emails, generate_report, send_alerts],
)


# ----5. Run the Crew ----
results = crew.kickoff()


