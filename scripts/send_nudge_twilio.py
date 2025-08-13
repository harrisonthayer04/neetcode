import os, random, requests
from datetime import datetime, timezone
import pytz

# --- Config from env ---
ACC_SID = os.environ["TWILIO_ACCOUNT_SID"]
AUTH = os.environ["TWILIO_AUTH_TOKEN"]
TO = os.environ["TWILIO_TO"]
FROM = os.environ.get("TWILIO_FROM")  # optional if using Messaging Service
MSG_SID = os.environ.get("TWILIO_MESSAGING_SID")  # optional alternative

REPO = os.environ.get("GITHUB_REPO")
GH_TOKEN = os.environ.get("GH_TOKEN")
SKIP_IF_DONE = os.environ.get("SKIP_IF_DONE", "0") == "1"
SUPPRESS_WEEKENDS = os.environ.get("SUPPRESS_WEEKENDS", "0") == "1"

LA = pytz.timezone("America/Los_Angeles")

# --- Optional hourly-run guard (enable if your cron is hourly) ---
# now_la = datetime.now(LA)
# if not (now_la.hour == 9 and now_la.minute < 10):
#     print("Not in 09:00–09:09 LA window; exiting.")
#     raise SystemExit(0)

def committed_today(repo: str, token: str) -> bool:
    """Check if there was any commit to the repo since midnight LA today."""
    if not (repo and token):
        return False
    now_la = datetime.now(LA)
    start_la = LA.localize(datetime(now_la.year, now_la.month, now_la.day, 0, 0, 0))
    start_utc = start_la.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    url = f"https://api.github.com/repos/{repo}/commits"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    params = {"since": start_utc, "per_page": 1}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=20)
        r.raise_for_status()
        return len(r.json()) > 0
    except Exception as e:
        print("Commit check failed:", e)
        return False  # fail-open to still send nudges

TODO_LINES = [
    "Time to level up 🧠 — grab the daily LeetCode!",
    "Tiny steps → big gains. Daily problem time!",
    "Let’s keep the streak alive 🔥. One problem today.",
    "You vs. yesterday’s you. 1 problem. Go! 💪",
    "Coffee + one LeetCode. That’s the pact ☕️📚",
]

DONE_LINES = [
    "Nice work on today’s push! 🎉 Keep the momentum.",
    "Streak looking spicy 🌶️. Proud of you!",
    "Daily reps complete. Consistency is OP 💯",
    "You showed up today — that’s the hardest part 🙌",
    "Ship. Learn. Repeat. See you tomorrow! 🚀",
]

EXTRA_PROMPTS = [
    "Try a data structure you’ve been avoiding.",
    "Solve then refactor for readability.",
    "Write a brute-force first, then optimize.",
    "Explain your solution in 3 sentences in the README.",
    "Pick a tag you rarely touch (graphs/DP/greedy).",
]

def send_sms(acc_sid: str, auth: str, to: str, body: str, from_num: str = None, msg_sid: str = None):
    """
    Send an SMS via Twilio REST API.
    Use either a raw From number or a Messaging Service SID.
    """
    url = f"https://api.twilio.com/2010-04-01/Accounts/{acc_sid}/Messages.json"
    data = {"To": to, "Body": body}
    if msg_sid:
        data["MessagingServiceSid"] = msg_sid
    elif from_num:
        data["From"] = from_num
    else:
        raise RuntimeError("Provide TWILIO_FROM or TWILIO_MESSAGING_SID")

    r = requests.post(url, data=data, auth=(acc_sid, auth), timeout=20)
    try:
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Twilio API error:", r.text)
        raise e

# Suppress weekends if configured
if SUPPRESS_WEEKENDS:
    if datetime.now(LA).weekday() >= 5:  # 5=Sat,6=Sun
        print("Weekend; skipping.")
        raise SystemExit(0)

already_done = committed_today(REPO, GH_TOKEN)

if SKIP_IF_DONE and already_done:
    print("Already pushed today; SKIP_IF_DONE=1 so not sending.")
    raise SystemExit(0)

line = random.choice(DONE_LINES if already_done else TODO_LINES)
prompt = random.choice(EXTRA_PROMPTS)
msg = f"{line}\n\nToday’s nudge: {prompt}\n\nRepo: {REPO}"

send_sms(ACC_SID, AUTH, TO, msg, FROM, MSG_SID)
print("SMS sent.")
