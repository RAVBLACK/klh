/**
 * Month Dashboard Page
 * Display all months for a shop
 */

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Navbar from '../components/layout/Navbar';
import BottomNav from '../components/layout/BottomNav';
import MonthCard from '../components/month/MonthCard';
import AddMonthModal from '../components/month/AddMonthModal';
import Button from '../components/common/Button';
import Loader from '../components/common/Loader';
import { useShop } from '../hooks/useShop';

const MonthDashboard = () => {
  const { shopId } = useParams();
  const navigate = useNavigate();
  const { currentShop, months, loading, fetchShopMonths, createMonth } = useShop();
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    if (shopId) {
      fetchShopMonths(shopId);
    }
  }, [shopId]);

  const handleAddMonth = async (monthData) => {
    try {
      await createMonth(monthData);
      setIsModalOpen(false);
    } catch (error) {
      console.error('Failed to create month:', error);
    }
  };

  if (loading) {
    return <Loader />;
  }

  return (
    <div className="month-dashboard">
      <Navbar 
        title={currentShop?.shopName || 'Months'} 
        showBack 
        onBack={() => navigate('/shops')}
      />
      
      <div className="dashboard-content">
        <div className="dashboard-header">
          <h1>Select a Month</h1>
          <Button onClick={() => setIsModalOpen(true)}>
            + Add Month
          </Button>
        </div>

        <div className="months-grid">
          {months.length === 0 ? (
            <div className="empty-state">
              <p>No months yet. Add your first month!</p>
            </div>
          ) : (
            months.map((month) => (
              <MonthCard key={month.id} month={month} shopId={shopId} />
            ))
          )}
        </div>
      </div>

      <AddMonthModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handleAddMonth}
        shopId={shopId}
      />

      <BottomNav />
    </div>
  );
};

export default MonthDashboard;
