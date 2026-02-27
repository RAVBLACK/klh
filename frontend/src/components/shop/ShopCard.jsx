/**
 * ShopCard Component
 * Display individual shop information
 */

import React from 'react';
import { useNavigate } from 'react-router-dom';

const ShopCard = ({ shop }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/shop/${shop.id}/months`);
  };

  return (
    <div className="shop-card" onClick={handleClick}>
      <div className="shop-header">
        <h3>{shop.shopName}</h3>
        <span className="shop-type">{shop.shopType}</span>
      </div>
      <div className="shop-details">
        <p className="customer-name">{shop.customerName}</p>
        <p className="created-date">
          Created: {new Date(shop.createdAt).toLocaleDateString()}
        </p>
      </div>
    </div>
  );
};

export default ShopCard;
