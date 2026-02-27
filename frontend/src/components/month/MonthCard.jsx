/**
 * MonthCard Component
 * Display individual month information
 */

import React from 'react';
import { useNavigate } from 'react-router-dom';

const MonthCard = ({ month, shopId }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/shop/${shopId}/month/${month.id}/upload`);
  };

  return (
    <div className="month-card" onClick={handleClick}>
      <div className="month-header">
        <h3>{month.month}</h3>
      </div>
      <div className="month-details">
        <p className="invoice-count">
          Invoices: {month.invoiceCount || 0}
        </p>
        <p className="created-date">
          Created: {new Date(month.createdAt).toLocaleDateString()}
        </p>
      </div>
    </div>
  );
};

export default MonthCard;
