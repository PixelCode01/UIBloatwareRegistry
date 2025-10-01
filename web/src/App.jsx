import { useState, useEffect, useMemo } from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import FilterPanel from './components/FilterPanel';
import PackageCard from './components/PackageCard';
import './App.css';

function App() {
  const [packages, setPackages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedBrands, setSelectedBrands] = useState([]);
  const [selectedRisks, setSelectedRisks] = useState([]);

  useEffect(() => {
    fetch('./data.json')
      .then(res => {
        if (!res.ok) throw new Error('Failed to load data');
        return res.json();
      })
      .then(data => {
        setPackages(data.packages || []);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const brands = useMemo(() => {
    const brandSet = new Set();
    packages.forEach(pkg => brandSet.add(pkg.brand));
    return Array.from(brandSet).sort();
  }, [packages]);

  const filteredPackages = useMemo(() => {
    return packages.filter(pkg => {
      const matchesSearch = 
        pkg.package.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (pkg.description && pkg.description.toLowerCase().includes(searchQuery.toLowerCase()));
      
      const matchesBrand = selectedBrands.length === 0 || selectedBrands.includes(pkg.brand);
      const matchesRisk = selectedRisks.length === 0 || selectedRisks.includes(pkg.risk);

      return matchesSearch && matchesBrand && matchesRisk;
    });
  }, [packages, searchQuery, selectedBrands, selectedRisks]);

  if (loading) {
    return (
      <div className="app">
        <Header />
        <div className="loading">Loading packages...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <Header />
        <div className="error">Error: {error}</div>
      </div>
    );
  }

  return (
    <div className="app">
      <Header />
      
      <div className="container">
        <div className="sidebar">
          <SearchBar 
            value={searchQuery} 
            onChange={setSearchQuery} 
          />
          
          <FilterPanel
            brands={brands}
            selectedBrands={selectedBrands}
            setSelectedBrands={setSelectedBrands}
            selectedRisks={selectedRisks}
            setSelectedRisks={setSelectedRisks}
          />
        </div>

        <div className="main-content">
          <div className="results-info">
            Found {filteredPackages.length} package{filteredPackages.length !== 1 ? 's' : ''}
          </div>

          <div className="package-grid">
            {filteredPackages.map((pkg, index) => (
              <PackageCard key={`${pkg.brand}-${pkg.package}-${index}`} package={pkg} />
            ))}
          </div>

          {filteredPackages.length === 0 && (
            <div className="no-results">
              No packages found matching your criteria.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
