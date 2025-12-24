class SMSService:
    """Сервис отправки SMS-напоминаний"""
    
    def __init__(self, api_key="prod_key_456"):
        self.api_key = api_key
    
    def send_reminder(self, appointment, urgent=False):
        """Отправка напоминания о приёме"""
        prefix = "СРОЧНО! " if urgent else ""
        message = f"{prefix}Напоминание: приём {appointment.date}"
        return f"SMS отправлено: {message}"
    
    
    def log_sent(self, count):
        print(f"Отправлено SMS: {count}")
