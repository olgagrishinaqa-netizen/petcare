export interface Pet {
  id: number;
  user_id: number;
  name: string;
  species: string;
  breed?: string | null;
  birth_date?: string | null;
  gender?: string | null;
  weight?: number | null;
  note?: string | null;
}
