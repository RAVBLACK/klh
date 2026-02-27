/**
 * useShop Hook
 * Custom hook for shop operations
 */

import { useShopContext } from '../context/ShopContext';

export const useShop = () => {
  return useShopContext();
};
