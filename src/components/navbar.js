import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light px-3">
      <Link className="navbar-brand" to="/">TravelEase</Link>
      <div className="navbar-nav">
        <Link className="nav-link" to="/booking">Travel Booking</Link>
        <Link className="nav-link" to="/carter">Carter Mobil</Link>
      </div>
    </nav>
  );
}

export default Navbar;
