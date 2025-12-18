import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/octofitapp-small.png';

const OctofitLogo = () => (
  <Link className="navbar-brand d-flex align-items-center" to="/">
    <img src={logo} alt="Octofit Logo" style={{ height: '40px', marginRight: '10px' }} />
    <span className="fw-bold">Octofit Tracker</span>
  </Link>
);

export default OctofitLogo;
