import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional, List


class GmailClient:
    """Класс для отправки и получения писем через Gmail."""

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.smtp_server = "smtp.gmail.com"
        self.imap_server = "imap.gmail.com"

    def send_email(self, recipients: List[str], subject: str, message: str) -> None:
        """Отправка письма."""
        msg = MIMEMultipart()
        msg["From"] = self.login
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain", "utf-8"))

        try:
            with smtplib.SMTP(self.smtp_server, 587) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.login, self.password)
                server.sendmail(self.login, recipients, msg.as_string())
        except smtplib.SMTPException as e:
            print(f"Ошибка при отправке письма: {e}")

    def receive_email(
        self, header: Optional[str] = None
    ) -> Optional[email.message.Message]:
        """Получение последнего письма (по заголовку или всех)."""
        try:
            with imaplib.IMAP4_SSL(self.imap_server) as mail:
                mail.login(self.login, self.password)
                mail.select("inbox")

                criterion = f'(HEADER Subject "{header}")' if header else "ALL"
                result, data = mail.uid("search", None, criterion)

                if not data or not data[0]:
                    print("Писем с заданным критерием не найдено.")
                    return None

                latest_email_uid = data[0].split()[-1]
                result, data = mail.uid("fetch", latest_email_uid, "(RFC822)")

                if not data or not data[0]:
                    print("Не удалось получить письмо.")
                    return None

                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)

                return email_message
        except imaplib.IMAP4.error as e:
            print(f"Ошибка при получении писем: {e}")
            return None


if __name__ == "__main__":
    login = input("Введите email: ").strip()
    password = input("Введите пароль приложения: ").strip()

    client = GmailClient(login, password)

    action = input("Выберите действие (send / receive): ").strip().lower()

    if action == "send":
        subject = input("Тема письма: ").strip()
        recipients_input = input("Получатели (через запятую): ").strip()
        recipients = [r.strip() for r in recipients_input.split(",") if r.strip()]
        message = input("Текст письма: ").strip()

        client.send_email(recipients, subject, message)
        print("✅ Письмо отправлено!")

    elif action == "receive":
        header = input("Заголовок для поиска (Enter для всех): ").strip() or None
        email_obj = client.receive_email(header)
        if email_obj:
            print("\n--- Последнее письмо ---")
            print("От:", email_obj["From"])
            print("Тема:", email_obj["Subject"])
            print("Содержимое:")
            for part in email_obj.walk():
                if part.get_content_type() == "text/plain":
                    charset = part.get_content_charset() or "utf-8"
                    text = part.get_payload(decode=True).decode(
                        charset, errors="replace"
                    )
                    print(text)
    else:
        print("Неизвестная команда.")