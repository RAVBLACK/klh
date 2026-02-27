/**
 * Button Component
 * Reusable button component
 */

import React from 'react';

export default function Button({ children, onClick, disabled, variant = 'primary' }) {
  return (
    <button onClick={onClick} disabled={disabled}>
      {children}
    </button>
  );
}
