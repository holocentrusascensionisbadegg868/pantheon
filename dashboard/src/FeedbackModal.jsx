import React, { useState, useEffect, useRef } from 'react';

const TYPES = [
  { id: 'Challenge', label: 'Challenge' },
  { id: 'Historical case', label: 'Historical case' },
  { id: 'Applied this', label: 'Applied this' },
  { id: 'Question', label: 'Question' },
];

export default function FeedbackModal({ gem, onClose }) {
  const [type, setType] = useState('Challenge');
  const [thought, setThought] = useState('');
  const [handle, setHandle] = useState('');
  const [status, setStatus] = useState('idle'); // idle | submitting | done | error
  const textareaRef = useRef(null);

  useEffect(() => {
    textareaRef.current?.focus();
    const onKey = (e) => { if (e.key === 'Escape') onClose(); };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [onClose]);

  async function handleSubmit(e) {
    e.preventDefault();
    if (!thought.trim()) return;
    setStatus('submitting');
    try {
      const res = await fetch('/api/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ gem: gem.name, type, thought, handle }),
      });
      setStatus(res.ok ? 'done' : 'error');
    } catch {
      setStatus('error');
    }
  }

  return (
    <div
      className="fixed inset-0 z-50 flex items-end sm:items-center justify-center"
      onClick={(e) => { if (e.target === e.currentTarget) onClose(); }}
    >
      {/* backdrop */}
      <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" />

      <div className="relative w-full sm:max-w-md mx-4 mb-0 sm:mb-auto bg-pantheon-card border border-pantheon-border rounded-t-2xl sm:rounded-2xl shadow-2xl overflow-hidden">

        {/* header */}
        <div className="flex items-center justify-between px-5 pt-5 pb-3 border-b border-pantheon-border">
          <div>
            <p className="text-xs text-pantheon-muted uppercase tracking-wider">React to gem</p>
            <h2 className="text-pantheon-accent font-semibold text-sm mt-0.5 uppercase tracking-wide">{gem.name}</h2>
          </div>
          <button onClick={onClose} className="text-pantheon-muted hover:text-pantheon-text transition-colors text-lg leading-none">✕</button>
        </div>

        {status === 'done' ? (
          <div className="px-5 py-10 text-center">
            <div className="text-2xl mb-3">🔮</div>
            <p className="text-pantheon-text font-medium text-sm">Pantheon Gem Researcher notified!</p>
            <p className="text-pantheon-muted text-xs mt-1">Your reaction has been filed.</p>
            <button onClick={onClose} className="mt-6 px-4 py-1.5 text-xs rounded border border-pantheon-border text-pantheon-muted hover:text-pantheon-text transition-colors">
              Close
            </button>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="px-5 pt-4 pb-5 space-y-4">
            {/* type selector */}
            <div>
              <p className="text-xs text-pantheon-muted mb-2">Type</p>
              <div className="flex flex-wrap gap-2">
                {TYPES.map(t => (
                  <button
                    key={t.id}
                    type="button"
                    onClick={() => setType(t.id)}
                    className={`px-3 py-1 rounded text-xs border transition-colors ${
                      type === t.id
                        ? 'border-pantheon-accent text-pantheon-accent bg-pantheon-accent/10'
                        : 'border-pantheon-border text-pantheon-muted hover:border-pantheon-muted'
                    }`}
                  >
                    {t.label}
                  </button>
                ))}
              </div>
            </div>

            {/* thought */}
            <div>
              <p className="text-xs text-pantheon-muted mb-2">Your reaction</p>
              <textarea
                ref={textareaRef}
                value={thought}
                onChange={e => setThought(e.target.value)}
                placeholder={
                  type === 'Challenge' ? "Isn't this what X did when..." :
                  type === 'Historical case' ? "This pattern also appears in..." :
                  type === 'Applied this' ? "I applied this to..." :
                  "I'm curious whether..."
                }
                rows={4}
                className="w-full bg-pantheon-bg border border-pantheon-border rounded-lg px-3 py-2.5 text-xs text-pantheon-text placeholder-pantheon-muted/50 resize-none focus:outline-none focus:border-pantheon-accent/50 transition-colors"
              />
            </div>

            {/* handle */}
            <div>
              <input
                type="text"
                value={handle}
                onChange={e => setHandle(e.target.value)}
                placeholder="Your handle (optional)"
                className="w-full bg-pantheon-bg border border-pantheon-border rounded-lg px-3 py-2 text-xs text-pantheon-text placeholder-pantheon-muted/50 focus:outline-none focus:border-pantheon-accent/50 transition-colors"
              />
            </div>

            {status === 'error' && (
              <p className="text-xs text-red-400">Something went wrong — try again.</p>
            )}

            <div className="flex gap-2 pt-1">
              <button
                type="submit"
                disabled={!thought.trim() || status === 'submitting'}
                className="flex-1 py-2 rounded-lg text-xs font-medium bg-pantheon-accent text-pantheon-bg disabled:opacity-40 disabled:cursor-not-allowed hover:bg-pantheon-accent/90 transition-colors"
              >
                {status === 'submitting' ? 'Sending…' : 'Submit'}
              </button>
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 rounded-lg text-xs border border-pantheon-border text-pantheon-muted hover:text-pantheon-text transition-colors"
              >
                Cancel
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
