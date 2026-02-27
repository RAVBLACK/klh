/**
 * Invoice Service
 * API calls for invoice management
 */

import { db } from './firebase';
import api from './api';
import { 
  collection, 
  addDoc, 
  getDocs, 
  getDoc,
  doc, 
  query, 
  where,
  updateDoc 
} from 'firebase/firestore';

export const invoiceService = {
  // Upload and process invoice
  async uploadInvoice(monthId, imageFile) {
    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('monthId', monthId);
    
    const response = await api.post('/invoice/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    
    return response.data;
  },

  // Get all invoices for a month
  async getMonthInvoices(monthId) {
    const q = query(collection(db, 'invoices'), where('monthId', '==', monthId));
    const querySnapshot = await getDocs(q);
    return querySnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
  },

  // Get single invoice
  async getInvoice(invoiceId) {
    const invoiceDoc = await getDoc(doc(db, 'invoices', invoiceId));
    if (invoiceDoc.exists()) {
      return { id: invoiceDoc.id, ...invoiceDoc.data() };
    }
    return null;
  },

  // Update invoice
  async updateInvoice(invoiceId, updates) {
    const invoiceRef = doc(db, 'invoices', invoiceId);
    await updateDoc(invoiceRef, updates);
    return { id: invoiceId, ...updates };
  },

  // Validate invoice data
  async validateInvoice(invoiceId) {
    const response = await api.post(`/invoice/${invoiceId}/validate`);
    return response.data;
  }
};
