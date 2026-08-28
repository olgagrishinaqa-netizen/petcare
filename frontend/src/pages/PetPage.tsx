import type { Pet } from "../types/pet";
import PetCalendar from "../components/PetCalendar";

interface PetPageProps {
  pet: Pet;
  onBack: () => void;
}

function PetPage({ pet, onBack }: PetPageProps) {
  return (
    <main className="main">
      <button className="back-button" onClick={onBack}>
        ← Назад к питомцам
      </button>

      <section className="pet-profile">
        <div className="pet-profile-avatar">
          {pet.species.toLowerCase() === "cat" ||
          pet.species.toLowerCase() === "кошка"
            ? "🐱"
            : "🐶"}
        </div>

        <div>
          <p className="welcome-label">Мой питомец</p>
          <h1>{pet.name}</h1>
          <p className="subtitle">
            {pet.species}
            {pet.breed ? ` • ${pet.breed}` : ""}
          </p>
        </div>
      </section>

      <section className="pet-details-grid">
        <article className="dashboard-card">
          <div className="card-icon">🐾</div>
          <h2>Информация</h2>

          <p>
            <strong>Вид:</strong> {pet.species}
          </p>

          {pet.breed && (
            <p>
              <strong>Порода:</strong> {pet.breed}
            </p>
          )}

          {pet.birth_date && (
            <p>
              <strong>Дата рождения:</strong> {pet.birth_date}
            </p>
          )}

          {pet.weight !== null && pet.weight !== undefined && (
            <p>
              <strong>Вес:</strong> {pet.weight} кг
            </p>
          )}

          {pet.note && (
            <p>
              <strong>Заметка:</strong> {pet.note}
            </p>
          )}
        </article>

        <article className="dashboard-card">
          <div className="card-icon">📅</div>
          <h2>Календарь</h2>
          <p>
            Вакцинации, обработки, напоминания и другие
            события питомца.
          </p>
        </article>

        <article className="dashboard-card">
          <div className="card-icon">🔔</div>
          <h2>Напоминания</h2>
          <p>
            Предстоящие процедуры и важные задачи.
          </p>

          <button>Открыть напоминания</button>
        </article>

        <article className="dashboard-card">
          <div className="card-icon">💉</div>
          <h2>Здоровье</h2>
          <p>
            Вакцинации, обработки от паразитов и медицинские записи.
          </p>

          <button>История здоровья</button>
        </article>
      </section>

      <PetCalendar petId={pet.id} />
    </main>
  );
}

export default PetPage;
