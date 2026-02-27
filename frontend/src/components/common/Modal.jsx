/**
 * Modal Component
 * Reusable modal dialog component
 */

import React from 'react';

export default function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;

  return (
    <div>
      <div>
        {children}
      </div>
    </div>
  );
}
