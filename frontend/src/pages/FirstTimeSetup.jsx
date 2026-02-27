/**
 * First Time Setup Page
 * Onboarding flow for new users
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Input from '../components/common/Input';
import Select from '../components/common/Select';
import Button from '../components/common/Button';
import { useShop } from '../hooks/useShop';

const FirstTimeSetup = () => {
  const navigate = useNavigate();
  const { createShop } = useShop();
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    shopName: '',
    shopType: '',
    customerName: '',
    month: ''
  });

  const shopTypes = [
    { value: 'retail', label: 'Retail' },
    { value: 'wholesale', label: 'Wholesale' },
    { value: 'service', label: 'Service' },
    { value: 'manufacturing', label: 'Manufacturing' }
  ];

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

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleNext = () => {
    setStep(step + 1);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createShop(formData);
      navigate('/shops');
    } catch (error) {
      console.error('Setup failed:', error);
    }
  };

  return (
    <div className="first-time-setup">
      <div className="setup-header">
        <h1>Welcome! Let's set up your account</h1>
        <p>Step {step} of 4</p>
      </div>

      <form onSubmit={handleSubmit} className="setup-form">
        {step === 1 && (
          <div className="setup-step">
            <h2>Shop Information</h2>
            <Input
              label="Shop Name"
              name="shopName"
              value={formData.shopName}
              onChange={handleChange}
              placeholder="Enter your shop name"
              required
            />
            <Button type="button" onClick={handleNext}>
              Next
            </Button>
          </div>
        )}

        {step === 2 && (
          <div className="setup-step">
            <h2>Shop Type</h2>
            <Select
              label="Select Shop Type"
              name="shopType"
              value={formData.shopType}
              onChange={handleChange}
              options={shopTypes}
              required
            />
            <Button type="button" onClick={handleNext}>
              Next
            </Button>
          </div>
        )}

        {step === 3 && (
          <div className="setup-step">
            <h2>Customer Information</h2>
            <Input
              label="Customer Name"
              name="customerName"
              value={formData.customerName}
              onChange={handleChange}
              placeholder="Enter customer name"
              required
            />
            <Button type="button" onClick={handleNext}>
              Next
            </Button>
          </div>
        )}

        {step === 4 && (
          <div className="setup-step">
            <h2>Starting Month</h2>
            <Select
              label="Select Month"
              name="month"
              value={formData.month}
              onChange={handleChange}
              options={months}
              required
            />
            <Button type="submit">
              Complete Setup
            </Button>
          </div>
        )}
      </form>
    </div>
  );
};

export default FirstTimeSetup;
