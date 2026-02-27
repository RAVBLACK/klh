/**
 * Month Context
 * Global state management for months
 */

import React, { createContext, useState, useContext } from 'react';
import { monthService } from '../services/monthService';

const MonthContext = createContext();

export const MonthProvider = ({ children }) => {
  const [currentMonth, setCurrentMonth] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchMonth = async (monthId) => {
    setLoading(true);
    try {
      const month = await monthService.getMonth(monthId);
      setCurrentMonth(month);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const value = {
    currentMonth,
    loading,
    error,
    fetchMonth
  };

  return <MonthContext.Provider value={value}>{children}</MonthContext.Provider>;
};

export const useMonthContext = () => {
  const context = useContext(MonthContext);
  if (!context) {
    throw new Error('useMonthContext must be used within MonthProvider');
  }
  return context;
};
