class SMSService:
    """Сервис отправки SMS-напоминаний"""
    
    def __init__(self):
        self.api_key = "demo_key_123"
    
    def send_reminder(self, appointment):
        """Отправка напоминания о приёме"""
        message = f"Напоминание: приём {appointment.date}"
        return f"SMS отправлено: {message}"
    
    
    def check_balance(self):
        """Проверка баланса SMS"""
        return 100  
