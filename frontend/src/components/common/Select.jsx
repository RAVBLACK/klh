/**
 * Select Component
 * Reusable dropdown select
 */

import React from 'react';

const Select = ({ 
  label, 
  name, 
  value, 
  onChange, 
  options, 
  placeholder = 'Select an option', 
  error, 
  required = false,
  disabled = false 
}) => {
  return (
    <div className="select-wrapper">
      {label && (
        <label htmlFor={name}>
          {label}
          {required && <span className="required">*</span>}
        </label>
      )}
      <select
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        required={required}
        disabled={disabled}
        className={error ? 'select-error' : ''}
      >
        <option value="">{placeholder}</option>
        {options.map((option, index) => (
          <option key={index} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {error && <span className="error-message">{error}</span>}
    </div>
  );
};

export default Select;
