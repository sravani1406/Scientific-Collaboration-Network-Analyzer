import resend

from app.core.config import settings


resend.api_key = settings.RESEND_API_KEY


async def send_email(
    recipient: str,
    subject: str,
    body: str,
):
    params: resend.Emails.SendParams = {
        "from": settings.MAIL_FROM,
        "to": [recipient],
        "subject": subject,
        "html": f"<p>{body}</p>",
    }

    return await resend.Emails.send_async(params)