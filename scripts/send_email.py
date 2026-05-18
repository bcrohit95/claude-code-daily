"""Send the day's lesson by email via Gmail SMTP.

Reads the lesson markdown file path from the LESSON_PATH env var (set by the workflow),
renders it as both plain text and a simple HTML version, and sends it.

Required env vars:
  GMAIL_FROM           - sender Gmail address
  GMAIL_APP_PASSWORD   - 16-char Gmail app password
  GMAIL_TO             - recipient address
  LESSON_PATH          - path to today's lesson markdown file (relative to repo root)
"""
import os
import smtplib
import sys
from email.message import EmailMessage
from pathlib import Path


def md_to_basic_html(md: str) -> str:
    """Tiny markdown->HTML. Good enough for Gmail; not a real parser."""
    lines = md.splitlines()
    out = []
    in_code = False
    for line in lines:
        if line.startswith("```"):
            out.append("<pre style='background:#f4f4f4;padding:8px;border-radius:4px'>" if not in_code else "</pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(line.replace("<", "&lt;").replace(">", "&gt;"))
            continue
        if line.startswith("# "):
            out.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("- "):
            out.append(f"<li>{line[2:]}</li>")
        elif line.strip() == "":
            out.append("<br>")
        else:
            out.append(f"<p>{line}</p>")
    return "<html><body style='font-family:-apple-system,sans-serif;max-width:640px;margin:auto'>" + "\n".join(out) + "</body></html>"


def main() -> int:
    lesson_path = os.environ.get("LESSON_PATH", "").strip()
    sender = os.environ["GMAIL_FROM"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    recipient = os.environ["GMAIL_TO"]

    if not lesson_path:
        print("ERROR: LESSON_PATH env var is empty. Did the lesson generator run?", file=sys.stderr)
        return 1

    path = Path(lesson_path)
    if not path.is_file():
        print(f"ERROR: lesson file not found at {path}", file=sys.stderr)
        return 1

    body_md = path.read_text(encoding="utf-8")

    # Subject = first H1 line, fallback to filename
    subject = path.stem
    for line in body_md.splitlines():
        if line.startswith("# "):
            subject = line[2:].strip()
            break

    msg = EmailMessage()
    msg["Subject"] = f"Claude Code Daily — {subject}"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(body_md)
    msg.add_alternative(md_to_basic_html(body_md), subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(sender, password)
        s.send_message(msg)

    print(f"Sent lesson '{subject}' to {recipient}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
