import React, { useMemo, useState, useRef, useEffect } from 'react';

export default function Header({ gems, practitioners, filterType, setFilterType, filterValue, setFilterValue, onSearchSelect, activeTab, onTabChange }) {
  const [query, setQuery] = useState('');
  const [showResults, setShowResults] = useState(false);
  const searchRef = useRef();
  const lastResultsRef = useRef([]);

  const allDomains = useMemo(() => {
    const set = new Set();
    gems.forEach(g => g.domains.forEach(d => set.add(d)));
    return [...set].sort();
  }, [gems]);

  const eventCount = useMemo(() => gems.reduce((sum, g) => sum + g.events.length, 0), [gems]);

  const searchResults = useMemo(() => {
    if (!query.trim() || query.length < 2) return [];
    const q = query.toLowerCase();
    const seen = new Set();
    const tiers = [[], [], [], []]; // [gem name/alias, practitioner name, event name, soft matches]

    for (const gem of gems) {
      const gemId = `gem:${gem.name}`;
      // Tier 1: gem name or alias matches
      if (gem.name.toLowerCase().includes(q) || (gem.aliases || []).some(a => a.toLowerCase().includes(q))) {
        if (!seen.has(gemId)) { seen.add(gemId); tiers[0].push({ id: gemId, type: 'gem', label: gem.name, data: gem }); }
      }
    }

    for (const gem of gems) {
      const gemId = `gem:${gem.name}`;
      // Tier 2: practitioner name matches → surface the gem
      for (const p of gem.practitioners) {
        if (p.name.toLowerCase().includes(q) && !seen.has(gemId)) {
          seen.add(gemId);
          tiers[1].push({ id: gemId, type: 'gem', label: gem.name, data: gem, matchedPractitioner: p.name });
          break;
        }
      }
    }

    for (const gem of gems) {
      // Tier 3: event name matches
      for (const e of gem.events) {
        const eId = `event:${gem.name}:${e.name}`;
        if (e.name.toLowerCase().includes(q) && !seen.has(eId)) {
          seen.add(eId);
          tiers[2].push({ id: eId, type: 'event', label: e.name, data: { ...e, gemName: gem.name } });
        }
      }
    }

    for (const gem of gems) {
      const gemId = `gem:${gem.name}`;
      // Tier 4: application text or event description — broadest, lowest priority
      for (const p of gem.practitioners) {
        if ((p.application || '').toLowerCase().includes(q) && !seen.has(gemId)) {
          seen.add(gemId);
          tiers[3].push({ id: gemId, type: 'gem', label: gem.name, data: gem, matchedPractitioner: p.name });
          break;
        }
      }
    }

    return [...tiers[0], ...tiers[1], ...tiers[2], ...tiers[3]].slice(0, 12);
  }, [query, gems]);
  lastResultsRef.current = searchResults;

  useEffect(() => {
    function handleClick(e) {
      if (searchRef.current && !searchRef.current.contains(e.target)) setShowResults(false);
    }
    document.addEventListener('mousedown', handleClick);
    document.addEventListener('touchstart', handleClick);
    return () => { document.removeEventListener('mousedown', handleClick); document.removeEventListener('touchstart', handleClick); };
  }, []);

  const handleSelect = (result) => {
    onSearchSelect(result);
    setQuery('');
    setShowResults(false);
  };

  const handleFilterChange = (type, value) => {
    setFilterType(type);
    setFilterValue(value);
  };

  const clearFilter = () => {
    setFilterType('all');
    setFilterValue('');
  };

  const typeColor = { gem: 'text-pantheon-gem', practitioner: 'text-pantheon-practitioner', event: 'text-pantheon-event' };

  return (
    <header className="bg-pantheon-card border-b border-pantheon-border px-4 py-3 flex flex-col sm:flex-row sm:items-center sm:justify-between flex-shrink-0 gap-2">
      <div className="flex items-center gap-4 flex-shrink-0">
        <h1 className="font-display text-xl text-pantheon-accent tracking-wide">PANTHEON</h1>
        <div className="h-6 w-px bg-pantheon-border" />
        {/* Tab switcher */}
        <div className="flex gap-1">
          <button
            onClick={() => onTabChange('graph')}
            className={`px-3 py-1 text-xs rounded transition-colors ${activeTab === 'graph' ? 'bg-pantheon-accent/20 text-pantheon-accent' : 'text-pantheon-muted hover:text-pantheon-text'}`}
          >
            Graph
          </button>
          <button
            onClick={() => onTabChange('historian')}
            className={`px-3 py-1 text-xs rounded transition-colors ${activeTab === 'historian' ? 'bg-pantheon-accent/20 text-pantheon-accent' : 'text-pantheon-muted hover:text-pantheon-text'}`}
          >
            Historian
          </button>
          <button
            onClick={() => onTabChange('run')}
            className={`px-3 py-1 text-xs rounded transition-colors ${activeTab === 'run' ? 'bg-pantheon-accent/20 text-pantheon-accent' : 'text-pantheon-muted hover:text-pantheon-text'}`}
          >
            Run
          </button>
        </div>
        <div className="h-6 w-px bg-pantheon-border hidden sm:block" />
        <div className="hidden sm:flex items-center gap-2 text-sm text-pantheon-muted">
          <span className="inline-block w-3 h-3 rotate-45 bg-pantheon-gem" /> {gems.length} gems
          <span className="ml-2 inline-block w-3 h-3 rounded-full bg-pantheon-practitioner" /> {practitioners.length} practitioners
          <span className="ml-2 inline-block w-3 h-3 rounded-sm bg-pantheon-event" /> {eventCount} events
        </div>
      </div>
      <div className="flex items-center gap-3 overflow-x-auto pb-1 sm:pb-0 flex-nowrap">
        {/* Global search */}
        <div ref={searchRef} className="relative">
          <input
            type="text"
            placeholder="Search gems, people, events..."
            value={query}
            onChange={e => { setQuery(e.target.value); setShowResults(true); }}
            onFocus={() => setShowResults(true)}
            onKeyDown={e => { if (e.key === 'Enter' && lastResultsRef.current.length > 0) handleSelect(lastResultsRef.current[0]); }}
            className="bg-pantheon-bg border border-pantheon-border rounded-lg px-3 py-1.5 text-sm w-40 sm:w-56 focus:outline-none focus:border-pantheon-accent placeholder:text-pantheon-muted/50"
          />
          {showResults && searchResults.length > 0 && (
            <div className="absolute top-full mt-1 left-0 w-80 bg-pantheon-card border border-pantheon-border rounded-lg shadow-xl z-50 overflow-hidden">
              {searchResults.map(r => (
                <button key={r.id} onClick={() => handleSelect(r)}
                  className="w-full text-left px-3 py-2 hover:bg-pantheon-border/40 transition-colors flex items-center gap-2 border-b border-pantheon-border/30 last:border-0">
                  <span className={`text-[10px] uppercase tracking-wider w-16 flex-shrink-0 ${typeColor[r.type]}`}>{r.type}</span>
                  <span className="text-sm truncate">{r.label}</span>
                  {r.type === 'gem' && r.matchedPractitioner && (
                    <span className="text-[10px] text-pantheon-muted ml-auto flex-shrink-0">via {r.matchedPractitioner}</span>
                  )}
                  {r.type === 'event' && (
                    <span className="text-[10px] text-pantheon-muted ml-auto flex-shrink-0">via {r.data.gemName}</span>
                  )}
                </button>
              ))}
            </div>
          )}
          {showResults && query.length >= 2 && searchResults.length === 0 && (
            <div className="absolute top-full mt-1 left-0 w-80 bg-pantheon-card border border-pantheon-border rounded-lg shadow-xl z-50 px-3 py-2 text-xs text-pantheon-muted">
              No matches for "{query}"
            </div>
          )}
        </div>

        {activeTab === 'graph' && (
          <>
            <select
              className="bg-pantheon-bg border border-pantheon-border rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:border-pantheon-accent"
              value={filterType === 'practitioner' ? filterValue : ''}
              onChange={e => handleFilterChange('practitioner', e.target.value)}
            >
              <option value="">All Practitioners</option>
              {[...practitioners].sort((a, b) => a.name < b.name ? -1 : a.name > b.name ? 1 : 0).map(p => (
                <option key={p.name} value={p.name}>{p.name}</option>
              ))}
            </select>
            <select
              className="bg-pantheon-bg border border-pantheon-border rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:border-pantheon-accent"
              value={filterType === 'gem' ? filterValue : ''}
              onChange={e => handleFilterChange('gem', e.target.value)}
            >
              <option value="">All Gems</option>
              {[...gems].sort((a, b) => a.name < b.name ? -1 : a.name > b.name ? 1 : 0).map(g => (
                <option key={g.name} value={g.name}>{g.name}</option>
              ))}
            </select>
            <select
              className="bg-pantheon-bg border border-pantheon-border rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:border-pantheon-accent"
              value={filterType === 'domain' ? filterValue : ''}
              onChange={e => handleFilterChange('domain', e.target.value)}
            >
              <option value="">All Domains</option>
              {allDomains.map(d => (
                <option key={d} value={d}>{d}</option>
              ))}
            </select>
            <select
              className="bg-pantheon-bg border border-pantheon-border rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:border-pantheon-accent"
              value={filterType === 'origin' ? filterValue : ''}
              onChange={e => handleFilterChange('origin', e.target.value)}
            >
              <option value="">All Origins</option>
              <option value="authored">✦ Authored</option>
              <option value="historian">Historian</option>
            </select>
            {filterValue && (
              <button onClick={clearFilter} className="text-xs text-pantheon-muted hover:text-pantheon-accent transition-colors px-2 py-1 border border-pantheon-border rounded-lg">Clear</button>
            )}
          </>
        )}
      <a
        href="https://github.com/dkschrei/pantheon"
        target="_blank"
        rel="noopener noreferrer"
        className="flex-shrink-0 text-pantheon-muted hover:text-pantheon-accent transition-colors"
        title="View on GitHub"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z" />
        </svg>
      </a>
      </div>
    </header>
  );
}
