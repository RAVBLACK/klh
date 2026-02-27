/**
 * AddShopModal Component
 * Modal for creating new shop
 */

import React, { useState } from 'react';
import Modal from '../common/Modal';
import Input from '../common/Input';
import Select from '../common/Select';
import Button from '../common/Button';

const AddShopModal = ({ isOpen, onClose, onSubmit }) => {
  const [formData, setFormData] = useState({
    shopName: '',
    shopType: '',
    customerName: ''
  });

  const shopTypes = [
    { value: 'retail', label: 'Retail' },
    { value: 'wholesale', label: 'Wholesale' },
    { value: 'service', label: 'Service' },
    { value: 'manufacturing', label: 'Manufacturing' }
  ];

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
    setFormData({ shopName: '', shopType: '', customerName: '' });
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Add New Shop">
      <form onSubmit={handleSubmit}>
        <Input
          label="Shop Name"
          name="shopName"
          value={formData.shopName}
          onChange={handleChange}
          placeholder="Enter shop name"
          required
        />
        <Select
          label="Shop Type"
          name="shopType"
          value={formData.shopType}
          onChange={handleChange}
          options={shopTypes}
          required
        />
        <Input
          label="Customer Name"
          name="customerName"
          value={formData.customerName}
          onChange={handleChange}
          placeholder="Enter customer name"
          required
        />
        <Button type="submit">Create Shop</Button>
      </form>
    </Modal>
  );
};

export default AddShopModal;
