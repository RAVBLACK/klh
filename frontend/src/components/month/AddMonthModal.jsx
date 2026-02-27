/**
 * AddMonthModal Component
 * Modal for adding new month
 */

import React, { useState } from 'react';
import Modal from '../common/Modal';
import Select from '../common/Select';
import Button from '../common/Button';

const AddMonthModal = ({ isOpen, onClose, onSubmit, shopId }) => {
  const [month, setMonth] = useState('');

  const months = [
    { value: 'January', label: 'January' },
    { value: 'February', label: 'February' },
    { value: 'March', label: 'March' },
    { value: 'April', label: 'April' },
    { value: 'May', label: 'May' },
    { value: 'June', label: 'June' },
    { value: 'July', label: 'July' },
    { value: 'August', label: 'August' },
    { value: 'September', label: 'September' },
    { value: 'October', label: 'October' },
    { value: 'November', label: 'November' },
    { value: 'December', label: 'December' }
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ shopId, month });
    setMonth('');
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Add New Month">
      <form onSubmit={handleSubmit}>
        <Select
          label="Select Month"
          name="month"
          value={month}
          onChange={(e) => setMonth(e.target.value)}
          options={months}
          required
        />
        <Button type="submit">Add Month</Button>
      </form>
    </Modal>
  );
};

export default AddMonthModal;
