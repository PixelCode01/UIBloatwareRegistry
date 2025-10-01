import './SearchBar.css';

function SearchBar({ value, onChange }) {
  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search packages..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="search-input"
      />
      {value && (
        <button 
          className="clear-button" 
          onClick={() => onChange('')}
          aria-label="Clear search"
        >
          ×
        </button>
      )}
    </div>
  );
}

export default SearchBar;
