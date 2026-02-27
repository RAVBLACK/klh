/**
 * Shop Dashboard Page
 * Display list of all shops
 */

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../components/layout/Navbar';
import BottomNav from '../components/layout/BottomNav';
import ShopCard from '../components/shop/ShopCard';
import AddShopModal from '../components/shop/AddShopModal';
import Button from '../components/common/Button';
import Loader from '../components/common/Loader';
import { useShop } from '../hooks/useShop';

const ShopDashboard = () => {
  const navigate = useNavigate();
  const { shops, loading, createShop, fetchShops } = useShop();
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetchShops();
  }, []);

  const handleAddShop = async (shopData) => {
    try {
      await createShop(shopData);
      setIsModalOpen(false);
    } catch (error) {
      console.error('Failed to create shop:', error);
    }
  };

  if (loading) {
    return <Loader />;
  }

  return (
    <div className="shop-dashboard">
      <Navbar title="My Shops" />
      
      <div className="dashboard-content">
        <div className="dashboard-header">
          <h1>Select a Shop</h1>
          <Button onClick={() => setIsModalOpen(true)}>
            + Add Shop
          </Button>
        </div>

        <div className="shops-grid">
          {shops.length === 0 ? (
            <div className="empty-state">
              <p>No shops yet. Create your first shop!</p>
            </div>
          ) : (
            shops.map((shop) => (
              <ShopCard key={shop.id} shop={shop} />
            ))
          )}
        </div>
      </div>

      <AddShopModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handleAddShop}
      />

      <BottomNav />
    </div>
  );
};

export default ShopDashboard;
