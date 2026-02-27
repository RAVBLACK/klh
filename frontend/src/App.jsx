/**
 * App Component
 * Main application component
 */

import React from 'react';
import { AuthProvider } from './context/AuthContext';
import { UserProvider } from './context/UserContext';

function App() {
  return (
    <AuthProvider>
      <UserProvider>
        <div className="App">
          <h1>GST Filing Copilot</h1>
        </div>
      </UserProvider>
    </AuthProvider>
  );
}

export default App;
