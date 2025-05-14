import React, { useState } from 'react';
import travelSchedules from '../data/travelSchedules';

function FormBooking() {
  const [form, setForm] = useState({
    scheduleId: '',
    passengers: 1,
    name: ''
  });

  const [submitted, setSubmitted] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const schedule = travelSchedules.find(s => s.id === parseInt(form.scheduleId));
    setSubmitted({
      ...form,
      schedule
    });
  };

  return (
    <div className="container mt-4">
      <h2>Form Pemesanan Travel</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Nama Pemesan</label>
          <input
            type="text"
            className="form-control"
            name="name"
            value={form.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Pilih Jadwal Travel</label>
          <select
            name="scheduleId"
            className="form-select"
            value={form.scheduleId}
            onChange={handleChange}
            required
          >
            <option value="">-- Pilih Jadwal --</option>
            {travelSchedules.map(s => (
              <option key={s.id} value={s.id}>
                {s.route} - {s.date}
              </option>
            ))}
          </select>
        </div>
        <div className="mb-3">
          <label className="form-label">Jumlah Penumpang</label>
          <input
            type="number"
            className="form-control"
            name="passengers"
            value={form.passengers}
            min={1}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">Pesan</button>
      </form>

      {submitted && (
        <div className="alert alert-success mt-4">
          <h4>Pesanan Berhasil!</h4>
          <p>Nama: {submitted.name}</p>
          <p>Jadwal: {submitted.schedule.route} - {submitted.schedule.date}</p>
          <p>Jumlah Penumpang: {submitted.passengers}</p>
        </div>
      )}
    </div>
  );
}

export default FormBooking;
