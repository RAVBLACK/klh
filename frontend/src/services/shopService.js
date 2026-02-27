/**
 * Shop Service
 * API calls for shop management
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

export const shopService = {
  // Create new shop
  async createShop(userId, shopData) {
    const shopRef = await addDoc(collection(db, 'shops'), {
      userId,
      ...shopData,
      createdAt: new Date().toISOString()
    });
    return { id: shopRef.id, ...shopData };
  },

  // Get all shops for a user
  async getUserShops(userId) {
    const q = query(collection(db, 'shops'), where('userId', '==', userId));
    const querySnapshot = await getDocs(q);
    return querySnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
  },

  // Get single shop
  async getShop(shopId) {
    const shopDoc = await getDoc(doc(db, 'shops', shopId));
    if (shopDoc.exists()) {
      return { id: shopDoc.id, ...shopDoc.data() };
    }
    return null;
  },

  // Update shop
  async updateShop(shopId, updates) {
    const shopRef = doc(db, 'shops', shopId);
    await updateDoc(shopRef, updates);
    return { id: shopId, ...updates };
  },

  // Delete shop
  async deleteShop(shopId) {
    await deleteDoc(doc(db, 'shops', shopId));
  }
};
