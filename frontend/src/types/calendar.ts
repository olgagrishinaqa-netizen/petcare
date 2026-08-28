export type CalendarEventType =
  | "vaccination"
  | "vaccination_next"
  | "deworming"
  | "deworming_next"
  | "flea_tick"
  | "flea_tick_next"
  | "reminder"
  | "note";

export interface CalendarEvent {
  id: number;
  pet_id: number;
  title: string;
  date: string;
  event_type: CalendarEventType;
  note?: string | null;
  source_id?: number;
}
