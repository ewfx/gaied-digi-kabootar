import React from 'react';
import logo from '../../assests/logo.png';

function Header() {
  return (
    <header className='header'>
        <img src={logo} alt="Example"/>
        <div>Digi-Kabootar</div>
    </header>
  );
}

export default Header;