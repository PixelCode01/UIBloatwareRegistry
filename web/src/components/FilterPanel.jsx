import './FilterPanel.css';

function FilterPanel({ 
  brands, 
  selectedBrands, 
  setSelectedBrands, 
  selectedRisks, 
  setSelectedRisks 
}) {
  const riskLevels = ['safe', 'caution', 'dangerous', 'unknown'];

  const toggleBrand = (brand) => {
    setSelectedBrands(prev => 
      prev.includes(brand) 
        ? prev.filter(b => b !== brand)
        : [...prev, brand]
    );
  };

  const toggleRisk = (risk) => {
    setSelectedRisks(prev => 
      prev.includes(risk) 
        ? prev.filter(r => r !== risk)
        : [...prev, risk]
    );
  };

  const clearFilters = () => {
    setSelectedBrands([]);
    setSelectedRisks([]);
  };

  return (
    <div className="filter-panel">
      <div className="filter-header">
        <h3>Filters</h3>
        {(selectedBrands.length > 0 || selectedRisks.length > 0) && (
          <button className="clear-filters" onClick={clearFilters}>
            Clear All
          </button>
        )}
      </div>

      <div className="filter-section">
        <h4>Brand</h4>
        <div className="filter-options">
          {brands.map(brand => (
            <label key={brand} className="filter-checkbox">
              <input
                type="checkbox"
                checked={selectedBrands.includes(brand)}
                onChange={() => toggleBrand(brand)}
              />
              <span>{brand}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="filter-section">
        <h4>Risk Level</h4>
        <div className="filter-options">
          {riskLevels.map(risk => (
            <label key={risk} className="filter-checkbox">
              <input
                type="checkbox"
                checked={selectedRisks.includes(risk)}
                onChange={() => toggleRisk(risk)}
              />
              <span className={`risk-badge risk-${risk}`}>{risk}</span>
            </label>
          ))}
        </div>
      </div>
    </div>
  );
}

export default FilterPanel;
