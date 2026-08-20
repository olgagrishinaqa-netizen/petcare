#!/usr/bin/env python3
"""
Скрипт для автоматической генерации напоминаний для всех питомцев.
Запускается по расписанию через cron.
"""

import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import SessionLocal
from app.services.reminder_generator import generate_reminders
from app.models.pet import Pet


def run():
    """Запускает генерацию напоминаний для всех питомцев."""
    db = SessionLocal()
    
    try:
        # Получаем всех питомцев
        pets = db.query(Pet).all()
        
        if not pets:
            print("No pets found")
            return
        
        total_reminders = 0
        
        for pet in pets:
            # Генерируем напоминания для каждого питомца
            reminders = generate_reminders(
                db=db,
                pet_id=pet.id,
                days_before=7
            )
            total_reminders += len(reminders)
            print(f"Pet {pet.id} ({pet.name}): created {len(reminders)} reminders")
        
        db.commit()
        print(f"Total reminders created: {total_reminders}")
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    run()
