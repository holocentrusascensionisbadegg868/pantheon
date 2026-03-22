import { loadGems, buildPractitionerIndex } from './parser.js';

// Load all data once at startup
const gems = loadGems();
const practitionerIndex = buildPractitionerIndex(gems);
const gemsByName = new Map(gems.map((g) => [g.name, g]));

export const resolvers = {
  Query: {
    gems(_parent, { domain }) {
      if (!domain) return gems;
      return gems.filter((g) =>
        g.domains.some((d) => d.toLowerCase() === domain.toLowerCase())
      );
    },

    gem(_parent, { name }) {
      return gemsByName.get(name) ?? null;
    },

    practitioners() {
      return Array.from(practitionerIndex.values());
    },

    practitioner(_parent, { name }) {
      return practitionerIndex.get(name) ?? null;
    },

    events() {
      return gems.flatMap((g) => g.events);
    },
  },

  GemPractitioner: {
    practitioner(gemPractitioner) {
      return practitionerIndex.get(gemPractitioner.name) ?? null;
    },
  },

  Practitioner: {
    gems(practitioner) {
      return practitioner.gemNames.map((n) => gemsByName.get(n)).filter(Boolean);
    },
  },

  Event: {
    gem(event) {
      return gemsByName.get(event.gemName) ?? null;
    },
  },
};
