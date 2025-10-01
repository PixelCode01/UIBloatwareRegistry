import './PackageCard.css';

function PackageCard({ package: pkg }) {
  return (
    <div className="package-card">
      <div className="package-header">
        <span className="brand-badge">{pkg.brand}</span>
        <span className={`risk-badge risk-${pkg.risk}`}>
          {pkg.risk}
        </span>
      </div>
      
      <h3 className="package-name">{pkg.package}</h3>
      
      {pkg.description && (
        <p className="package-description">{pkg.description}</p>
      )}
      
      <div className="package-footer">
        <code className="package-code">{pkg.package}</code>
      </div>
    </div>
  );
}

export default PackageCard;
