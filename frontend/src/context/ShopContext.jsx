/**
 * Shop Context
 * Global state management for shops and months
 */

import React, { createContext, useState, useContext } from 'react';
import { shopService } from '../services/shopService';
import { monthService } from '../services/monthService';
import { useAuth } from '../hooks/useAuth';

const ShopContext = createContext();

export const ShopProvider = ({ children }) => {
  const { user } = useAuth();
  const [shops, setShops] = useState([]);
  const [currentShop, setCurrentShop] = useState(null);
  const [months, setMonths] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch all shops
  const fetchShops = async () => {
    if (!user) return;
    
    setLoading(true);
    try {
      const userShops = await shopService.getUserShops(user.uid);
      setShops(userShops);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Create new shop
  const createShop = async (shopData) => {
    if (!user) return;
    
    setLoading(true);
    try {
      const newShop = await shopService.createShop(user.uid, shopData);
      setShops([...shops, newShop]);
      setError(null);
      return newShop;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  // Fetch months for a shop
  const fetchShopMonths = async (shopId) => {
    setLoading(true);
    try {
      const shop = await shopService.getShop(shopId);
      setCurrentShop(shop);
      
      const shopMonths = await monthService.getShopMonths(shopId);
      setMonths(shopMonths);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Create new month
  const createMonth = async (monthData) => {
    setLoading(true);
    try {
      const newMonth = await monthService.createMonth(monthData.shopId, monthData);
      setMonths([...months, newMonth]);
      setError(null);
      return newMonth;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const value = {
    shops,
    currentShop,
    months,
    loading,
    error,
    fetchShops,
    createShop,
    fetchShopMonths,
    createMonth
  };

  return <ShopContext.Provider value={value}>{children}</ShopContext.Provider>;
};

export const useShopContext = () => {
  const context = useContext(ShopContext);
  if (!context) {
    throw new Error('useShopContext must be used within ShopProvider');
  }
  return context;
};
