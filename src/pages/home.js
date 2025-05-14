import React from 'react';
import '../home.css';

function Home() {
  return (
    <div className="hero-section">
      <div className="hero-text">
        <h1>Your Favourite Travel Experience</h1>
        <h2>Delivered Fast & Safe</h2>
        <p>
          TravelEase siap mengantar Anda antar kota dengan nyaman dan aman.
          Pemesanan cepat, transparan, dan didukung driver berpengalaman.
        </p>
        <a href="/booking" className="cta-button">Book Now ➜</a>
      </div>
      <div className="hero-image">
        <img src="/hiace-img.png" alt="TravelEase Hero" />
      </div>
    </div>
  );
}

export default Home;
