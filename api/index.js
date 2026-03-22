import { ApolloServer } from '@apollo/server';
import { expressMiddleware } from '@apollo/server/express4';
import express from 'express';
import cors from 'cors';
import { typeDefs } from './schema.js';
import { resolvers } from './resolvers.js';

const app = express();
app.use(cors({ origin: '*' }));
app.use(express.json());

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

await server.start();
app.use('/', expressMiddleware(server));

app.listen(4000, () => {
  console.log('Pantheon GraphQL API running at http://localhost:4000/');
});
