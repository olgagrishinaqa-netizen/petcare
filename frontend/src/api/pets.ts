import { apiGet } from "./client";
import type { Pet } from "../types/pet";
import type { CalendarEvent } from "../types/calendar";

export function getPets(): Promise<Pet[]> {
  return apiGet<Pet[]>("/pets/");
}

export function getPet(petId: number): Promise<Pet> {
  return apiGet<Pet>(`/pets/${petId}`);
}

export function getPetCalendar(
  petId: number,
  startDate: string,
  endDate: string,
): Promise<CalendarEvent[]> {
  return apiGet<CalendarEvent[]>(
    `/pets/${petId}/calendar?start_date=${startDate}&end_date=${endDate}`,
  );
}
