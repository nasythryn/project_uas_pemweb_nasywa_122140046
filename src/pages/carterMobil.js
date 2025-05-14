import React from 'react';
import carterData from '../data/carterData';
import './carterMobil.css';

function CarterMobil() {
  return (
    <div className="carter-container">
      <h2 className="carter-title">Layanan Carter Mobil</h2>
      <div className="carter-grid">
        {carterData.map(carter => (
          <div key={carter.id} className="carter-card">
            <h3>{carter.car_type}</h3>
            <p>Supir: {carter.driver_name}</p>
            <p>Tanggal: {carter.date}</p>
            <a href="/carter/form" className="carter-btn">Pesan Carter</a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CarterMobil;
