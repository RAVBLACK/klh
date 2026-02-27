/**
 * useInvoices Hook
 * Custom hook for invoice data management
 */

import { useState, useEffect } from 'react';

export function useInvoices() {
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(false);

  return { invoices, loading, setInvoices };
}
