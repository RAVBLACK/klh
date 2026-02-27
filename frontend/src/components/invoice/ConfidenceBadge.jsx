/**
 * Confidence Badge Component
 * Shows AI extraction confidence level
 */

import React from 'react';

export default function ConfidenceBadge({ confidence }) {
  return (
    <div>
      <span>Confidence: {confidence}%</span>
    </div>
  );
}
