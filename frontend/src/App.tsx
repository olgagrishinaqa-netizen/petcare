import { useEffect, useState } from "react";
import { getPets } from "./api/pets";
import type { Pet } from "./types/pet";
import "./App.css";
import PetPage from "./pages/PetPage";

function App() {
  const [pets, setPets] = useState<Pet[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedPet, setSelectedPet] = useState<Pet | null>(null);

  useEffect(() => {
    getPets()
      .then((data) => {
        setPets(data);
      })
      .catch((err) => {
        setError(err instanceof Error ? err.message : "Ошибка загрузки");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);
if (selectedPet) {
  return (
    <div className="app">
      <header className="header">
        <div className="logo">
          🐾 <span>PetCare</span>
        </div>
      </header>

      <PetPage
        pet={selectedPet}
        onBack={() => setSelectedPet(null)}
      />
    </div>
  );
}

  return (
    <div className="app">
      <header className="header">
        <div className="logo">
          🐾 <span>PetCare</span>
        </div>

        <button className="profile-button">
          👤 Профиль
        </button>
      </header>

      <main className="main">
        <section className="welcome">
          <p className="welcome-label">Добро пожаловать!</p>
          <h1>Мои питомцы</h1>
          <p className="subtitle">
            Забота о здоровье питомца — всё в одном месте.
          </p>
        </section>

        <section className="pets-section">
          {loading && (
            <div className="status-card">
              Загрузка питомцев...
            </div>
          )}

          {error && (
            <div className="status-card error">
              <strong>Не удалось загрузить питомцев</strong>
              <p>{error}</p>
            </div>
          )}

          {!loading && !error && pets.length === 0 && (
            <div className="status-card">
              <div className="empty-icon">🐾</div>
              <h2>Питомцев пока нет</h2>
              <p>Добавьте первого питомца, чтобы начать вести календарь ухода.</p>
            </div>
          )}

          {!loading && !error && pets.length > 0 && (
            <div className="pets-grid">
              {pets.map((pet) => (
                <article className="pet-card" key={pet.id}>
                  <div className="pet-avatar">
                    {pet.species.toLowerCase() === "cat" ||
                    pet.species.toLowerCase() === "кошка"
                      ? "🐱"
                      : "🐶"}
                  </div>

                  <div className="pet-info">
                    <h2>{pet.name}</h2>

                    <p className="pet-species">
                      {pet.species}
                      {pet.breed ? ` • ${pet.breed}` : ""}
                    </p>

                    {pet.birth_date && (
                      <p className="pet-detail">
                        🎂 {pet.birth_date}
                      </p>
                    )}

                    {pet.weight !== null &&
                      pet.weight !== undefined && (
                        <p className="pet-detail">
                          ⚖️ {pet.weight} кг
                        </p>
                      )}
                  </div>

                  <button
                    className="open-button"
                    onClick={() => setSelectedPet(pet)}
                  >
                    Открыть
                  </button>
                </article>
              ))}
            </div>
          )}
        </section>

        <section className="dashboard-grid">
          <article className="dashboard-card">
            <div className="card-icon">📅</div>
            <h2>Календарь</h2>
            <p>
              Вакцинации, обработки и другие важные события.
            </p>
            <button>Открыть календарь</button>
          </article>

          <article className="dashboard-card">
            <div className="card-icon">🔔</div>
            <h2>Напоминания</h2>
            <p>
              Следите за предстоящими процедурами и задачами.
            </p>
            <button>Мои напоминания</button>
          </article>
        </section>
      </main>
    </div>
  );
}

export default App;
