/**
 * Home Page
 * Landing page with About and Start button
 */

import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import Button from '../components/common/Button';

const Home = () => {
  const navigate = useNavigate();
  const { user } = useAuth();

  React.useEffect(() => {
    if (user) {
      navigate('/shops');
    }
  }, [user, navigate]);

  return (
    <div className="home-page">
      <header className="home-header">
        <h1>GST Filing Copilot</h1>
        <p className="tagline">AI-Powered Mobile GST Filing Assistant</p>
      </header>

      <section className="about-section">
        <h2>About</h2>
        <p>
          Simplify your GST filing process with our AI-powered mobile assistant.
          Capture invoices with your camera, extract data automatically, and
          generate GSTR-1 reports effortlessly.
        </p>
        
        <div className="features">
          <div className="feature">
            <h3>📸 Smart Capture</h3>
            <p>Capture invoices using your mobile camera</p>
          </div>
          <div className="feature">
            <h3>🤖 AI Extraction</h3>
            <p>Automatic data extraction with high accuracy</p>
          </div>
          <div className="feature">
            <h3>📊 GSTR-1 Generation</h3>
            <p>Generate compliant GST reports instantly</p>
          </div>
          <div className="feature">
            <h3>💬 AI Copilot</h3>
            <p>Get instant explanations for GST queries</p>
          </div>
        </div>
      </section>

      <div className="cta-section">
        <Button onClick={() => navigate('/login')}>
          Get Started
        </Button>
        <p className="login-link">
          Already have an account? <a href="/login">Login</a>
        </p>
      </div>
    </div>
  );
};

export default Home;
