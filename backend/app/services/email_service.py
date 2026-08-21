from brevo import AsyncBrevo
from brevo.transactional_emails import (
    SendTransacEmailRequestSender,
    SendTransacEmailRequestToItem,
)

from app.core.config import settings


client = AsyncBrevo(api_key=settings.BREVO_API_KEY)


async def send_email(
    recipient: str,
    subject: str,
    body: str,
):
    result = await client.transactional_emails.send_transac_email(
        subject=subject,
        text_content=body,
        sender=SendTransacEmailRequestSender(
            name="SciConnect",
            email=settings.MAIL_FROM,
        ),
        to=[
            SendTransacEmailRequestToItem(
                email=recipient,
            )
        ],
    )

    print("Brevo email sent successfully:", result.message_id)