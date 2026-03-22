# Pantheon GraphQL API

GraphQL API for the Pantheon library of 33 cognitive patterns (gems).

## Setup

```bash
cd api
npm install
npm start
```

Server starts at **http://localhost:4000/** with Apollo Sandbox for interactive queries.

## Schema Overview

| Type | Description |
|------|-------------|
| `Gem` | A cognitive pattern with aliases, domains, triggers, lineage, practitioners, and events |
| `Practitioner` | A deduplicated person across all gems — includes reverse-lookup of every gem they appear in |
| `GemPractitioner` | A practitioner as they appear on a specific gem (with application context) |
| `Event` | A historical event tied to a gem, with `role` (applied/violated) and description |

## Queries

### All gems
```graphql
query {
  gems {
    name
    domains
    practitioners { name era }
  }
}
```

### Filter gems by domain
```graphql
query {
  gems(domain: "engineering") {
    name
    domains
  }
}
```

### Single gem by name
```graphql
query {
  gem(name: "anomaly-isolation") {
    name
    aliases
    domains
    triggers
    lineage
    originType
    practitioners {
      name
      era
      application
    }
    events {
      name
      year
      role
      description
    }
  }
}
```

### All practitioners (deduplicated)
```graphql
query {
  practitioners {
    name
    gems { name }
  }
}
```

### Single practitioner — all their gems and events
```graphql
query {
  practitioner(name: "Richard Feynman") {
    name
    gems {
      name
      events {
        name
        year
        role
        description
      }
    }
  }
}
```

### All events
```graphql
query {
  events {
    name
    year
    role
    description
    gem { name }
  }
}
```

## Notes

- Gem names match the directory slugs (e.g., `anomaly-isolation`, `feynman-clarity`)
- `year` is always a string — it can be a single year (`"1986"`), a range (`"1943-1945"`), or include BC dates (`"48bc-642ad"`)
- `role` on events is `"applied"` or `"violated"`
- Domain filter is case-insensitive
