import React from 'react';
import logo from '../../assests/logo.png';

function Header() {
  return (
    <header className='header'>
        <img src={logo} alt="Example"/>
        <h1>Digi-Kabootar</h1>
    </header>
  );
}

export default Header;