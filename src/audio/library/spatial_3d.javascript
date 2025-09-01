import { useEffect, useRef } from 'react';

const SpatialAudioEngine = ({ marketData }) => {
  const audioContextRef = useRef(null);
  const audioNodesRef = useRef(new Map());

  useEffect(() => {
    // Initialize Web Audio API
    audioContextRef.current = new (window.AudioContext || window.webkitAudioContext)();
    
    // Create spatialization nodes for each instrument
    initializeSpatialNodes();
    
    return () => {
      if (audioContextRef.current) {
        audioContextRef.current.close();
      }
    };
  }, []);

  useEffect(() => {
    if (marketData && audioContextRef.current) {
      updateMarketAudio(marketData);
    }
  }, [marketData]);

  const initializeSpatialNodes = () => {
    const instruments = ['BTC', 'ETH', 'SOL', 'XLM', 'AVAX'];
    
    instruments.forEach(symbol => {
      const panner = audioContextRef.current.createPanner();
      panner.panningModel = 'HRTF';
      panner.distanceModel = 'inverse';
      panner.refDistance = 1;
      panner.maxDistance = 1000;
      panner.rolloffFactor = 1;
      panner.coneInnerAngle = 360;
      panner.coneOuterAngle = 0;
      panner.coneOuterGain = 0;
      
      // Position in 3D space
      panner.setPosition(
        Math.random() * 10 - 5,  // x: -5 to 5
        Math.random() * 6 - 3,   // y: -3 to 3  
        Math.random() * 8 - 4    // z: -4 to 4
      );
      
      panner.connect(audioContextRef.current.destination);
      audioNodesRef.current.set(symbol, panner);
    });
  };

  const updateMarketAudio = (marketData) => {
    marketData.forEach(data => {
      const panner = audioNodesRef.current.get(data.symbol);
      if (panner) {
        // Update position based on market movements
        const xPos = (data.changePercent / 10) * 5; // X based on change
        const yPos = data.volatility * 3;           // Y based on volatility
        const zPos = (data.volume / 1000000) * 2;   // Z based on volume
        
        panner.setPosition(xPos, yPos, zPos);
        
        // Play sound if significant movement
        if (Math.abs(data.changePercent) > 1.5) {
          playMarketSound(data.symbol, data.changePercent, panner);
        }
      }
    });
  };

  const playMarketSound = (symbol, changePercent, panner) => {
    // Create oscillator for synthetic market sounds
    const oscillator = audioContextRef.current.createOscillator();
    const gainNode = audioContextRef.current.createGain();
    
    // Set frequency based on change direction and magnitude
    const baseFreq = changePercent > 0 ? 440 : 330; // A4 for rise, E4 for fall
    const freqVariation = Math.min(Math.abs(changePercent) * 10, 200);
    
    oscillator.type = changePercent > 0 ? 'sine' : 'sawtooth';
    oscillator.frequency.setValueAtTime(baseFreq, audioContextRef.current.currentTime);
    oscillator.frequency.exponentialRampToValueAtTime(
      baseFreq + freqVariation, 
      audioContextRef.current.currentTime + 0.5
    );
    
    // Configure volume
    gainNode.gain.setValueAtTime(0.1, audioContextRef.current.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(
      0.01, 
      audioContextRef.current.currentTime + 1.5
    );
    
    // Connect and play
    oscillator.connect(gainNode);
    gainNode.connect(panner);
    
    oscillator.start();
    oscillator.stop(audioContextRef.current.currentTime + 1.5);
  };

  return null; // This component doesn't render anything
};

export default SpatialAudioEngine;
