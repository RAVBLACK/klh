/**
 * Month Service
 * API calls for month management
 */

import { db } from './firebase';
import { 
  collection, 
  addDoc, 
  getDocs, 
  getDoc,
  doc, 
  query, 
  where,
  updateDoc,
  deleteDoc 
} from 'firebase/firestore';

export const monthService = {
  // Create new month
  async createMonth(shopId, monthData) {
    const monthRef = await addDoc(collection(db, 'months'), {
      shopId,
      ...monthData,
      createdAt: new Date().toISOString()
    });
    return { id: monthRef.id, ...monthData };
  },

  // Get all months for a shop
  async getShopMonths(shopId) {
    const q = query(collection(db, 'months'), where('shopId', '==', shopId));
    const querySnapshot = await getDocs(q);
    return querySnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
  },

  // Get single month
  async getMonth(monthId) {
    const monthDoc = await getDoc(doc(db, 'months', monthId));
    if (monthDoc.exists()) {
      return { id: monthDoc.id, ...monthDoc.data() };
    }
    return null;
  },

  // Update month
  async updateMonth(monthId, updates) {
    const monthRef = doc(db, 'months', monthId);
    await updateDoc(monthRef, updates);
    return { id: monthId, ...updates };
  },

  // Delete month
  async deleteMonth(monthId) {
    await deleteDoc(doc(db, 'months', monthId));
  }
};
