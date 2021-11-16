import express from 'express';
import morgan from 'morgan';
import cors from 'cors';
// import sequelize from './config/sequelize';
import dotenv from 'dotenv';

dotenv.config();
const app = express();
const port = process.env.PHASE === 'prod' ? 80 : 8080;

/* json parse */
app.use(express.json());

/* cors */
app.use(cors({ origin: true, credentials: true }));

/* logging */
app.use(morgan('common'));

/* test */
app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('*', (req, res) => {
  res.status(404).send('not found');
});

/* default 404 */
app.get('*', (req, res) => {
  res.status(404).send('not found');
});

/* error catch */
// app.use(function (err, req, res, next) {
//   console.error(err.stack);
//   res.status(err.status || 500).send(err?.message || 'server error!');
// });

app.use(function (err, req, res, next) {
  console.error(err.stack);
  res.status(500).send('server error!');
});

/* listening port */
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

/* db connecting */
// const db_connect = async () => {
//   try {
//     await sequelize.authenticate();
//     await sequelize.sync({ alter: true, force: true });
//     console.log('Connection has been established successfully.');
//   } catch (error) {
//     console.error('Unable to connect to the database:', error);
//   }
// };

// db_connect();

export default app;
