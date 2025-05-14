import React from 'react';
import travelSchedules from '../data/travelSchedules';
import './travelBooking.css';

function TravelBooking() {
  return (
    <div className="booking-container">
      <h2 className="booking-title">Jadwal Travel Tersedia</h2>
      <div className="booking-grid">
        {travelSchedules.map(schedule => (
          <div key={schedule.id} className="booking-card">
            <h3>{schedule.route}</h3>
            <p>Tanggal: {schedule.date}</p>
            <p>Kapasitas: {schedule.capacity} penumpang</p>
            <a href="/booking/form" className="booking-btn">Pesan Sekarang</a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TravelBooking;
