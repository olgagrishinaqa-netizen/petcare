import { useEffect, useMemo, useState } from "react";
import { getPetCalendar } from "../api/pets";
import type { CalendarEvent } from "../types/calendar";

interface PetCalendarProps {
  petId: number;
}

const monthNames = [
  "Январь",
  "Февраль",
  "Март",
  "Апрель",
  "Май",
  "Июнь",
  "Июль",
  "Август",
  "Сентябрь",
  "Октябрь",
  "Ноябрь",
  "Декабрь",
];

const weekDays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"];

function formatDate(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");

  return `${year}-${month}-${day}`;
}

function getEventIcon(type: CalendarEvent["event_type"]): string {
  switch (type) {
    case "vaccination":
    case "vaccination_next":
      return "💉";

    case "deworming":
    case "deworming_next":
      return "🐛";

    case "flea_tick":
    case "flea_tick_next":
      return "🦟";

    case "reminder":
      return "🔔";

    case "note":
      return "📝";

    default:
      return "📌";
  }
}

function PetCalendar({ petId }: PetCalendarProps) {
  const [currentDate, setCurrentDate] = useState(new Date());
  const [events, setEvents] = useState<CalendarEvent[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const year = currentDate.getFullYear();
  const month = currentDate.getMonth();

  useEffect(() => {
    const startDate = new Date(year, month, 1);
    const endDate = new Date(year, month + 1, 0);

    setLoading(true);
    setError(null);

    getPetCalendar(
      petId,
      formatDate(startDate),
      formatDate(endDate),
    )
      .then((data) => {
        setEvents(data);
      })
      .catch((err) => {
        setError(
          err instanceof Error
            ? err.message
            : "Не удалось загрузить календарь",
        );
      })
      .finally(() => {
        setLoading(false);
      });
  }, [petId, year, month]);

  const calendarDays = useMemo(() => {
    const firstDay = new Date(year, month, 1);

    // JavaScript: воскресенье = 0.
    // Нам нужен понедельник = 0.
    const firstWeekDay = (firstDay.getDay() + 6) % 7;

    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const days: (number | null)[] = [];

    for (let i = 0; i < firstWeekDay; i++) {
      days.push(null);
    }

    for (let day = 1; day <= daysInMonth; day++) {
      days.push(day);
    }

    return days;
  }, [year, month]);

  const eventsByDate = useMemo(() => {
    const map = new Map<string, CalendarEvent[]>();

    for (const event of events) {
      const existing = map.get(event.date) ?? [];
      existing.push(event);
      map.set(event.date, existing);
    }

    return map;
  }, [events]);

  const goToPreviousMonth = () => {
    setCurrentDate(new Date(year, month - 1, 1));
  };

  const goToNextMonth = () => {
    setCurrentDate(new Date(year, month + 1, 1));
  };

  const goToToday = () => {
    setCurrentDate(new Date());
  };

  return (
    <section className="calendar-section">
      <div className="calendar-header">
        <div>
          <p className="welcome-label">Календарь ухода</p>

          <h2>
            {monthNames[month]} {year}
          </h2>
        </div>

        <div className="calendar-controls">
          <button
            className="calendar-nav-button"
            onClick={goToPreviousMonth}
            aria-label="Предыдущий месяц"
          >
            ‹
          </button>

          <button
            className="calendar-today-button"
            onClick={goToToday}
          >
            Сегодня
          </button>

          <button
            className="calendar-nav-button"
            onClick={goToNextMonth}
            aria-label="Следующий месяц"
          >
            ›
          </button>
        </div>
      </div>

      {loading && (
        <div className="calendar-status">
          Загрузка событий...
        </div>
      )}

      {error && (
        <div className="calendar-status calendar-error">
          <strong>Не удалось загрузить календарь</strong>
          <p>{error}</p>
        </div>
      )}

      {!loading && !error && (
        <>
          <div className="calendar-grid calendar-weekdays">
            {weekDays.map((day) => (
              <div key={day} className="calendar-weekday">
                {day}
              </div>
            ))}
          </div>

          <div className="calendar-grid calendar-days">
            {calendarDays.map((day, index) => {
              if (day === null) {
                return (
                  <div
                    key={`empty-${index}`}
                    className="calendar-day calendar-day-empty"
                  />
                );
              }

              const date = formatDate(
                new Date(year, month, day),
              );

              const dayEvents = eventsByDate.get(date) ?? [];

              const isToday =
                formatDate(new Date()) === date;

              return (
                <div
                  key={date}
                  className={`calendar-day ${
                    isToday ? "calendar-day-today" : ""
                  }`}
                >
                  <div className="calendar-day-number">
                    {day}
                  </div>

                  <div className="calendar-day-events">
                    {dayEvents.map((event) => (
                      <div
                        key={`${event.event_type}-${event.source_id ?? event.id}`}
                        className={`calendar-event event-${event.event_type}`}
                        title={
                          event.note
                            ? `${event.title}: ${event.note}`
                            : event.title
                        }
                      >
                        <span className="calendar-event-icon">
                          {getEventIcon(event.event_type)}
                        </span>

                        <span className="calendar-event-title">
                          {event.title}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>

          <div className="calendar-events-list">
            <h3>События месяца</h3>

            {events.length === 0 ? (
              <p className="calendar-empty">
                В этом месяце событий нет.
              </p>
            ) : (
              events
                .slice()
                .sort((a, b) =>
                  a.date.localeCompare(b.date),
                )
                .map((event) => (
                  <article
                    key={`${event.event_type}-${event.source_id ?? event.id}`}
                    className="calendar-event-card"
                  >
                    <div className="calendar-event-card-icon">
                      {getEventIcon(event.event_type)}
                    </div>

                    <div>
                      <strong>{event.title}</strong>

                      <p>
                        {new Date(
                          `${event.date}T00:00:00`,
                        ).toLocaleDateString("ru-RU", {
                          day: "numeric",
                          month: "long",
                          year: "numeric",
                        })}
                      </p>

                      {event.note && (
                        <small>{event.note}</small>
                      )}
                    </div>
                  </article>
                ))
            )}
          </div>
        </>
      )}
    </section>
  );
}

export default PetCalendar;
