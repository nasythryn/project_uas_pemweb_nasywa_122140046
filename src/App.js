import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/navbar';
import Home from './pages/home';
import TravelBooking from './pages/travelBooking';
import CarterMobil from './pages/carterMobil';
import FormBooking from './pages/formBooking';


function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/booking" element={<TravelBooking />} />
        <Route path="/carter" element={<CarterMobil />} />
        <Route path="/booking/form" element={<FormBooking />} />
      </Routes>
    </Router>
  );
}

export default App;
