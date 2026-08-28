export interface Reminder {
  id: number;
  pet_id: number;
  title: string;
  date: string;
  note?: string | null;
  completed?: boolean;
}
