/**
 * Message Bubble Component
 * Individual chat message display
 */

import React from 'react';

export default function MessageBubble({ message, isUser }) {
  return (
    <div>
      <p>{message}</p>
    </div>
  );
}
